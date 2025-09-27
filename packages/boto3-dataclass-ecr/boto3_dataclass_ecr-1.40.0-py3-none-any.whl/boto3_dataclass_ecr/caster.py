# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ecr import type_defs as bs_td


class ECRCaster:

    def batch_check_layer_availability(
        self,
        res: "bs_td.BatchCheckLayerAvailabilityResponseTypeDef",
    ) -> "dc_td.BatchCheckLayerAvailabilityResponse":
        return dc_td.BatchCheckLayerAvailabilityResponse.make_one(res)

    def batch_delete_image(
        self,
        res: "bs_td.BatchDeleteImageResponseTypeDef",
    ) -> "dc_td.BatchDeleteImageResponse":
        return dc_td.BatchDeleteImageResponse.make_one(res)

    def batch_get_image(
        self,
        res: "bs_td.BatchGetImageResponseTypeDef",
    ) -> "dc_td.BatchGetImageResponse":
        return dc_td.BatchGetImageResponse.make_one(res)

    def batch_get_repository_scanning_configuration(
        self,
        res: "bs_td.BatchGetRepositoryScanningConfigurationResponseTypeDef",
    ) -> "dc_td.BatchGetRepositoryScanningConfigurationResponse":
        return dc_td.BatchGetRepositoryScanningConfigurationResponse.make_one(res)

    def complete_layer_upload(
        self,
        res: "bs_td.CompleteLayerUploadResponseTypeDef",
    ) -> "dc_td.CompleteLayerUploadResponse":
        return dc_td.CompleteLayerUploadResponse.make_one(res)

    def create_pull_through_cache_rule(
        self,
        res: "bs_td.CreatePullThroughCacheRuleResponseTypeDef",
    ) -> "dc_td.CreatePullThroughCacheRuleResponse":
        return dc_td.CreatePullThroughCacheRuleResponse.make_one(res)

    def create_repository(
        self,
        res: "bs_td.CreateRepositoryResponseTypeDef",
    ) -> "dc_td.CreateRepositoryResponse":
        return dc_td.CreateRepositoryResponse.make_one(res)

    def create_repository_creation_template(
        self,
        res: "bs_td.CreateRepositoryCreationTemplateResponseTypeDef",
    ) -> "dc_td.CreateRepositoryCreationTemplateResponse":
        return dc_td.CreateRepositoryCreationTemplateResponse.make_one(res)

    def delete_lifecycle_policy(
        self,
        res: "bs_td.DeleteLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.DeleteLifecyclePolicyResponse":
        return dc_td.DeleteLifecyclePolicyResponse.make_one(res)

    def delete_pull_through_cache_rule(
        self,
        res: "bs_td.DeletePullThroughCacheRuleResponseTypeDef",
    ) -> "dc_td.DeletePullThroughCacheRuleResponse":
        return dc_td.DeletePullThroughCacheRuleResponse.make_one(res)

    def delete_registry_policy(
        self,
        res: "bs_td.DeleteRegistryPolicyResponseTypeDef",
    ) -> "dc_td.DeleteRegistryPolicyResponse":
        return dc_td.DeleteRegistryPolicyResponse.make_one(res)

    def delete_repository(
        self,
        res: "bs_td.DeleteRepositoryResponseTypeDef",
    ) -> "dc_td.DeleteRepositoryResponse":
        return dc_td.DeleteRepositoryResponse.make_one(res)

    def delete_repository_creation_template(
        self,
        res: "bs_td.DeleteRepositoryCreationTemplateResponseTypeDef",
    ) -> "dc_td.DeleteRepositoryCreationTemplateResponse":
        return dc_td.DeleteRepositoryCreationTemplateResponse.make_one(res)

    def delete_repository_policy(
        self,
        res: "bs_td.DeleteRepositoryPolicyResponseTypeDef",
    ) -> "dc_td.DeleteRepositoryPolicyResponse":
        return dc_td.DeleteRepositoryPolicyResponse.make_one(res)

    def describe_image_replication_status(
        self,
        res: "bs_td.DescribeImageReplicationStatusResponseTypeDef",
    ) -> "dc_td.DescribeImageReplicationStatusResponse":
        return dc_td.DescribeImageReplicationStatusResponse.make_one(res)

    def describe_image_scan_findings(
        self,
        res: "bs_td.DescribeImageScanFindingsResponseTypeDef",
    ) -> "dc_td.DescribeImageScanFindingsResponse":
        return dc_td.DescribeImageScanFindingsResponse.make_one(res)

    def describe_images(
        self,
        res: "bs_td.DescribeImagesResponseTypeDef",
    ) -> "dc_td.DescribeImagesResponse":
        return dc_td.DescribeImagesResponse.make_one(res)

    def describe_pull_through_cache_rules(
        self,
        res: "bs_td.DescribePullThroughCacheRulesResponseTypeDef",
    ) -> "dc_td.DescribePullThroughCacheRulesResponse":
        return dc_td.DescribePullThroughCacheRulesResponse.make_one(res)

    def describe_registry(
        self,
        res: "bs_td.DescribeRegistryResponseTypeDef",
    ) -> "dc_td.DescribeRegistryResponse":
        return dc_td.DescribeRegistryResponse.make_one(res)

    def describe_repositories(
        self,
        res: "bs_td.DescribeRepositoriesResponseTypeDef",
    ) -> "dc_td.DescribeRepositoriesResponse":
        return dc_td.DescribeRepositoriesResponse.make_one(res)

    def describe_repository_creation_templates(
        self,
        res: "bs_td.DescribeRepositoryCreationTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeRepositoryCreationTemplatesResponse":
        return dc_td.DescribeRepositoryCreationTemplatesResponse.make_one(res)

    def get_account_setting(
        self,
        res: "bs_td.GetAccountSettingResponseTypeDef",
    ) -> "dc_td.GetAccountSettingResponse":
        return dc_td.GetAccountSettingResponse.make_one(res)

    def get_authorization_token(
        self,
        res: "bs_td.GetAuthorizationTokenResponseTypeDef",
    ) -> "dc_td.GetAuthorizationTokenResponse":
        return dc_td.GetAuthorizationTokenResponse.make_one(res)

    def get_download_url_for_layer(
        self,
        res: "bs_td.GetDownloadUrlForLayerResponseTypeDef",
    ) -> "dc_td.GetDownloadUrlForLayerResponse":
        return dc_td.GetDownloadUrlForLayerResponse.make_one(res)

    def get_lifecycle_policy(
        self,
        res: "bs_td.GetLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.GetLifecyclePolicyResponse":
        return dc_td.GetLifecyclePolicyResponse.make_one(res)

    def get_lifecycle_policy_preview(
        self,
        res: "bs_td.GetLifecyclePolicyPreviewResponseTypeDef",
    ) -> "dc_td.GetLifecyclePolicyPreviewResponse":
        return dc_td.GetLifecyclePolicyPreviewResponse.make_one(res)

    def get_registry_policy(
        self,
        res: "bs_td.GetRegistryPolicyResponseTypeDef",
    ) -> "dc_td.GetRegistryPolicyResponse":
        return dc_td.GetRegistryPolicyResponse.make_one(res)

    def get_registry_scanning_configuration(
        self,
        res: "bs_td.GetRegistryScanningConfigurationResponseTypeDef",
    ) -> "dc_td.GetRegistryScanningConfigurationResponse":
        return dc_td.GetRegistryScanningConfigurationResponse.make_one(res)

    def get_repository_policy(
        self,
        res: "bs_td.GetRepositoryPolicyResponseTypeDef",
    ) -> "dc_td.GetRepositoryPolicyResponse":
        return dc_td.GetRepositoryPolicyResponse.make_one(res)

    def initiate_layer_upload(
        self,
        res: "bs_td.InitiateLayerUploadResponseTypeDef",
    ) -> "dc_td.InitiateLayerUploadResponse":
        return dc_td.InitiateLayerUploadResponse.make_one(res)

    def list_images(
        self,
        res: "bs_td.ListImagesResponseTypeDef",
    ) -> "dc_td.ListImagesResponse":
        return dc_td.ListImagesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_account_setting(
        self,
        res: "bs_td.PutAccountSettingResponseTypeDef",
    ) -> "dc_td.PutAccountSettingResponse":
        return dc_td.PutAccountSettingResponse.make_one(res)

    def put_image(
        self,
        res: "bs_td.PutImageResponseTypeDef",
    ) -> "dc_td.PutImageResponse":
        return dc_td.PutImageResponse.make_one(res)

    def put_image_scanning_configuration(
        self,
        res: "bs_td.PutImageScanningConfigurationResponseTypeDef",
    ) -> "dc_td.PutImageScanningConfigurationResponse":
        return dc_td.PutImageScanningConfigurationResponse.make_one(res)

    def put_image_tag_mutability(
        self,
        res: "bs_td.PutImageTagMutabilityResponseTypeDef",
    ) -> "dc_td.PutImageTagMutabilityResponse":
        return dc_td.PutImageTagMutabilityResponse.make_one(res)

    def put_lifecycle_policy(
        self,
        res: "bs_td.PutLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.PutLifecyclePolicyResponse":
        return dc_td.PutLifecyclePolicyResponse.make_one(res)

    def put_registry_policy(
        self,
        res: "bs_td.PutRegistryPolicyResponseTypeDef",
    ) -> "dc_td.PutRegistryPolicyResponse":
        return dc_td.PutRegistryPolicyResponse.make_one(res)

    def put_registry_scanning_configuration(
        self,
        res: "bs_td.PutRegistryScanningConfigurationResponseTypeDef",
    ) -> "dc_td.PutRegistryScanningConfigurationResponse":
        return dc_td.PutRegistryScanningConfigurationResponse.make_one(res)

    def put_replication_configuration(
        self,
        res: "bs_td.PutReplicationConfigurationResponseTypeDef",
    ) -> "dc_td.PutReplicationConfigurationResponse":
        return dc_td.PutReplicationConfigurationResponse.make_one(res)

    def set_repository_policy(
        self,
        res: "bs_td.SetRepositoryPolicyResponseTypeDef",
    ) -> "dc_td.SetRepositoryPolicyResponse":
        return dc_td.SetRepositoryPolicyResponse.make_one(res)

    def start_image_scan(
        self,
        res: "bs_td.StartImageScanResponseTypeDef",
    ) -> "dc_td.StartImageScanResponse":
        return dc_td.StartImageScanResponse.make_one(res)

    def start_lifecycle_policy_preview(
        self,
        res: "bs_td.StartLifecyclePolicyPreviewResponseTypeDef",
    ) -> "dc_td.StartLifecyclePolicyPreviewResponse":
        return dc_td.StartLifecyclePolicyPreviewResponse.make_one(res)

    def update_pull_through_cache_rule(
        self,
        res: "bs_td.UpdatePullThroughCacheRuleResponseTypeDef",
    ) -> "dc_td.UpdatePullThroughCacheRuleResponse":
        return dc_td.UpdatePullThroughCacheRuleResponse.make_one(res)

    def update_repository_creation_template(
        self,
        res: "bs_td.UpdateRepositoryCreationTemplateResponseTypeDef",
    ) -> "dc_td.UpdateRepositoryCreationTemplateResponse":
        return dc_td.UpdateRepositoryCreationTemplateResponse.make_one(res)

    def upload_layer_part(
        self,
        res: "bs_td.UploadLayerPartResponseTypeDef",
    ) -> "dc_td.UploadLayerPartResponse":
        return dc_td.UploadLayerPartResponse.make_one(res)

    def validate_pull_through_cache_rule(
        self,
        res: "bs_td.ValidatePullThroughCacheRuleResponseTypeDef",
    ) -> "dc_td.ValidatePullThroughCacheRuleResponse":
        return dc_td.ValidatePullThroughCacheRuleResponse.make_one(res)


ecr_caster = ECRCaster()
