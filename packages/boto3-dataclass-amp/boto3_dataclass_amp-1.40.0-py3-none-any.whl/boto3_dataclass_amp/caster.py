# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amp import type_defs as bs_td


class AMPCaster:

    def create_alert_manager_definition(
        self,
        res: "bs_td.CreateAlertManagerDefinitionResponseTypeDef",
    ) -> "dc_td.CreateAlertManagerDefinitionResponse":
        return dc_td.CreateAlertManagerDefinitionResponse.make_one(res)

    def create_logging_configuration(
        self,
        res: "bs_td.CreateLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.CreateLoggingConfigurationResponse":
        return dc_td.CreateLoggingConfigurationResponse.make_one(res)

    def create_query_logging_configuration(
        self,
        res: "bs_td.CreateQueryLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.CreateQueryLoggingConfigurationResponse":
        return dc_td.CreateQueryLoggingConfigurationResponse.make_one(res)

    def create_rule_groups_namespace(
        self,
        res: "bs_td.CreateRuleGroupsNamespaceResponseTypeDef",
    ) -> "dc_td.CreateRuleGroupsNamespaceResponse":
        return dc_td.CreateRuleGroupsNamespaceResponse.make_one(res)

    def create_scraper(
        self,
        res: "bs_td.CreateScraperResponseTypeDef",
    ) -> "dc_td.CreateScraperResponse":
        return dc_td.CreateScraperResponse.make_one(res)

    def create_workspace(
        self,
        res: "bs_td.CreateWorkspaceResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceResponse":
        return dc_td.CreateWorkspaceResponse.make_one(res)

    def delete_alert_manager_definition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_logging_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_query_logging_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_rule_groups_namespace(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_scraper(
        self,
        res: "bs_td.DeleteScraperResponseTypeDef",
    ) -> "dc_td.DeleteScraperResponse":
        return dc_td.DeleteScraperResponse.make_one(res)

    def delete_scraper_logging_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workspace(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_alert_manager_definition(
        self,
        res: "bs_td.DescribeAlertManagerDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeAlertManagerDefinitionResponse":
        return dc_td.DescribeAlertManagerDefinitionResponse.make_one(res)

    def describe_logging_configuration(
        self,
        res: "bs_td.DescribeLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeLoggingConfigurationResponse":
        return dc_td.DescribeLoggingConfigurationResponse.make_one(res)

    def describe_query_logging_configuration(
        self,
        res: "bs_td.DescribeQueryLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeQueryLoggingConfigurationResponse":
        return dc_td.DescribeQueryLoggingConfigurationResponse.make_one(res)

    def describe_resource_policy(
        self,
        res: "bs_td.DescribeResourcePolicyResponseTypeDef",
    ) -> "dc_td.DescribeResourcePolicyResponse":
        return dc_td.DescribeResourcePolicyResponse.make_one(res)

    def describe_rule_groups_namespace(
        self,
        res: "bs_td.DescribeRuleGroupsNamespaceResponseTypeDef",
    ) -> "dc_td.DescribeRuleGroupsNamespaceResponse":
        return dc_td.DescribeRuleGroupsNamespaceResponse.make_one(res)

    def describe_scraper(
        self,
        res: "bs_td.DescribeScraperResponseTypeDef",
    ) -> "dc_td.DescribeScraperResponse":
        return dc_td.DescribeScraperResponse.make_one(res)

    def describe_scraper_logging_configuration(
        self,
        res: "bs_td.DescribeScraperLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeScraperLoggingConfigurationResponse":
        return dc_td.DescribeScraperLoggingConfigurationResponse.make_one(res)

    def describe_workspace(
        self,
        res: "bs_td.DescribeWorkspaceResponseTypeDef",
    ) -> "dc_td.DescribeWorkspaceResponse":
        return dc_td.DescribeWorkspaceResponse.make_one(res)

    def describe_workspace_configuration(
        self,
        res: "bs_td.DescribeWorkspaceConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeWorkspaceConfigurationResponse":
        return dc_td.DescribeWorkspaceConfigurationResponse.make_one(res)

    def get_default_scraper_configuration(
        self,
        res: "bs_td.GetDefaultScraperConfigurationResponseTypeDef",
    ) -> "dc_td.GetDefaultScraperConfigurationResponse":
        return dc_td.GetDefaultScraperConfigurationResponse.make_one(res)

    def list_rule_groups_namespaces(
        self,
        res: "bs_td.ListRuleGroupsNamespacesResponseTypeDef",
    ) -> "dc_td.ListRuleGroupsNamespacesResponse":
        return dc_td.ListRuleGroupsNamespacesResponse.make_one(res)

    def list_scrapers(
        self,
        res: "bs_td.ListScrapersResponseTypeDef",
    ) -> "dc_td.ListScrapersResponse":
        return dc_td.ListScrapersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_workspaces(
        self,
        res: "bs_td.ListWorkspacesResponseTypeDef",
    ) -> "dc_td.ListWorkspacesResponse":
        return dc_td.ListWorkspacesResponse.make_one(res)

    def put_alert_manager_definition(
        self,
        res: "bs_td.PutAlertManagerDefinitionResponseTypeDef",
    ) -> "dc_td.PutAlertManagerDefinitionResponse":
        return dc_td.PutAlertManagerDefinitionResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def put_rule_groups_namespace(
        self,
        res: "bs_td.PutRuleGroupsNamespaceResponseTypeDef",
    ) -> "dc_td.PutRuleGroupsNamespaceResponse":
        return dc_td.PutRuleGroupsNamespaceResponse.make_one(res)

    def update_logging_configuration(
        self,
        res: "bs_td.UpdateLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateLoggingConfigurationResponse":
        return dc_td.UpdateLoggingConfigurationResponse.make_one(res)

    def update_query_logging_configuration(
        self,
        res: "bs_td.UpdateQueryLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateQueryLoggingConfigurationResponse":
        return dc_td.UpdateQueryLoggingConfigurationResponse.make_one(res)

    def update_scraper(
        self,
        res: "bs_td.UpdateScraperResponseTypeDef",
    ) -> "dc_td.UpdateScraperResponse":
        return dc_td.UpdateScraperResponse.make_one(res)

    def update_scraper_logging_configuration(
        self,
        res: "bs_td.UpdateScraperLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateScraperLoggingConfigurationResponse":
        return dc_td.UpdateScraperLoggingConfigurationResponse.make_one(res)

    def update_workspace_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_workspace_configuration(
        self,
        res: "bs_td.UpdateWorkspaceConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateWorkspaceConfigurationResponse":
        return dc_td.UpdateWorkspaceConfigurationResponse.make_one(res)


amp_caster = AMPCaster()
