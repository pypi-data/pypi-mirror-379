# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ds import type_defs as bs_td


class DSCaster:

    def accept_shared_directory(
        self,
        res: "bs_td.AcceptSharedDirectoryResultTypeDef",
    ) -> "dc_td.AcceptSharedDirectoryResult":
        return dc_td.AcceptSharedDirectoryResult.make_one(res)

    def connect_directory(
        self,
        res: "bs_td.ConnectDirectoryResultTypeDef",
    ) -> "dc_td.ConnectDirectoryResult":
        return dc_td.ConnectDirectoryResult.make_one(res)

    def create_alias(
        self,
        res: "bs_td.CreateAliasResultTypeDef",
    ) -> "dc_td.CreateAliasResult":
        return dc_td.CreateAliasResult.make_one(res)

    def create_computer(
        self,
        res: "bs_td.CreateComputerResultTypeDef",
    ) -> "dc_td.CreateComputerResult":
        return dc_td.CreateComputerResult.make_one(res)

    def create_directory(
        self,
        res: "bs_td.CreateDirectoryResultTypeDef",
    ) -> "dc_td.CreateDirectoryResult":
        return dc_td.CreateDirectoryResult.make_one(res)

    def create_hybrid_ad(
        self,
        res: "bs_td.CreateHybridADResultTypeDef",
    ) -> "dc_td.CreateHybridADResult":
        return dc_td.CreateHybridADResult.make_one(res)

    def create_microsoft_ad(
        self,
        res: "bs_td.CreateMicrosoftADResultTypeDef",
    ) -> "dc_td.CreateMicrosoftADResult":
        return dc_td.CreateMicrosoftADResult.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.CreateSnapshotResultTypeDef",
    ) -> "dc_td.CreateSnapshotResult":
        return dc_td.CreateSnapshotResult.make_one(res)

    def create_trust(
        self,
        res: "bs_td.CreateTrustResultTypeDef",
    ) -> "dc_td.CreateTrustResult":
        return dc_td.CreateTrustResult.make_one(res)

    def delete_ad_assessment(
        self,
        res: "bs_td.DeleteADAssessmentResultTypeDef",
    ) -> "dc_td.DeleteADAssessmentResult":
        return dc_td.DeleteADAssessmentResult.make_one(res)

    def delete_directory(
        self,
        res: "bs_td.DeleteDirectoryResultTypeDef",
    ) -> "dc_td.DeleteDirectoryResult":
        return dc_td.DeleteDirectoryResult.make_one(res)

    def delete_snapshot(
        self,
        res: "bs_td.DeleteSnapshotResultTypeDef",
    ) -> "dc_td.DeleteSnapshotResult":
        return dc_td.DeleteSnapshotResult.make_one(res)

    def delete_trust(
        self,
        res: "bs_td.DeleteTrustResultTypeDef",
    ) -> "dc_td.DeleteTrustResult":
        return dc_td.DeleteTrustResult.make_one(res)

    def describe_ad_assessment(
        self,
        res: "bs_td.DescribeADAssessmentResultTypeDef",
    ) -> "dc_td.DescribeADAssessmentResult":
        return dc_td.DescribeADAssessmentResult.make_one(res)

    def describe_ca_enrollment_policy(
        self,
        res: "bs_td.DescribeCAEnrollmentPolicyResultTypeDef",
    ) -> "dc_td.DescribeCAEnrollmentPolicyResult":
        return dc_td.DescribeCAEnrollmentPolicyResult.make_one(res)

    def describe_certificate(
        self,
        res: "bs_td.DescribeCertificateResultTypeDef",
    ) -> "dc_td.DescribeCertificateResult":
        return dc_td.DescribeCertificateResult.make_one(res)

    def describe_client_authentication_settings(
        self,
        res: "bs_td.DescribeClientAuthenticationSettingsResultTypeDef",
    ) -> "dc_td.DescribeClientAuthenticationSettingsResult":
        return dc_td.DescribeClientAuthenticationSettingsResult.make_one(res)

    def describe_conditional_forwarders(
        self,
        res: "bs_td.DescribeConditionalForwardersResultTypeDef",
    ) -> "dc_td.DescribeConditionalForwardersResult":
        return dc_td.DescribeConditionalForwardersResult.make_one(res)

    def describe_directories(
        self,
        res: "bs_td.DescribeDirectoriesResultTypeDef",
    ) -> "dc_td.DescribeDirectoriesResult":
        return dc_td.DescribeDirectoriesResult.make_one(res)

    def describe_directory_data_access(
        self,
        res: "bs_td.DescribeDirectoryDataAccessResultTypeDef",
    ) -> "dc_td.DescribeDirectoryDataAccessResult":
        return dc_td.DescribeDirectoryDataAccessResult.make_one(res)

    def describe_domain_controllers(
        self,
        res: "bs_td.DescribeDomainControllersResultTypeDef",
    ) -> "dc_td.DescribeDomainControllersResult":
        return dc_td.DescribeDomainControllersResult.make_one(res)

    def describe_event_topics(
        self,
        res: "bs_td.DescribeEventTopicsResultTypeDef",
    ) -> "dc_td.DescribeEventTopicsResult":
        return dc_td.DescribeEventTopicsResult.make_one(res)

    def describe_hybrid_ad_update(
        self,
        res: "bs_td.DescribeHybridADUpdateResultTypeDef",
    ) -> "dc_td.DescribeHybridADUpdateResult":
        return dc_td.DescribeHybridADUpdateResult.make_one(res)

    def describe_ldaps_settings(
        self,
        res: "bs_td.DescribeLDAPSSettingsResultTypeDef",
    ) -> "dc_td.DescribeLDAPSSettingsResult":
        return dc_td.DescribeLDAPSSettingsResult.make_one(res)

    def describe_regions(
        self,
        res: "bs_td.DescribeRegionsResultTypeDef",
    ) -> "dc_td.DescribeRegionsResult":
        return dc_td.DescribeRegionsResult.make_one(res)

    def describe_settings(
        self,
        res: "bs_td.DescribeSettingsResultTypeDef",
    ) -> "dc_td.DescribeSettingsResult":
        return dc_td.DescribeSettingsResult.make_one(res)

    def describe_shared_directories(
        self,
        res: "bs_td.DescribeSharedDirectoriesResultTypeDef",
    ) -> "dc_td.DescribeSharedDirectoriesResult":
        return dc_td.DescribeSharedDirectoriesResult.make_one(res)

    def describe_snapshots(
        self,
        res: "bs_td.DescribeSnapshotsResultTypeDef",
    ) -> "dc_td.DescribeSnapshotsResult":
        return dc_td.DescribeSnapshotsResult.make_one(res)

    def describe_trusts(
        self,
        res: "bs_td.DescribeTrustsResultTypeDef",
    ) -> "dc_td.DescribeTrustsResult":
        return dc_td.DescribeTrustsResult.make_one(res)

    def describe_update_directory(
        self,
        res: "bs_td.DescribeUpdateDirectoryResultTypeDef",
    ) -> "dc_td.DescribeUpdateDirectoryResult":
        return dc_td.DescribeUpdateDirectoryResult.make_one(res)

    def get_directory_limits(
        self,
        res: "bs_td.GetDirectoryLimitsResultTypeDef",
    ) -> "dc_td.GetDirectoryLimitsResult":
        return dc_td.GetDirectoryLimitsResult.make_one(res)

    def get_snapshot_limits(
        self,
        res: "bs_td.GetSnapshotLimitsResultTypeDef",
    ) -> "dc_td.GetSnapshotLimitsResult":
        return dc_td.GetSnapshotLimitsResult.make_one(res)

    def list_ad_assessments(
        self,
        res: "bs_td.ListADAssessmentsResultTypeDef",
    ) -> "dc_td.ListADAssessmentsResult":
        return dc_td.ListADAssessmentsResult.make_one(res)

    def list_certificates(
        self,
        res: "bs_td.ListCertificatesResultTypeDef",
    ) -> "dc_td.ListCertificatesResult":
        return dc_td.ListCertificatesResult.make_one(res)

    def list_ip_routes(
        self,
        res: "bs_td.ListIpRoutesResultTypeDef",
    ) -> "dc_td.ListIpRoutesResult":
        return dc_td.ListIpRoutesResult.make_one(res)

    def list_log_subscriptions(
        self,
        res: "bs_td.ListLogSubscriptionsResultTypeDef",
    ) -> "dc_td.ListLogSubscriptionsResult":
        return dc_td.ListLogSubscriptionsResult.make_one(res)

    def list_schema_extensions(
        self,
        res: "bs_td.ListSchemaExtensionsResultTypeDef",
    ) -> "dc_td.ListSchemaExtensionsResult":
        return dc_td.ListSchemaExtensionsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def register_certificate(
        self,
        res: "bs_td.RegisterCertificateResultTypeDef",
    ) -> "dc_td.RegisterCertificateResult":
        return dc_td.RegisterCertificateResult.make_one(res)

    def reject_shared_directory(
        self,
        res: "bs_td.RejectSharedDirectoryResultTypeDef",
    ) -> "dc_td.RejectSharedDirectoryResult":
        return dc_td.RejectSharedDirectoryResult.make_one(res)

    def share_directory(
        self,
        res: "bs_td.ShareDirectoryResultTypeDef",
    ) -> "dc_td.ShareDirectoryResult":
        return dc_td.ShareDirectoryResult.make_one(res)

    def start_ad_assessment(
        self,
        res: "bs_td.StartADAssessmentResultTypeDef",
    ) -> "dc_td.StartADAssessmentResult":
        return dc_td.StartADAssessmentResult.make_one(res)

    def start_schema_extension(
        self,
        res: "bs_td.StartSchemaExtensionResultTypeDef",
    ) -> "dc_td.StartSchemaExtensionResult":
        return dc_td.StartSchemaExtensionResult.make_one(res)

    def unshare_directory(
        self,
        res: "bs_td.UnshareDirectoryResultTypeDef",
    ) -> "dc_td.UnshareDirectoryResult":
        return dc_td.UnshareDirectoryResult.make_one(res)

    def update_hybrid_ad(
        self,
        res: "bs_td.UpdateHybridADResultTypeDef",
    ) -> "dc_td.UpdateHybridADResult":
        return dc_td.UpdateHybridADResult.make_one(res)

    def update_settings(
        self,
        res: "bs_td.UpdateSettingsResultTypeDef",
    ) -> "dc_td.UpdateSettingsResult":
        return dc_td.UpdateSettingsResult.make_one(res)

    def update_trust(
        self,
        res: "bs_td.UpdateTrustResultTypeDef",
    ) -> "dc_td.UpdateTrustResult":
        return dc_td.UpdateTrustResult.make_one(res)

    def verify_trust(
        self,
        res: "bs_td.VerifyTrustResultTypeDef",
    ) -> "dc_td.VerifyTrustResult":
        return dc_td.VerifyTrustResult.make_one(res)


ds_caster = DSCaster()
