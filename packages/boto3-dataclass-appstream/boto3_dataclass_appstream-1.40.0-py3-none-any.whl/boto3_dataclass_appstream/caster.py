# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appstream import type_defs as bs_td


class APPSTREAMCaster:

    def associate_app_block_builder_app_block(
        self,
        res: "bs_td.AssociateAppBlockBuilderAppBlockResultTypeDef",
    ) -> "dc_td.AssociateAppBlockBuilderAppBlockResult":
        return dc_td.AssociateAppBlockBuilderAppBlockResult.make_one(res)

    def associate_application_fleet(
        self,
        res: "bs_td.AssociateApplicationFleetResultTypeDef",
    ) -> "dc_td.AssociateApplicationFleetResult":
        return dc_td.AssociateApplicationFleetResult.make_one(res)

    def batch_associate_user_stack(
        self,
        res: "bs_td.BatchAssociateUserStackResultTypeDef",
    ) -> "dc_td.BatchAssociateUserStackResult":
        return dc_td.BatchAssociateUserStackResult.make_one(res)

    def batch_disassociate_user_stack(
        self,
        res: "bs_td.BatchDisassociateUserStackResultTypeDef",
    ) -> "dc_td.BatchDisassociateUserStackResult":
        return dc_td.BatchDisassociateUserStackResult.make_one(res)

    def copy_image(
        self,
        res: "bs_td.CopyImageResponseTypeDef",
    ) -> "dc_td.CopyImageResponse":
        return dc_td.CopyImageResponse.make_one(res)

    def create_app_block(
        self,
        res: "bs_td.CreateAppBlockResultTypeDef",
    ) -> "dc_td.CreateAppBlockResult":
        return dc_td.CreateAppBlockResult.make_one(res)

    def create_app_block_builder(
        self,
        res: "bs_td.CreateAppBlockBuilderResultTypeDef",
    ) -> "dc_td.CreateAppBlockBuilderResult":
        return dc_td.CreateAppBlockBuilderResult.make_one(res)

    def create_app_block_builder_streaming_url(
        self,
        res: "bs_td.CreateAppBlockBuilderStreamingURLResultTypeDef",
    ) -> "dc_td.CreateAppBlockBuilderStreamingURLResult":
        return dc_td.CreateAppBlockBuilderStreamingURLResult.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResultTypeDef",
    ) -> "dc_td.CreateApplicationResult":
        return dc_td.CreateApplicationResult.make_one(res)

    def create_directory_config(
        self,
        res: "bs_td.CreateDirectoryConfigResultTypeDef",
    ) -> "dc_td.CreateDirectoryConfigResult":
        return dc_td.CreateDirectoryConfigResult.make_one(res)

    def create_entitlement(
        self,
        res: "bs_td.CreateEntitlementResultTypeDef",
    ) -> "dc_td.CreateEntitlementResult":
        return dc_td.CreateEntitlementResult.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetResultTypeDef",
    ) -> "dc_td.CreateFleetResult":
        return dc_td.CreateFleetResult.make_one(res)

    def create_image_builder(
        self,
        res: "bs_td.CreateImageBuilderResultTypeDef",
    ) -> "dc_td.CreateImageBuilderResult":
        return dc_td.CreateImageBuilderResult.make_one(res)

    def create_image_builder_streaming_url(
        self,
        res: "bs_td.CreateImageBuilderStreamingURLResultTypeDef",
    ) -> "dc_td.CreateImageBuilderStreamingURLResult":
        return dc_td.CreateImageBuilderStreamingURLResult.make_one(res)

    def create_stack(
        self,
        res: "bs_td.CreateStackResultTypeDef",
    ) -> "dc_td.CreateStackResult":
        return dc_td.CreateStackResult.make_one(res)

    def create_streaming_url(
        self,
        res: "bs_td.CreateStreamingURLResultTypeDef",
    ) -> "dc_td.CreateStreamingURLResult":
        return dc_td.CreateStreamingURLResult.make_one(res)

    def create_theme_for_stack(
        self,
        res: "bs_td.CreateThemeForStackResultTypeDef",
    ) -> "dc_td.CreateThemeForStackResult":
        return dc_td.CreateThemeForStackResult.make_one(res)

    def create_updated_image(
        self,
        res: "bs_td.CreateUpdatedImageResultTypeDef",
    ) -> "dc_td.CreateUpdatedImageResult":
        return dc_td.CreateUpdatedImageResult.make_one(res)

    def create_usage_report_subscription(
        self,
        res: "bs_td.CreateUsageReportSubscriptionResultTypeDef",
    ) -> "dc_td.CreateUsageReportSubscriptionResult":
        return dc_td.CreateUsageReportSubscriptionResult.make_one(res)

    def delete_image(
        self,
        res: "bs_td.DeleteImageResultTypeDef",
    ) -> "dc_td.DeleteImageResult":
        return dc_td.DeleteImageResult.make_one(res)

    def delete_image_builder(
        self,
        res: "bs_td.DeleteImageBuilderResultTypeDef",
    ) -> "dc_td.DeleteImageBuilderResult":
        return dc_td.DeleteImageBuilderResult.make_one(res)

    def describe_app_block_builder_app_block_associations(
        self,
        res: "bs_td.DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef",
    ) -> "dc_td.DescribeAppBlockBuilderAppBlockAssociationsResult":
        return dc_td.DescribeAppBlockBuilderAppBlockAssociationsResult.make_one(res)

    def describe_app_block_builders(
        self,
        res: "bs_td.DescribeAppBlockBuildersResultTypeDef",
    ) -> "dc_td.DescribeAppBlockBuildersResult":
        return dc_td.DescribeAppBlockBuildersResult.make_one(res)

    def describe_app_blocks(
        self,
        res: "bs_td.DescribeAppBlocksResultTypeDef",
    ) -> "dc_td.DescribeAppBlocksResult":
        return dc_td.DescribeAppBlocksResult.make_one(res)

    def describe_application_fleet_associations(
        self,
        res: "bs_td.DescribeApplicationFleetAssociationsResultTypeDef",
    ) -> "dc_td.DescribeApplicationFleetAssociationsResult":
        return dc_td.DescribeApplicationFleetAssociationsResult.make_one(res)

    def describe_applications(
        self,
        res: "bs_td.DescribeApplicationsResultTypeDef",
    ) -> "dc_td.DescribeApplicationsResult":
        return dc_td.DescribeApplicationsResult.make_one(res)

    def describe_directory_configs(
        self,
        res: "bs_td.DescribeDirectoryConfigsResultTypeDef",
    ) -> "dc_td.DescribeDirectoryConfigsResult":
        return dc_td.DescribeDirectoryConfigsResult.make_one(res)

    def describe_entitlements(
        self,
        res: "bs_td.DescribeEntitlementsResultTypeDef",
    ) -> "dc_td.DescribeEntitlementsResult":
        return dc_td.DescribeEntitlementsResult.make_one(res)

    def describe_fleets(
        self,
        res: "bs_td.DescribeFleetsResultTypeDef",
    ) -> "dc_td.DescribeFleetsResult":
        return dc_td.DescribeFleetsResult.make_one(res)

    def describe_image_builders(
        self,
        res: "bs_td.DescribeImageBuildersResultTypeDef",
    ) -> "dc_td.DescribeImageBuildersResult":
        return dc_td.DescribeImageBuildersResult.make_one(res)

    def describe_image_permissions(
        self,
        res: "bs_td.DescribeImagePermissionsResultTypeDef",
    ) -> "dc_td.DescribeImagePermissionsResult":
        return dc_td.DescribeImagePermissionsResult.make_one(res)

    def describe_images(
        self,
        res: "bs_td.DescribeImagesResultTypeDef",
    ) -> "dc_td.DescribeImagesResult":
        return dc_td.DescribeImagesResult.make_one(res)

    def describe_sessions(
        self,
        res: "bs_td.DescribeSessionsResultTypeDef",
    ) -> "dc_td.DescribeSessionsResult":
        return dc_td.DescribeSessionsResult.make_one(res)

    def describe_stacks(
        self,
        res: "bs_td.DescribeStacksResultTypeDef",
    ) -> "dc_td.DescribeStacksResult":
        return dc_td.DescribeStacksResult.make_one(res)

    def describe_theme_for_stack(
        self,
        res: "bs_td.DescribeThemeForStackResultTypeDef",
    ) -> "dc_td.DescribeThemeForStackResult":
        return dc_td.DescribeThemeForStackResult.make_one(res)

    def describe_usage_report_subscriptions(
        self,
        res: "bs_td.DescribeUsageReportSubscriptionsResultTypeDef",
    ) -> "dc_td.DescribeUsageReportSubscriptionsResult":
        return dc_td.DescribeUsageReportSubscriptionsResult.make_one(res)

    def describe_user_stack_associations(
        self,
        res: "bs_td.DescribeUserStackAssociationsResultTypeDef",
    ) -> "dc_td.DescribeUserStackAssociationsResult":
        return dc_td.DescribeUserStackAssociationsResult.make_one(res)

    def describe_users(
        self,
        res: "bs_td.DescribeUsersResultTypeDef",
    ) -> "dc_td.DescribeUsersResult":
        return dc_td.DescribeUsersResult.make_one(res)

    def list_associated_fleets(
        self,
        res: "bs_td.ListAssociatedFleetsResultTypeDef",
    ) -> "dc_td.ListAssociatedFleetsResult":
        return dc_td.ListAssociatedFleetsResult.make_one(res)

    def list_associated_stacks(
        self,
        res: "bs_td.ListAssociatedStacksResultTypeDef",
    ) -> "dc_td.ListAssociatedStacksResult":
        return dc_td.ListAssociatedStacksResult.make_one(res)

    def list_entitled_applications(
        self,
        res: "bs_td.ListEntitledApplicationsResultTypeDef",
    ) -> "dc_td.ListEntitledApplicationsResult":
        return dc_td.ListEntitledApplicationsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_app_block_builder(
        self,
        res: "bs_td.StartAppBlockBuilderResultTypeDef",
    ) -> "dc_td.StartAppBlockBuilderResult":
        return dc_td.StartAppBlockBuilderResult.make_one(res)

    def start_image_builder(
        self,
        res: "bs_td.StartImageBuilderResultTypeDef",
    ) -> "dc_td.StartImageBuilderResult":
        return dc_td.StartImageBuilderResult.make_one(res)

    def stop_app_block_builder(
        self,
        res: "bs_td.StopAppBlockBuilderResultTypeDef",
    ) -> "dc_td.StopAppBlockBuilderResult":
        return dc_td.StopAppBlockBuilderResult.make_one(res)

    def stop_image_builder(
        self,
        res: "bs_td.StopImageBuilderResultTypeDef",
    ) -> "dc_td.StopImageBuilderResult":
        return dc_td.StopImageBuilderResult.make_one(res)

    def update_app_block_builder(
        self,
        res: "bs_td.UpdateAppBlockBuilderResultTypeDef",
    ) -> "dc_td.UpdateAppBlockBuilderResult":
        return dc_td.UpdateAppBlockBuilderResult.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResultTypeDef",
    ) -> "dc_td.UpdateApplicationResult":
        return dc_td.UpdateApplicationResult.make_one(res)

    def update_directory_config(
        self,
        res: "bs_td.UpdateDirectoryConfigResultTypeDef",
    ) -> "dc_td.UpdateDirectoryConfigResult":
        return dc_td.UpdateDirectoryConfigResult.make_one(res)

    def update_entitlement(
        self,
        res: "bs_td.UpdateEntitlementResultTypeDef",
    ) -> "dc_td.UpdateEntitlementResult":
        return dc_td.UpdateEntitlementResult.make_one(res)

    def update_fleet(
        self,
        res: "bs_td.UpdateFleetResultTypeDef",
    ) -> "dc_td.UpdateFleetResult":
        return dc_td.UpdateFleetResult.make_one(res)

    def update_stack(
        self,
        res: "bs_td.UpdateStackResultTypeDef",
    ) -> "dc_td.UpdateStackResult":
        return dc_td.UpdateStackResult.make_one(res)

    def update_theme_for_stack(
        self,
        res: "bs_td.UpdateThemeForStackResultTypeDef",
    ) -> "dc_td.UpdateThemeForStackResult":
        return dc_td.UpdateThemeForStackResult.make_one(res)


appstream_caster = APPSTREAMCaster()
