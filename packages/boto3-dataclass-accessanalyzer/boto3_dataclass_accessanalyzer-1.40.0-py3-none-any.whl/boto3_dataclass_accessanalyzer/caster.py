# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_accessanalyzer import type_defs as bs_td


class ACCESSANALYZERCaster:

    def apply_archive_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def check_access_not_granted(
        self,
        res: "bs_td.CheckAccessNotGrantedResponseTypeDef",
    ) -> "dc_td.CheckAccessNotGrantedResponse":
        return dc_td.CheckAccessNotGrantedResponse.make_one(res)

    def check_no_new_access(
        self,
        res: "bs_td.CheckNoNewAccessResponseTypeDef",
    ) -> "dc_td.CheckNoNewAccessResponse":
        return dc_td.CheckNoNewAccessResponse.make_one(res)

    def check_no_public_access(
        self,
        res: "bs_td.CheckNoPublicAccessResponseTypeDef",
    ) -> "dc_td.CheckNoPublicAccessResponse":
        return dc_td.CheckNoPublicAccessResponse.make_one(res)

    def create_access_preview(
        self,
        res: "bs_td.CreateAccessPreviewResponseTypeDef",
    ) -> "dc_td.CreateAccessPreviewResponse":
        return dc_td.CreateAccessPreviewResponse.make_one(res)

    def create_analyzer(
        self,
        res: "bs_td.CreateAnalyzerResponseTypeDef",
    ) -> "dc_td.CreateAnalyzerResponse":
        return dc_td.CreateAnalyzerResponse.make_one(res)

    def create_archive_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_analyzer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_archive_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def generate_finding_recommendation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_access_preview(
        self,
        res: "bs_td.GetAccessPreviewResponseTypeDef",
    ) -> "dc_td.GetAccessPreviewResponse":
        return dc_td.GetAccessPreviewResponse.make_one(res)

    def get_analyzed_resource(
        self,
        res: "bs_td.GetAnalyzedResourceResponseTypeDef",
    ) -> "dc_td.GetAnalyzedResourceResponse":
        return dc_td.GetAnalyzedResourceResponse.make_one(res)

    def get_analyzer(
        self,
        res: "bs_td.GetAnalyzerResponseTypeDef",
    ) -> "dc_td.GetAnalyzerResponse":
        return dc_td.GetAnalyzerResponse.make_one(res)

    def get_archive_rule(
        self,
        res: "bs_td.GetArchiveRuleResponseTypeDef",
    ) -> "dc_td.GetArchiveRuleResponse":
        return dc_td.GetArchiveRuleResponse.make_one(res)

    def get_finding(
        self,
        res: "bs_td.GetFindingResponseTypeDef",
    ) -> "dc_td.GetFindingResponse":
        return dc_td.GetFindingResponse.make_one(res)

    def get_finding_recommendation(
        self,
        res: "bs_td.GetFindingRecommendationResponseTypeDef",
    ) -> "dc_td.GetFindingRecommendationResponse":
        return dc_td.GetFindingRecommendationResponse.make_one(res)

    def get_finding_v2(
        self,
        res: "bs_td.GetFindingV2ResponseTypeDef",
    ) -> "dc_td.GetFindingV2Response":
        return dc_td.GetFindingV2Response.make_one(res)

    def get_findings_statistics(
        self,
        res: "bs_td.GetFindingsStatisticsResponseTypeDef",
    ) -> "dc_td.GetFindingsStatisticsResponse":
        return dc_td.GetFindingsStatisticsResponse.make_one(res)

    def get_generated_policy(
        self,
        res: "bs_td.GetGeneratedPolicyResponseTypeDef",
    ) -> "dc_td.GetGeneratedPolicyResponse":
        return dc_td.GetGeneratedPolicyResponse.make_one(res)

    def list_access_preview_findings(
        self,
        res: "bs_td.ListAccessPreviewFindingsResponseTypeDef",
    ) -> "dc_td.ListAccessPreviewFindingsResponse":
        return dc_td.ListAccessPreviewFindingsResponse.make_one(res)

    def list_access_previews(
        self,
        res: "bs_td.ListAccessPreviewsResponseTypeDef",
    ) -> "dc_td.ListAccessPreviewsResponse":
        return dc_td.ListAccessPreviewsResponse.make_one(res)

    def list_analyzed_resources(
        self,
        res: "bs_td.ListAnalyzedResourcesResponseTypeDef",
    ) -> "dc_td.ListAnalyzedResourcesResponse":
        return dc_td.ListAnalyzedResourcesResponse.make_one(res)

    def list_analyzers(
        self,
        res: "bs_td.ListAnalyzersResponseTypeDef",
    ) -> "dc_td.ListAnalyzersResponse":
        return dc_td.ListAnalyzersResponse.make_one(res)

    def list_archive_rules(
        self,
        res: "bs_td.ListArchiveRulesResponseTypeDef",
    ) -> "dc_td.ListArchiveRulesResponse":
        return dc_td.ListArchiveRulesResponse.make_one(res)

    def list_findings(
        self,
        res: "bs_td.ListFindingsResponseTypeDef",
    ) -> "dc_td.ListFindingsResponse":
        return dc_td.ListFindingsResponse.make_one(res)

    def list_findings_v2(
        self,
        res: "bs_td.ListFindingsV2ResponseTypeDef",
    ) -> "dc_td.ListFindingsV2Response":
        return dc_td.ListFindingsV2Response.make_one(res)

    def list_policy_generations(
        self,
        res: "bs_td.ListPolicyGenerationsResponseTypeDef",
    ) -> "dc_td.ListPolicyGenerationsResponse":
        return dc_td.ListPolicyGenerationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_policy_generation(
        self,
        res: "bs_td.StartPolicyGenerationResponseTypeDef",
    ) -> "dc_td.StartPolicyGenerationResponse":
        return dc_td.StartPolicyGenerationResponse.make_one(res)

    def start_resource_scan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_analyzer(
        self,
        res: "bs_td.UpdateAnalyzerResponseTypeDef",
    ) -> "dc_td.UpdateAnalyzerResponse":
        return dc_td.UpdateAnalyzerResponse.make_one(res)

    def update_archive_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_findings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def validate_policy(
        self,
        res: "bs_td.ValidatePolicyResponseTypeDef",
    ) -> "dc_td.ValidatePolicyResponse":
        return dc_td.ValidatePolicyResponse.make_one(res)


accessanalyzer_caster = ACCESSANALYZERCaster()
