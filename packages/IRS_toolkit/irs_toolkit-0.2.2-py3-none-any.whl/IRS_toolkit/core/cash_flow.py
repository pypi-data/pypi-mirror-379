import warnings

import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime

from IRS_toolkit.utils import core
from IRS_toolkit.core.curve import yield_curve
from IRS_toolkit.utils.constants import VALID_CONVENTIONS

warnings.filterwarnings("ignore")


class cash_flow:
    """
    cash flows handling
        Args:
            dates (Datframe): dates
            amounts (Dataframe): coupons
    """

    def __init__(
        self,
        dates: list[datetime],
        amounts: list[float],
        date_convention: VALID_CONVENTIONS,
        date_format="%Y-%m-%d",
    ):
        dates = [
            datetime.strptime(dt, date_format) if isinstance(dt, str) else dt
            for dt in dates
        ]
        self.cashflows = pd.DataFrame(
            {"cash_flow_date": dates, "cash_flow_amount": amounts}
        )
        self.date_convention = date_convention

    def npv(
        self,
        valuation_date: datetime,
        curve: yield_curve.YieldCurve,
        relative_delta=None,
        date_format="%Y-%m-%d",
    ):
        """
        Compute the Net present value with settlement detection.

        Properly handles settled vs unsettled cash flows:
        - Settled payments (payment_date <= valuation_date): DF = 1.0 (no discounting)
        - Unsettled payments (payment_date > valuation_date): Normal discounting

        Args:
            valuation_date (date): valuation date
            curve (curve): yield curve

        Returns:
            float: Net present value including settled and future cash flows
        """
        if relative_delta is None:
            relative_delta = relativedelta(days=0)

        # Initialize columns
        self.cashflows["discount_cashflow_amounts"] = 0.0
        self.cashflows["DF"] = 0.0
        self.cashflows["settlement_status"] = "future"  # Track settlement status

        valuation_date = (
            datetime.strptime(valuation_date, date_format)
            if isinstance(valuation_date, str)
            else valuation_date
        )

        for ind, dt in self.cashflows.iterrows():
            # Track settlement status for reporting purposes only
            if dt.cash_flow_date <= valuation_date:
                self.cashflows.loc[ind, "settlement_status"] = "settled"
                # For settled payments, set DF to 0 to exclude from NPV calculation
                # (they are already settled and not part of the valuation)
                self.cashflows.loc[ind, "DF"] = 0.0
            else:
                self.cashflows.loc[ind, "settlement_status"] = "future"

                # Calculate discount factors using forward rates for FUTURE payments only
                forward_rate = curve.forward_rates(
                    valuation_date, dt.cash_flow_date, relative_delta
                )
                time_period = core.day_count(
                    valuation_date, dt.cash_flow_date, self.date_convention
                )

                # Validate required inputs - fail fast with clear error messages
                if forward_rate is None:
                    raise ValueError(
                        f"Cannot calculate forward rate for payment date {dt.cash_flow_date}. "
                        f"Curve may be missing data points or payment date is outside curve range. "
                        f"Check yield curve data completeness."
                    )

                if time_period is None:
                    raise ValueError(
                        f"Cannot calculate time period from {valuation_date} to {dt.cash_flow_date} "
                        f"using convention {self.date_convention}. Check date convention and date format."
                    )

                # Calculate discount factor using forward rates for future payments
                self.cashflows.loc[ind, "DF"] = 1 / (1 + forward_rate) ** time_period

        # Calculate discounted amounts (settled payments excluded, future payments discounted)
        self.cashflows["discount_cashflow_amounts"] = (
            self.cashflows.DF * self.cashflows.cash_flow_amount
        )

        # NPV includes only future payments discounted using forward rates
        # (settled payments are excluded as they don't contribute to current valuation)
        self.NPV = self.cashflows["discount_cashflow_amounts"].sum()

        # Store settlement breakdown for reporting purposes only
        self.settled_npv = self.cashflows[
            self.cashflows.settlement_status == "settled"
        ][
            "discount_cashflow_amounts"
        ].sum()  # This will be 0 since settled payments have DF=0

        self.future_npv = self.cashflows[self.cashflows.settlement_status == "future"][
            "discount_cashflow_amounts"
        ].sum()

        return self.NPV

    # wighted present value for bonds
    def wpv(
        self,
        valuation_date: datetime,
        curve: yield_curve.YieldCurve,
        relative_delta=None,
        date_format="%Y-%m-%d",
    ):
        """
        Weighted Net present value

        Args:
            valuation_date (date): valuation date
            curve (curve): yield curve

        Returns:
            float: time weightide Net present value of future cash flows
        """
        if relative_delta is None:
            relative_delta = relativedelta(days=0)

        self.cashflows["wdiscount_cashflow_amounts"] = 0
        self.cashflows["DF"] = 0

        valuation_date = (
            datetime.strptime(valuation_date, date_format)
            if isinstance(valuation_date, str)
            else valuation_date
        )

        for ind, dt in self.cashflows.iterrows():
            if dt.cash_flow_date > valuation_date:
                self.cashflows.loc[ind, "DF"] = 1 / (
                    1
                    + curve.forward_rates(
                        valuation_date, dt.cash_flow_date, relative_delta
                    )
                ) ** (
                    core.day_count(
                        valuation_date, dt.cash_flow_date, self.date_convention
                    )
                )

                self.cashflows.loc[ind, "day_count"] = core.day_count(
                    valuation_date, dt.cash_flow_date, self.date_convention
                )

        self.cashflows["wdiscount_cashflow_amounts"] = (
            self.cashflows.DF
            * self.cashflows.cash_flow_amount
            * self.cashflows.day_count
        )

        self.WPV = (self.cashflows["wdiscount_cashflow_amounts"]).sum()
        return self.WPV
