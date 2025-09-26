import warnings

import pandas as pd
from scipy.optimize import minimize

from IRS_toolkit.core.leg import fix_leg, float_leg
from datetime import datetime
from dateutil.relativedelta import relativedelta
from IRS_toolkit.core.curve import compounded, yield_curve
from IRS_toolkit.utils import schedule

warnings.filterwarnings("ignore")


class Swap:
    """
    A class that provides various outputs related to swap pricing.


    Args:
        fix_leg (legFix): fixed leg
        float_leg (legFloat): float leg
    """

    def __init__(
        self,
        nominal: float,
        fix_rate: float,
        yield_curve_fix: yield_curve.YieldCurve = None,
        yield_curve_float: yield_curve.YieldCurve = None,
        ESTR_compounded: compounded.Compounded = None,
        schedule_fix: schedule.Schedule = None,
        schedule_float: schedule.Schedule = None,
        relative_delta=None,
        fix_rate_base: int = 1,
    ):
        self.nominal = nominal
        self.fix_rate = fix_rate / fix_rate_base
        self.yield_curve_fix = yield_curve_fix
        self.yield_curve_float = yield_curve_float
        self.ESTR_compounded = ESTR_compounded
        self.schedule_fix = schedule_fix
        self.schedule_float = schedule_float
        self.relative_delta = relative_delta
        self.cashflow = pd.DataFrame()

        fix_leg_object = fix_leg.FixLeg(
            nominal=nominal, fix_rate=self.fix_rate, schedule=schedule_fix
        )

        float_leg_object = float_leg.FloatLeg(
            nominal=nominal,
            yield_curve_object=yield_curve_float,
            schedule=schedule_float,
            ESTR_compounded=ESTR_compounded,
            relative_delta=relative_delta,
        )

        self.fix_leg_object = fix_leg_object
        self.float_leg_object = float_leg_object

    def npv(self, valuation_date: datetime):
        """
        Net present value of the swap with settlement asymmetry detection.

        Now properly handles scenarios where payment date offsets create settlement
        asymmetry between legs (one leg settled, other leg unsettled).

        Args:
            valuation_date (datetime): valuation date

        Returns:
            float: Net present value including settlement effects
        """
        # First compute cash flows for both legs
        self.fix_leg_object.compute_cash_flow(valuation_date)
        self.float_leg_object.compute_cash_flow(valuation_date)

        # Then discount the cash flows (now with settlement detection)
        self.fix_leg_object.discount_cashflow(self.yield_curve_fix, valuation_date)
        self.float_leg_object.discount_cashflow(self.yield_curve_float, valuation_date)

        # Calculate total NPV (fixed payer perspective: pay fixed, receive float)
        self.NPV_ = self.fix_leg_object.NPV - self.float_leg_object.NPV

        # Calculate settlement asymmetry impact
        self._calculate_settlement_asymmetry()

        result_dict = {
            "Nominal": self.nominal,
            "Fix_Rate": self.fix_rate,
            "Valuation_Date": valuation_date,
            "Swap_NPV": self.NPV_,
            "Fixed_Leg_NPV": self.fix_leg_object.NPV,
            "Float_Leg_NPV": self.float_leg_object.NPV,
            "Fixed_Leg_Settled_NPV": getattr(self.fix_leg_object, "settled_npv", 0.0),
            "Fixed_Leg_Future_NPV": getattr(self.fix_leg_object, "future_npv", 0.0),
            "Float_Leg_Settled_NPV": getattr(self.float_leg_object, "settled_npv", 0.0),
            "Float_Leg_Future_NPV": getattr(self.float_leg_object, "future_npv", 0.0),
            "Settlement_Asymmetry_Impact": getattr(
                self, "settlement_asymmetry_impact", 0.0
            ),
            "Accrued_Coupon_Float": self.float_leg_object.accrued_coupon_float,
            "Accrued_Coupon_Fix": self.fix_leg_object.accrued_coupon_fix,
            "Spread_Hedging_Cost": self.fix_leg_object.spreadHC,
            "Spread_Global_Collateral": self.fix_leg_object.spreadGC,
            "Fair_Rate": self.fair_rate(valuation_date)[1],
            "Global_Collateral": self.fix_leg_object.spreadGC
            + self.float_leg_object.accrued_coupon_float,
            "SWAP_ALL_IN": self.fix_leg_object.spreadGC
            + self.float_leg_object.accrued_coupon_float,
        }
        df_str = pd.DataFrame.from_dict(result_dict, orient="index")
        self.df = df_str.T
        self.df["Exit_cost"] = (
            self.df["Swap_NPV"]
            - self.df["Accrued_Coupon_Fix"]
            + self.df["Accrued_Coupon_Float"]
        )
        return self.NPV_

    def _calculate_settlement_asymmetry(self):
        """
        Calculate the impact of settlement asymmetry between legs.

        This captures the economic reality when one leg has settled payments
        while the other leg still has future obligations.
        """
        # Get settlement breakdowns
        fix_settled = getattr(self.fix_leg_object, "settled_npv", 0.0)
        fix_future = getattr(self.fix_leg_object, "future_npv", 0.0)
        float_settled = getattr(self.float_leg_object, "settled_npv", 0.0)
        float_future = getattr(self.float_leg_object, "future_npv", 0.0)

        # Calculate net settlement difference
        net_settled_difference = abs(fix_settled) - abs(float_settled)
        net_future_difference = abs(fix_future) - abs(float_future)

        # Settlement asymmetry impact: difference between what's settled vs what's still future
        # Higher impact when one leg is heavily settled while other is mostly future obligations
        self.settlement_asymmetry_impact = abs(
            net_settled_difference - net_future_difference
        )

        # Store detailed breakdown for analysis
        self.settlement_breakdown = {
            "fixed_leg_settled": fix_settled,
            "fixed_leg_future": fix_future,
            "float_leg_settled": float_settled,
            "float_leg_future": float_future,
            "net_settled_difference": net_settled_difference,
            "net_future_difference": net_future_difference,
            "asymmetry_impact": self.settlement_asymmetry_impact,
        }

    def fair_rate(self, valuation_date: datetime):
        """
        fair rate of the swap

        Args:
            date_valo (date): date valuation
            ImpSchedule (dataframe) : in case you use imported schedule

        Returns:
            float, float: fair rate, theorical fair rate
        """

        fix_rate = self.fix_leg_object.fix_rate
        fix_leg_object_nominal = self.fix_leg_object.nominal
        fix_leg_object_schedule = self.fix_leg_object.schedule_fix

        def loss_func(fix_rate: float):
            leg_fix = fix_leg.FixLeg(
                nominal=fix_leg_object_nominal,
                fix_rate=fix_rate,
                schedule=fix_leg_object_schedule,
            )
            leg_fix.compute_cash_flow(pd.Timestamp(valuation_date))
            leg_fix.discount_cashflow(
                self.float_leg_object.yield_curve_object, valuation_date
            )
            return (leg_fix.NPV - self.float_leg_object.NPV) * (
                leg_fix.NPV - self.float_leg_object.NPV
            )

        res = minimize(
            loss_func,
            fix_rate,
            method="nelder-mead",
            options={"xatol": 1e-8, "disp": True},
        )
        self.faire_rate = float(res.x[0]) if hasattr(res.x, "__len__") else float(res.x)
        self.faire_rate_theory = (
            self.float_leg_object.NPV
            / (
                self.fix_leg_object.nominal
                * self.fix_leg_object.cashflow_leg_fix["day_count"]
                * self.fix_leg_object.cashflow_leg_fix["DF"]
            ).sum()
        )
        return self.faire_rate, self.faire_rate_theory

    def price(self, valuation_date: datetime, spreadHC: float, spreadGC: float):
        if self.relative_delta is None:
            relative_delta = relativedelta(days=0)
        else:
            relative_delta = self.relative_delta

        self.fix_leg_object.compute_cash_flow(valuation_date, spreadHC, spreadGC)
        self.fix_leg_object.discount_cashflow(
            self.yield_curve_fix, valuation_date, relative_delta
        )

        self.float_leg_object.compute_cash_flow(valuation_date)
        self.float_leg_object.discount_cashflow(
            self.yield_curve_float, valuation_date, relative_delta
        )

        cashflow = self.fix_leg_object.cashflow_leg_fix.merge(
            self.float_leg_object.cashflow_leg_float,
            on=["start_date", "end_date"],
            how="outer",  # Changed from "inner" to "outer" to capture all payment dates
            suffixes=("_fix", "_float"),
        )

        # Fill NaN values with 0 for periods that don't exist in one leg
        # This ensures we capture all payment periods from both schedules
        numeric_columns = cashflow.select_dtypes(include=[float, int]).columns
        cashflow[numeric_columns] = cashflow[numeric_columns].fillna(0)

        cashflow.rename(
            columns={
                "start_date": "start date",
                "end_date": "end date",
                "Period_fix": "fix Period years",
                "day_count_fix": "fix day_count",
                "cashflow_fix": "fix cashflow",
                "discount_cashflow_amounts_fix": "fix DCF",
                "DF_fix": "fix DF",
                "forward_zc_fix": "forward_ZC",
                "forward_simple_rate_fix": "forward_simple_rate",
                "Period_float": "float Period years",
                "day_count_float": "float day_count",
                "cashflow_float": "float cashflow",
                "discount_cashflow_amounts_float": "float DCF",
                "DF_float": "float DF",
                "forward_zc_float": "forward_ZC",
                "forward_simple_rate_float": "forward_simple_rate",
            },
            inplace=True,
        )
        self.cashflow = cashflow
