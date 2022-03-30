import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_events import Schedule
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_events as event,
    aws_backup as backup,
    aws_ec2 as ec2,
    aws_kms as kms,
    RemovalPolicy,
    Duration,
    Tags,
)


class BackupStack(cdk.NestedStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        management_server: ec2.Instance,
        asg: autoscaling.AutoScalingGroup,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        tags_environment = environments.get("tags")
        mngt_tag_key = tags_environment.get("mngt_tag_key")
        mngt_tag_value = tags_environment.get("mngt_tag_value")
        asg_tag_key = tags_environment.get("asg_tag_key")
        asg_tag_value = tags_environment.get("asg_tag_value")
        bus_environment = environments.get("bus")
        mngt_vault_key = bus_environment.get("mngt_vault_key")
        mngt_vault_name = bus_environment.get("mngt_vault_name")
        mngt_backup_vault_name = bus_environment.get("mngt_backup_vault_name")
        mngt_backup_plan = bus_environment.get("mngt_backup_plan")
        mngt_backup_plan_name = bus_environment.get("mngt_backup_plan_name")
        mngt_rule_name = bus_environment.get("mngt_rule_name")
        mngt_complete = bus_environment.get("mngt_complete")
        mngt_start = bus_environment.get("mngt_start")
        mngt_minute = bus_environment.get("mngt_minute")
        mngt_hour = bus_environment.get("mngt_hour")
        mngt_month = bus_environment.get("mngt_month")
        mngt_weekday = bus_environment.get("mngt_weekday")
        mngt_duration = bus_environment.get("mngt_duration")
        asg_vault_key = bus_environment.get("asg_vault_key")
        asg_vault_name = bus_environment.get("asg_vault_name")
        asg_backup_vault_name = bus_environment.get("asg_backup_vault_name")
        asg_backup_plan = bus_environment.get("asg_backup_plan")
        asg_backup_plan_name = bus_environment.get("asg_backup_plan_name")
        asg_backup_resource = bus_environment.get("asg_backup_resource")
        asg_rule_name = bus_environment.get("asg_rule_name")
        asg_complete = bus_environment.get("asg_complete")
        asg_start = bus_environment.get("asg_start")
        asg_minute = bus_environment.get("asg_minute")
        asg_hour = bus_environment.get("asg_hour")
        asg_month = bus_environment.get("asg_month")
        asg_weekday = bus_environment.get("asg_weekday")
        asg_duration = bus_environment.get("asg_duration")

        #################### Create Tags ####################

        Tags.of(management_server).add(mngt_tag_key, mngt_tag_value)
        Tags.of(asg).add(asg_tag_key, asg_tag_value)

        ##################### Create Backup Routines #############################

        ### Backup Management Server
        ### Create Backup Vault
        mngtvaultkey = kms.Key(
            self, mngt_vault_key, removal_policy=RemovalPolicy.DESTROY
        )
        mngtvault = backup.BackupVault(
            self,
            mngt_vault_name,
            backup_vault_name=mngt_backup_vault_name,
            encryption_key=mngtvaultkey,
            removal_policy=RemovalPolicy.DESTROY,
        )

        ### Create Backup Plan
        mngtplan = backup.BackupPlan(
            self, mngt_backup_plan, backup_plan_name=mngt_backup_plan_name
        )

        ### Add Backup Resources through Tags
        mngtplan.add_selection(
            "Selection",
            resources=[backup.BackupResource.from_tag(mngt_tag_key, mngt_tag_value)],
        )

        ### Create Backup Rule - Each day at 4:30 hrs and keep for 7 days
        mngtplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=mngtvault,
                rule_name=mngt_rule_name,
                completion_window=Duration.hours(mngt_complete),
                start_window=Duration.hours(mngt_start),
                schedule_expression=Schedule.cron(
                    minute=mngt_minute,
                    hour=mngt_hour,
                    month=mngt_month,
                    week_day=mngt_weekday,
                ),
                delete_after=Duration.days(mngt_duration),
            )
        )

        ### Backup Webserver
        ### Create Backup Vault
        asgkey = kms.Key(self, asg_vault_key, removal_policy=RemovalPolicy.DESTROY)
        asgvault = backup.BackupVault(
            self,
            asg_vault_name,
            backup_vault_name=asg_backup_vault_name,
            encryption_key=asgkey,
            removal_policy=RemovalPolicy.DESTROY,
        )

        ### Create Backup Plan
        asgplan = backup.BackupPlan(
            self, asg_backup_plan, backup_plan_name=asg_backup_plan_name
        )

        ### Add Backup Resources through Tags
        asgplan.add_selection(
            asg_backup_resource,
            resources=[backup.BackupResource.from_tag(asg_tag_key, asg_tag_value)],
        )

        ### Create Backup Rule - Once a week and save 1
        asgplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=asgvault,
                rule_name=asg_rule_name,
                completion_window=Duration.hours(asg_complete),
                start_window=Duration.hours(asg_start),
                schedule_expression=Schedule.cron(
                    minute=asg_minute,
                    hour=asg_hour,
                    month=asg_month,
                    week_day=asg_weekday,
                ),
                delete_after=Duration.days(asg_duration),
            )
        )
