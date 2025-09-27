# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_autoscaling import type_defs as bs_td


class AUTOSCALINGCaster:

    def attach_instances(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_delete_scheduled_action(
        self,
        res: "bs_td.BatchDeleteScheduledActionAnswerTypeDef",
    ) -> "dc_td.BatchDeleteScheduledActionAnswer":
        return dc_td.BatchDeleteScheduledActionAnswer.make_one(res)

    def batch_put_scheduled_update_group_action(
        self,
        res: "bs_td.BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    ) -> "dc_td.BatchPutScheduledUpdateGroupActionAnswer":
        return dc_td.BatchPutScheduledUpdateGroupActionAnswer.make_one(res)

    def cancel_instance_refresh(
        self,
        res: "bs_td.CancelInstanceRefreshAnswerTypeDef",
    ) -> "dc_td.CancelInstanceRefreshAnswer":
        return dc_td.CancelInstanceRefreshAnswer.make_one(res)

    def create_auto_scaling_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_launch_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_or_update_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_auto_scaling_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_launch_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_notification_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_scheduled_action(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account_limits(
        self,
        res: "bs_td.DescribeAccountLimitsAnswerTypeDef",
    ) -> "dc_td.DescribeAccountLimitsAnswer":
        return dc_td.DescribeAccountLimitsAnswer.make_one(res)

    def describe_adjustment_types(
        self,
        res: "bs_td.DescribeAdjustmentTypesAnswerTypeDef",
    ) -> "dc_td.DescribeAdjustmentTypesAnswer":
        return dc_td.DescribeAdjustmentTypesAnswer.make_one(res)

    def describe_auto_scaling_groups(
        self,
        res: "bs_td.AutoScalingGroupsTypeTypeDef",
    ) -> "dc_td.AutoScalingGroupsType":
        return dc_td.AutoScalingGroupsType.make_one(res)

    def describe_auto_scaling_instances(
        self,
        res: "bs_td.AutoScalingInstancesTypeTypeDef",
    ) -> "dc_td.AutoScalingInstancesType":
        return dc_td.AutoScalingInstancesType.make_one(res)

    def describe_auto_scaling_notification_types(
        self,
        res: "bs_td.DescribeAutoScalingNotificationTypesAnswerTypeDef",
    ) -> "dc_td.DescribeAutoScalingNotificationTypesAnswer":
        return dc_td.DescribeAutoScalingNotificationTypesAnswer.make_one(res)

    def describe_instance_refreshes(
        self,
        res: "bs_td.DescribeInstanceRefreshesAnswerTypeDef",
    ) -> "dc_td.DescribeInstanceRefreshesAnswer":
        return dc_td.DescribeInstanceRefreshesAnswer.make_one(res)

    def describe_launch_configurations(
        self,
        res: "bs_td.LaunchConfigurationsTypeTypeDef",
    ) -> "dc_td.LaunchConfigurationsType":
        return dc_td.LaunchConfigurationsType.make_one(res)

    def describe_lifecycle_hook_types(
        self,
        res: "bs_td.DescribeLifecycleHookTypesAnswerTypeDef",
    ) -> "dc_td.DescribeLifecycleHookTypesAnswer":
        return dc_td.DescribeLifecycleHookTypesAnswer.make_one(res)

    def describe_lifecycle_hooks(
        self,
        res: "bs_td.DescribeLifecycleHooksAnswerTypeDef",
    ) -> "dc_td.DescribeLifecycleHooksAnswer":
        return dc_td.DescribeLifecycleHooksAnswer.make_one(res)

    def describe_load_balancer_target_groups(
        self,
        res: "bs_td.DescribeLoadBalancerTargetGroupsResponseTypeDef",
    ) -> "dc_td.DescribeLoadBalancerTargetGroupsResponse":
        return dc_td.DescribeLoadBalancerTargetGroupsResponse.make_one(res)

    def describe_load_balancers(
        self,
        res: "bs_td.DescribeLoadBalancersResponseTypeDef",
    ) -> "dc_td.DescribeLoadBalancersResponse":
        return dc_td.DescribeLoadBalancersResponse.make_one(res)

    def describe_metric_collection_types(
        self,
        res: "bs_td.DescribeMetricCollectionTypesAnswerTypeDef",
    ) -> "dc_td.DescribeMetricCollectionTypesAnswer":
        return dc_td.DescribeMetricCollectionTypesAnswer.make_one(res)

    def describe_notification_configurations(
        self,
        res: "bs_td.DescribeNotificationConfigurationsAnswerTypeDef",
    ) -> "dc_td.DescribeNotificationConfigurationsAnswer":
        return dc_td.DescribeNotificationConfigurationsAnswer.make_one(res)

    def describe_policies(
        self,
        res: "bs_td.PoliciesTypeTypeDef",
    ) -> "dc_td.PoliciesType":
        return dc_td.PoliciesType.make_one(res)

    def describe_scaling_activities(
        self,
        res: "bs_td.ActivitiesTypeTypeDef",
    ) -> "dc_td.ActivitiesType":
        return dc_td.ActivitiesType.make_one(res)

    def describe_scaling_process_types(
        self,
        res: "bs_td.ProcessesTypeTypeDef",
    ) -> "dc_td.ProcessesType":
        return dc_td.ProcessesType.make_one(res)

    def describe_scheduled_actions(
        self,
        res: "bs_td.ScheduledActionsTypeTypeDef",
    ) -> "dc_td.ScheduledActionsType":
        return dc_td.ScheduledActionsType.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.TagsTypeTypeDef",
    ) -> "dc_td.TagsType":
        return dc_td.TagsType.make_one(res)

    def describe_termination_policy_types(
        self,
        res: "bs_td.DescribeTerminationPolicyTypesAnswerTypeDef",
    ) -> "dc_td.DescribeTerminationPolicyTypesAnswer":
        return dc_td.DescribeTerminationPolicyTypesAnswer.make_one(res)

    def describe_traffic_sources(
        self,
        res: "bs_td.DescribeTrafficSourcesResponseTypeDef",
    ) -> "dc_td.DescribeTrafficSourcesResponse":
        return dc_td.DescribeTrafficSourcesResponse.make_one(res)

    def describe_warm_pool(
        self,
        res: "bs_td.DescribeWarmPoolAnswerTypeDef",
    ) -> "dc_td.DescribeWarmPoolAnswer":
        return dc_td.DescribeWarmPoolAnswer.make_one(res)

    def detach_instances(
        self,
        res: "bs_td.DetachInstancesAnswerTypeDef",
    ) -> "dc_td.DetachInstancesAnswer":
        return dc_td.DetachInstancesAnswer.make_one(res)

    def disable_metrics_collection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_metrics_collection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enter_standby(
        self,
        res: "bs_td.EnterStandbyAnswerTypeDef",
    ) -> "dc_td.EnterStandbyAnswer":
        return dc_td.EnterStandbyAnswer.make_one(res)

    def execute_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def exit_standby(
        self,
        res: "bs_td.ExitStandbyAnswerTypeDef",
    ) -> "dc_td.ExitStandbyAnswer":
        return dc_td.ExitStandbyAnswer.make_one(res)

    def get_predictive_scaling_forecast(
        self,
        res: "bs_td.GetPredictiveScalingForecastAnswerTypeDef",
    ) -> "dc_td.GetPredictiveScalingForecastAnswer":
        return dc_td.GetPredictiveScalingForecastAnswer.make_one(res)

    def put_notification_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_scaling_policy(
        self,
        res: "bs_td.PolicyARNTypeTypeDef",
    ) -> "dc_td.PolicyARNType":
        return dc_td.PolicyARNType.make_one(res)

    def put_scheduled_update_group_action(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def resume_processes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def rollback_instance_refresh(
        self,
        res: "bs_td.RollbackInstanceRefreshAnswerTypeDef",
    ) -> "dc_td.RollbackInstanceRefreshAnswer":
        return dc_td.RollbackInstanceRefreshAnswer.make_one(res)

    def set_desired_capacity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_instance_health(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_instance_refresh(
        self,
        res: "bs_td.StartInstanceRefreshAnswerTypeDef",
    ) -> "dc_td.StartInstanceRefreshAnswer":
        return dc_td.StartInstanceRefreshAnswer.make_one(res)

    def suspend_processes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def terminate_instance_in_auto_scaling_group(
        self,
        res: "bs_td.ActivityTypeTypeDef",
    ) -> "dc_td.ActivityType":
        return dc_td.ActivityType.make_one(res)

    def update_auto_scaling_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


autoscaling_caster = AUTOSCALINGCaster()
