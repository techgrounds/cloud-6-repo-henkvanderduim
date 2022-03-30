from tkinter import Widget
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_cloudwatch as cloudwatch


class DashboardStack(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.dashboard = cloudwatch.Dashboard(
            self,
            dashboard_name="MVPDashboard",
            end="end",
            period_override=cloudwatch.PeriodOverride.AUTO,
            start="start",
            widgets=[[Widget]],
        )
