# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appsync import type_defs as bs_td


class APPSYNCCaster:

    def associate_api(
        self,
        res: "bs_td.AssociateApiResponseTypeDef",
    ) -> "dc_td.AssociateApiResponse":
        return dc_td.AssociateApiResponse.make_one(res)

    def associate_merged_graphql_api(
        self,
        res: "bs_td.AssociateMergedGraphqlApiResponseTypeDef",
    ) -> "dc_td.AssociateMergedGraphqlApiResponse":
        return dc_td.AssociateMergedGraphqlApiResponse.make_one(res)

    def associate_source_graphql_api(
        self,
        res: "bs_td.AssociateSourceGraphqlApiResponseTypeDef",
    ) -> "dc_td.AssociateSourceGraphqlApiResponse":
        return dc_td.AssociateSourceGraphqlApiResponse.make_one(res)

    def create_api(
        self,
        res: "bs_td.CreateApiResponseTypeDef",
    ) -> "dc_td.CreateApiResponse":
        return dc_td.CreateApiResponse.make_one(res)

    def create_api_cache(
        self,
        res: "bs_td.CreateApiCacheResponseTypeDef",
    ) -> "dc_td.CreateApiCacheResponse":
        return dc_td.CreateApiCacheResponse.make_one(res)

    def create_api_key(
        self,
        res: "bs_td.CreateApiKeyResponseTypeDef",
    ) -> "dc_td.CreateApiKeyResponse":
        return dc_td.CreateApiKeyResponse.make_one(res)

    def create_channel_namespace(
        self,
        res: "bs_td.CreateChannelNamespaceResponseTypeDef",
    ) -> "dc_td.CreateChannelNamespaceResponse":
        return dc_td.CreateChannelNamespaceResponse.make_one(res)

    def create_data_source(
        self,
        res: "bs_td.CreateDataSourceResponseTypeDef",
    ) -> "dc_td.CreateDataSourceResponse":
        return dc_td.CreateDataSourceResponse.make_one(res)

    def create_domain_name(
        self,
        res: "bs_td.CreateDomainNameResponseTypeDef",
    ) -> "dc_td.CreateDomainNameResponse":
        return dc_td.CreateDomainNameResponse.make_one(res)

    def create_function(
        self,
        res: "bs_td.CreateFunctionResponseTypeDef",
    ) -> "dc_td.CreateFunctionResponse":
        return dc_td.CreateFunctionResponse.make_one(res)

    def create_graphql_api(
        self,
        res: "bs_td.CreateGraphqlApiResponseTypeDef",
    ) -> "dc_td.CreateGraphqlApiResponse":
        return dc_td.CreateGraphqlApiResponse.make_one(res)

    def create_resolver(
        self,
        res: "bs_td.CreateResolverResponseTypeDef",
    ) -> "dc_td.CreateResolverResponse":
        return dc_td.CreateResolverResponse.make_one(res)

    def create_type(
        self,
        res: "bs_td.CreateTypeResponseTypeDef",
    ) -> "dc_td.CreateTypeResponse":
        return dc_td.CreateTypeResponse.make_one(res)

    def disassociate_merged_graphql_api(
        self,
        res: "bs_td.DisassociateMergedGraphqlApiResponseTypeDef",
    ) -> "dc_td.DisassociateMergedGraphqlApiResponse":
        return dc_td.DisassociateMergedGraphqlApiResponse.make_one(res)

    def disassociate_source_graphql_api(
        self,
        res: "bs_td.DisassociateSourceGraphqlApiResponseTypeDef",
    ) -> "dc_td.DisassociateSourceGraphqlApiResponse":
        return dc_td.DisassociateSourceGraphqlApiResponse.make_one(res)

    def evaluate_code(
        self,
        res: "bs_td.EvaluateCodeResponseTypeDef",
    ) -> "dc_td.EvaluateCodeResponse":
        return dc_td.EvaluateCodeResponse.make_one(res)

    def evaluate_mapping_template(
        self,
        res: "bs_td.EvaluateMappingTemplateResponseTypeDef",
    ) -> "dc_td.EvaluateMappingTemplateResponse":
        return dc_td.EvaluateMappingTemplateResponse.make_one(res)

    def get_api(
        self,
        res: "bs_td.GetApiResponseTypeDef",
    ) -> "dc_td.GetApiResponse":
        return dc_td.GetApiResponse.make_one(res)

    def get_api_association(
        self,
        res: "bs_td.GetApiAssociationResponseTypeDef",
    ) -> "dc_td.GetApiAssociationResponse":
        return dc_td.GetApiAssociationResponse.make_one(res)

    def get_api_cache(
        self,
        res: "bs_td.GetApiCacheResponseTypeDef",
    ) -> "dc_td.GetApiCacheResponse":
        return dc_td.GetApiCacheResponse.make_one(res)

    def get_channel_namespace(
        self,
        res: "bs_td.GetChannelNamespaceResponseTypeDef",
    ) -> "dc_td.GetChannelNamespaceResponse":
        return dc_td.GetChannelNamespaceResponse.make_one(res)

    def get_data_source(
        self,
        res: "bs_td.GetDataSourceResponseTypeDef",
    ) -> "dc_td.GetDataSourceResponse":
        return dc_td.GetDataSourceResponse.make_one(res)

    def get_data_source_introspection(
        self,
        res: "bs_td.GetDataSourceIntrospectionResponseTypeDef",
    ) -> "dc_td.GetDataSourceIntrospectionResponse":
        return dc_td.GetDataSourceIntrospectionResponse.make_one(res)

    def get_domain_name(
        self,
        res: "bs_td.GetDomainNameResponseTypeDef",
    ) -> "dc_td.GetDomainNameResponse":
        return dc_td.GetDomainNameResponse.make_one(res)

    def get_function(
        self,
        res: "bs_td.GetFunctionResponseTypeDef",
    ) -> "dc_td.GetFunctionResponse":
        return dc_td.GetFunctionResponse.make_one(res)

    def get_graphql_api(
        self,
        res: "bs_td.GetGraphqlApiResponseTypeDef",
    ) -> "dc_td.GetGraphqlApiResponse":
        return dc_td.GetGraphqlApiResponse.make_one(res)

    def get_graphql_api_environment_variables(
        self,
        res: "bs_td.GetGraphqlApiEnvironmentVariablesResponseTypeDef",
    ) -> "dc_td.GetGraphqlApiEnvironmentVariablesResponse":
        return dc_td.GetGraphqlApiEnvironmentVariablesResponse.make_one(res)

    def get_introspection_schema(
        self,
        res: "bs_td.GetIntrospectionSchemaResponseTypeDef",
    ) -> "dc_td.GetIntrospectionSchemaResponse":
        return dc_td.GetIntrospectionSchemaResponse.make_one(res)

    def get_resolver(
        self,
        res: "bs_td.GetResolverResponseTypeDef",
    ) -> "dc_td.GetResolverResponse":
        return dc_td.GetResolverResponse.make_one(res)

    def get_schema_creation_status(
        self,
        res: "bs_td.GetSchemaCreationStatusResponseTypeDef",
    ) -> "dc_td.GetSchemaCreationStatusResponse":
        return dc_td.GetSchemaCreationStatusResponse.make_one(res)

    def get_source_api_association(
        self,
        res: "bs_td.GetSourceApiAssociationResponseTypeDef",
    ) -> "dc_td.GetSourceApiAssociationResponse":
        return dc_td.GetSourceApiAssociationResponse.make_one(res)

    def get_type(
        self,
        res: "bs_td.GetTypeResponseTypeDef",
    ) -> "dc_td.GetTypeResponse":
        return dc_td.GetTypeResponse.make_one(res)

    def list_api_keys(
        self,
        res: "bs_td.ListApiKeysResponseTypeDef",
    ) -> "dc_td.ListApiKeysResponse":
        return dc_td.ListApiKeysResponse.make_one(res)

    def list_apis(
        self,
        res: "bs_td.ListApisResponseTypeDef",
    ) -> "dc_td.ListApisResponse":
        return dc_td.ListApisResponse.make_one(res)

    def list_channel_namespaces(
        self,
        res: "bs_td.ListChannelNamespacesResponseTypeDef",
    ) -> "dc_td.ListChannelNamespacesResponse":
        return dc_td.ListChannelNamespacesResponse.make_one(res)

    def list_data_sources(
        self,
        res: "bs_td.ListDataSourcesResponseTypeDef",
    ) -> "dc_td.ListDataSourcesResponse":
        return dc_td.ListDataSourcesResponse.make_one(res)

    def list_domain_names(
        self,
        res: "bs_td.ListDomainNamesResponseTypeDef",
    ) -> "dc_td.ListDomainNamesResponse":
        return dc_td.ListDomainNamesResponse.make_one(res)

    def list_functions(
        self,
        res: "bs_td.ListFunctionsResponseTypeDef",
    ) -> "dc_td.ListFunctionsResponse":
        return dc_td.ListFunctionsResponse.make_one(res)

    def list_graphql_apis(
        self,
        res: "bs_td.ListGraphqlApisResponseTypeDef",
    ) -> "dc_td.ListGraphqlApisResponse":
        return dc_td.ListGraphqlApisResponse.make_one(res)

    def list_resolvers(
        self,
        res: "bs_td.ListResolversResponseTypeDef",
    ) -> "dc_td.ListResolversResponse":
        return dc_td.ListResolversResponse.make_one(res)

    def list_resolvers_by_function(
        self,
        res: "bs_td.ListResolversByFunctionResponseTypeDef",
    ) -> "dc_td.ListResolversByFunctionResponse":
        return dc_td.ListResolversByFunctionResponse.make_one(res)

    def list_source_api_associations(
        self,
        res: "bs_td.ListSourceApiAssociationsResponseTypeDef",
    ) -> "dc_td.ListSourceApiAssociationsResponse":
        return dc_td.ListSourceApiAssociationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_types(
        self,
        res: "bs_td.ListTypesResponseTypeDef",
    ) -> "dc_td.ListTypesResponse":
        return dc_td.ListTypesResponse.make_one(res)

    def list_types_by_association(
        self,
        res: "bs_td.ListTypesByAssociationResponseTypeDef",
    ) -> "dc_td.ListTypesByAssociationResponse":
        return dc_td.ListTypesByAssociationResponse.make_one(res)

    def put_graphql_api_environment_variables(
        self,
        res: "bs_td.PutGraphqlApiEnvironmentVariablesResponseTypeDef",
    ) -> "dc_td.PutGraphqlApiEnvironmentVariablesResponse":
        return dc_td.PutGraphqlApiEnvironmentVariablesResponse.make_one(res)

    def start_data_source_introspection(
        self,
        res: "bs_td.StartDataSourceIntrospectionResponseTypeDef",
    ) -> "dc_td.StartDataSourceIntrospectionResponse":
        return dc_td.StartDataSourceIntrospectionResponse.make_one(res)

    def start_schema_creation(
        self,
        res: "bs_td.StartSchemaCreationResponseTypeDef",
    ) -> "dc_td.StartSchemaCreationResponse":
        return dc_td.StartSchemaCreationResponse.make_one(res)

    def start_schema_merge(
        self,
        res: "bs_td.StartSchemaMergeResponseTypeDef",
    ) -> "dc_td.StartSchemaMergeResponse":
        return dc_td.StartSchemaMergeResponse.make_one(res)

    def update_api(
        self,
        res: "bs_td.UpdateApiResponseTypeDef",
    ) -> "dc_td.UpdateApiResponse":
        return dc_td.UpdateApiResponse.make_one(res)

    def update_api_cache(
        self,
        res: "bs_td.UpdateApiCacheResponseTypeDef",
    ) -> "dc_td.UpdateApiCacheResponse":
        return dc_td.UpdateApiCacheResponse.make_one(res)

    def update_api_key(
        self,
        res: "bs_td.UpdateApiKeyResponseTypeDef",
    ) -> "dc_td.UpdateApiKeyResponse":
        return dc_td.UpdateApiKeyResponse.make_one(res)

    def update_channel_namespace(
        self,
        res: "bs_td.UpdateChannelNamespaceResponseTypeDef",
    ) -> "dc_td.UpdateChannelNamespaceResponse":
        return dc_td.UpdateChannelNamespaceResponse.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.UpdateDataSourceResponseTypeDef",
    ) -> "dc_td.UpdateDataSourceResponse":
        return dc_td.UpdateDataSourceResponse.make_one(res)

    def update_domain_name(
        self,
        res: "bs_td.UpdateDomainNameResponseTypeDef",
    ) -> "dc_td.UpdateDomainNameResponse":
        return dc_td.UpdateDomainNameResponse.make_one(res)

    def update_function(
        self,
        res: "bs_td.UpdateFunctionResponseTypeDef",
    ) -> "dc_td.UpdateFunctionResponse":
        return dc_td.UpdateFunctionResponse.make_one(res)

    def update_graphql_api(
        self,
        res: "bs_td.UpdateGraphqlApiResponseTypeDef",
    ) -> "dc_td.UpdateGraphqlApiResponse":
        return dc_td.UpdateGraphqlApiResponse.make_one(res)

    def update_resolver(
        self,
        res: "bs_td.UpdateResolverResponseTypeDef",
    ) -> "dc_td.UpdateResolverResponse":
        return dc_td.UpdateResolverResponse.make_one(res)

    def update_source_api_association(
        self,
        res: "bs_td.UpdateSourceApiAssociationResponseTypeDef",
    ) -> "dc_td.UpdateSourceApiAssociationResponse":
        return dc_td.UpdateSourceApiAssociationResponse.make_one(res)

    def update_type(
        self,
        res: "bs_td.UpdateTypeResponseTypeDef",
    ) -> "dc_td.UpdateTypeResponse":
        return dc_td.UpdateTypeResponse.make_one(res)


appsync_caster = APPSYNCCaster()
