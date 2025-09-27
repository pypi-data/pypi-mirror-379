# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_compute_optimizer import type_defs as bs_td


class COMPUTE_OPTIMIZERCaster:

    def describe_recommendation_export_jobs(
        self,
        res: "bs_td.DescribeRecommendationExportJobsResponseTypeDef",
    ) -> "dc_td.DescribeRecommendationExportJobsResponse":
        return dc_td.DescribeRecommendationExportJobsResponse.make_one(res)

    def export_auto_scaling_group_recommendations(
        self,
        res: "bs_td.ExportAutoScalingGroupRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportAutoScalingGroupRecommendationsResponse":
        return dc_td.ExportAutoScalingGroupRecommendationsResponse.make_one(res)

    def export_ebs_volume_recommendations(
        self,
        res: "bs_td.ExportEBSVolumeRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportEBSVolumeRecommendationsResponse":
        return dc_td.ExportEBSVolumeRecommendationsResponse.make_one(res)

    def export_ec2_instance_recommendations(
        self,
        res: "bs_td.ExportEC2InstanceRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportEC2InstanceRecommendationsResponse":
        return dc_td.ExportEC2InstanceRecommendationsResponse.make_one(res)

    def export_ecs_service_recommendations(
        self,
        res: "bs_td.ExportECSServiceRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportECSServiceRecommendationsResponse":
        return dc_td.ExportECSServiceRecommendationsResponse.make_one(res)

    def export_idle_recommendations(
        self,
        res: "bs_td.ExportIdleRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportIdleRecommendationsResponse":
        return dc_td.ExportIdleRecommendationsResponse.make_one(res)

    def export_lambda_function_recommendations(
        self,
        res: "bs_td.ExportLambdaFunctionRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportLambdaFunctionRecommendationsResponse":
        return dc_td.ExportLambdaFunctionRecommendationsResponse.make_one(res)

    def export_license_recommendations(
        self,
        res: "bs_td.ExportLicenseRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportLicenseRecommendationsResponse":
        return dc_td.ExportLicenseRecommendationsResponse.make_one(res)

    def export_rds_database_recommendations(
        self,
        res: "bs_td.ExportRDSDatabaseRecommendationsResponseTypeDef",
    ) -> "dc_td.ExportRDSDatabaseRecommendationsResponse":
        return dc_td.ExportRDSDatabaseRecommendationsResponse.make_one(res)

    def get_auto_scaling_group_recommendations(
        self,
        res: "bs_td.GetAutoScalingGroupRecommendationsResponseTypeDef",
    ) -> "dc_td.GetAutoScalingGroupRecommendationsResponse":
        return dc_td.GetAutoScalingGroupRecommendationsResponse.make_one(res)

    def get_ebs_volume_recommendations(
        self,
        res: "bs_td.GetEBSVolumeRecommendationsResponseTypeDef",
    ) -> "dc_td.GetEBSVolumeRecommendationsResponse":
        return dc_td.GetEBSVolumeRecommendationsResponse.make_one(res)

    def get_ec2_instance_recommendations(
        self,
        res: "bs_td.GetEC2InstanceRecommendationsResponseTypeDef",
    ) -> "dc_td.GetEC2InstanceRecommendationsResponse":
        return dc_td.GetEC2InstanceRecommendationsResponse.make_one(res)

    def get_ec2_recommendation_projected_metrics(
        self,
        res: "bs_td.GetEC2RecommendationProjectedMetricsResponseTypeDef",
    ) -> "dc_td.GetEC2RecommendationProjectedMetricsResponse":
        return dc_td.GetEC2RecommendationProjectedMetricsResponse.make_one(res)

    def get_ecs_service_recommendation_projected_metrics(
        self,
        res: "bs_td.GetECSServiceRecommendationProjectedMetricsResponseTypeDef",
    ) -> "dc_td.GetECSServiceRecommendationProjectedMetricsResponse":
        return dc_td.GetECSServiceRecommendationProjectedMetricsResponse.make_one(res)

    def get_ecs_service_recommendations(
        self,
        res: "bs_td.GetECSServiceRecommendationsResponseTypeDef",
    ) -> "dc_td.GetECSServiceRecommendationsResponse":
        return dc_td.GetECSServiceRecommendationsResponse.make_one(res)

    def get_effective_recommendation_preferences(
        self,
        res: "bs_td.GetEffectiveRecommendationPreferencesResponseTypeDef",
    ) -> "dc_td.GetEffectiveRecommendationPreferencesResponse":
        return dc_td.GetEffectiveRecommendationPreferencesResponse.make_one(res)

    def get_enrollment_status(
        self,
        res: "bs_td.GetEnrollmentStatusResponseTypeDef",
    ) -> "dc_td.GetEnrollmentStatusResponse":
        return dc_td.GetEnrollmentStatusResponse.make_one(res)

    def get_enrollment_statuses_for_organization(
        self,
        res: "bs_td.GetEnrollmentStatusesForOrganizationResponseTypeDef",
    ) -> "dc_td.GetEnrollmentStatusesForOrganizationResponse":
        return dc_td.GetEnrollmentStatusesForOrganizationResponse.make_one(res)

    def get_idle_recommendations(
        self,
        res: "bs_td.GetIdleRecommendationsResponseTypeDef",
    ) -> "dc_td.GetIdleRecommendationsResponse":
        return dc_td.GetIdleRecommendationsResponse.make_one(res)

    def get_lambda_function_recommendations(
        self,
        res: "bs_td.GetLambdaFunctionRecommendationsResponseTypeDef",
    ) -> "dc_td.GetLambdaFunctionRecommendationsResponse":
        return dc_td.GetLambdaFunctionRecommendationsResponse.make_one(res)

    def get_license_recommendations(
        self,
        res: "bs_td.GetLicenseRecommendationsResponseTypeDef",
    ) -> "dc_td.GetLicenseRecommendationsResponse":
        return dc_td.GetLicenseRecommendationsResponse.make_one(res)

    def get_rds_database_recommendation_projected_metrics(
        self,
        res: "bs_td.GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef",
    ) -> "dc_td.GetRDSDatabaseRecommendationProjectedMetricsResponse":
        return dc_td.GetRDSDatabaseRecommendationProjectedMetricsResponse.make_one(res)

    def get_rds_database_recommendations(
        self,
        res: "bs_td.GetRDSDatabaseRecommendationsResponseTypeDef",
    ) -> "dc_td.GetRDSDatabaseRecommendationsResponse":
        return dc_td.GetRDSDatabaseRecommendationsResponse.make_one(res)

    def get_recommendation_preferences(
        self,
        res: "bs_td.GetRecommendationPreferencesResponseTypeDef",
    ) -> "dc_td.GetRecommendationPreferencesResponse":
        return dc_td.GetRecommendationPreferencesResponse.make_one(res)

    def get_recommendation_summaries(
        self,
        res: "bs_td.GetRecommendationSummariesResponseTypeDef",
    ) -> "dc_td.GetRecommendationSummariesResponse":
        return dc_td.GetRecommendationSummariesResponse.make_one(res)

    def update_enrollment_status(
        self,
        res: "bs_td.UpdateEnrollmentStatusResponseTypeDef",
    ) -> "dc_td.UpdateEnrollmentStatusResponse":
        return dc_td.UpdateEnrollmentStatusResponse.make_one(res)


compute_optimizer_caster = COMPUTE_OPTIMIZERCaster()
