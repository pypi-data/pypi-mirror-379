# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lambda import type_defs as bs_td


class LAMBDACaster:

    def add_layer_version_permission(
        self,
        res: "bs_td.AddLayerVersionPermissionResponseTypeDef",
    ) -> "dc_td.AddLayerVersionPermissionResponse":
        return dc_td.AddLayerVersionPermissionResponse.make_one(res)

    def add_permission(
        self,
        res: "bs_td.AddPermissionResponseTypeDef",
    ) -> "dc_td.AddPermissionResponse":
        return dc_td.AddPermissionResponse.make_one(res)

    def create_alias(
        self,
        res: "bs_td.AliasConfigurationResponseTypeDef",
    ) -> "dc_td.AliasConfigurationResponse":
        return dc_td.AliasConfigurationResponse.make_one(res)

    def create_code_signing_config(
        self,
        res: "bs_td.CreateCodeSigningConfigResponseTypeDef",
    ) -> "dc_td.CreateCodeSigningConfigResponse":
        return dc_td.CreateCodeSigningConfigResponse.make_one(res)

    def create_event_source_mapping(
        self,
        res: "bs_td.EventSourceMappingConfigurationResponseTypeDef",
    ) -> "dc_td.EventSourceMappingConfigurationResponse":
        return dc_td.EventSourceMappingConfigurationResponse.make_one(res)

    def create_function(
        self,
        res: "bs_td.FunctionConfigurationResponseTypeDef",
    ) -> "dc_td.FunctionConfigurationResponse":
        return dc_td.FunctionConfigurationResponse.make_one(res)

    def create_function_url_config(
        self,
        res: "bs_td.CreateFunctionUrlConfigResponseTypeDef",
    ) -> "dc_td.CreateFunctionUrlConfigResponse":
        return dc_td.CreateFunctionUrlConfigResponse.make_one(res)

    def delete_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_source_mapping(
        self,
        res: "bs_td.EventSourceMappingConfigurationResponseTypeDef",
    ) -> "dc_td.EventSourceMappingConfigurationResponse":
        return dc_td.EventSourceMappingConfigurationResponse.make_one(res)

    def delete_function(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_function_code_signing_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_function_concurrency(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_function_event_invoke_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_function_url_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_layer_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_provisioned_concurrency_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsResponseTypeDef",
    ) -> "dc_td.GetAccountSettingsResponse":
        return dc_td.GetAccountSettingsResponse.make_one(res)

    def get_alias(
        self,
        res: "bs_td.AliasConfigurationResponseTypeDef",
    ) -> "dc_td.AliasConfigurationResponse":
        return dc_td.AliasConfigurationResponse.make_one(res)

    def get_code_signing_config(
        self,
        res: "bs_td.GetCodeSigningConfigResponseTypeDef",
    ) -> "dc_td.GetCodeSigningConfigResponse":
        return dc_td.GetCodeSigningConfigResponse.make_one(res)

    def get_event_source_mapping(
        self,
        res: "bs_td.EventSourceMappingConfigurationResponseTypeDef",
    ) -> "dc_td.EventSourceMappingConfigurationResponse":
        return dc_td.EventSourceMappingConfigurationResponse.make_one(res)

    def get_function(
        self,
        res: "bs_td.GetFunctionResponseTypeDef",
    ) -> "dc_td.GetFunctionResponse":
        return dc_td.GetFunctionResponse.make_one(res)

    def get_function_code_signing_config(
        self,
        res: "bs_td.GetFunctionCodeSigningConfigResponseTypeDef",
    ) -> "dc_td.GetFunctionCodeSigningConfigResponse":
        return dc_td.GetFunctionCodeSigningConfigResponse.make_one(res)

    def get_function_concurrency(
        self,
        res: "bs_td.GetFunctionConcurrencyResponseTypeDef",
    ) -> "dc_td.GetFunctionConcurrencyResponse":
        return dc_td.GetFunctionConcurrencyResponse.make_one(res)

    def get_function_configuration(
        self,
        res: "bs_td.FunctionConfigurationResponseTypeDef",
    ) -> "dc_td.FunctionConfigurationResponse":
        return dc_td.FunctionConfigurationResponse.make_one(res)

    def get_function_event_invoke_config(
        self,
        res: "bs_td.FunctionEventInvokeConfigResponseTypeDef",
    ) -> "dc_td.FunctionEventInvokeConfigResponse":
        return dc_td.FunctionEventInvokeConfigResponse.make_one(res)

    def get_function_recursion_config(
        self,
        res: "bs_td.GetFunctionRecursionConfigResponseTypeDef",
    ) -> "dc_td.GetFunctionRecursionConfigResponse":
        return dc_td.GetFunctionRecursionConfigResponse.make_one(res)

    def get_function_url_config(
        self,
        res: "bs_td.GetFunctionUrlConfigResponseTypeDef",
    ) -> "dc_td.GetFunctionUrlConfigResponse":
        return dc_td.GetFunctionUrlConfigResponse.make_one(res)

    def get_layer_version(
        self,
        res: "bs_td.GetLayerVersionResponseTypeDef",
    ) -> "dc_td.GetLayerVersionResponse":
        return dc_td.GetLayerVersionResponse.make_one(res)

    def get_layer_version_by_arn(
        self,
        res: "bs_td.GetLayerVersionResponseTypeDef",
    ) -> "dc_td.GetLayerVersionResponse":
        return dc_td.GetLayerVersionResponse.make_one(res)

    def get_layer_version_policy(
        self,
        res: "bs_td.GetLayerVersionPolicyResponseTypeDef",
    ) -> "dc_td.GetLayerVersionPolicyResponse":
        return dc_td.GetLayerVersionPolicyResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_provisioned_concurrency_config(
        self,
        res: "bs_td.GetProvisionedConcurrencyConfigResponseTypeDef",
    ) -> "dc_td.GetProvisionedConcurrencyConfigResponse":
        return dc_td.GetProvisionedConcurrencyConfigResponse.make_one(res)

    def get_runtime_management_config(
        self,
        res: "bs_td.GetRuntimeManagementConfigResponseTypeDef",
    ) -> "dc_td.GetRuntimeManagementConfigResponse":
        return dc_td.GetRuntimeManagementConfigResponse.make_one(res)

    def invoke(
        self,
        res: "bs_td.InvocationResponseTypeDef",
    ) -> "dc_td.InvocationResponse":
        return dc_td.InvocationResponse.make_one(res)

    def invoke_async(
        self,
        res: "bs_td.InvokeAsyncResponseTypeDef",
    ) -> "dc_td.InvokeAsyncResponse":
        return dc_td.InvokeAsyncResponse.make_one(res)

    def invoke_with_response_stream(
        self,
        res: "bs_td.InvokeWithResponseStreamResponseTypeDef",
    ) -> "dc_td.InvokeWithResponseStreamResponse":
        return dc_td.InvokeWithResponseStreamResponse.make_one(res)

    def list_aliases(
        self,
        res: "bs_td.ListAliasesResponseTypeDef",
    ) -> "dc_td.ListAliasesResponse":
        return dc_td.ListAliasesResponse.make_one(res)

    def list_code_signing_configs(
        self,
        res: "bs_td.ListCodeSigningConfigsResponseTypeDef",
    ) -> "dc_td.ListCodeSigningConfigsResponse":
        return dc_td.ListCodeSigningConfigsResponse.make_one(res)

    def list_event_source_mappings(
        self,
        res: "bs_td.ListEventSourceMappingsResponseTypeDef",
    ) -> "dc_td.ListEventSourceMappingsResponse":
        return dc_td.ListEventSourceMappingsResponse.make_one(res)

    def list_function_event_invoke_configs(
        self,
        res: "bs_td.ListFunctionEventInvokeConfigsResponseTypeDef",
    ) -> "dc_td.ListFunctionEventInvokeConfigsResponse":
        return dc_td.ListFunctionEventInvokeConfigsResponse.make_one(res)

    def list_function_url_configs(
        self,
        res: "bs_td.ListFunctionUrlConfigsResponseTypeDef",
    ) -> "dc_td.ListFunctionUrlConfigsResponse":
        return dc_td.ListFunctionUrlConfigsResponse.make_one(res)

    def list_functions(
        self,
        res: "bs_td.ListFunctionsResponseTypeDef",
    ) -> "dc_td.ListFunctionsResponse":
        return dc_td.ListFunctionsResponse.make_one(res)

    def list_functions_by_code_signing_config(
        self,
        res: "bs_td.ListFunctionsByCodeSigningConfigResponseTypeDef",
    ) -> "dc_td.ListFunctionsByCodeSigningConfigResponse":
        return dc_td.ListFunctionsByCodeSigningConfigResponse.make_one(res)

    def list_layer_versions(
        self,
        res: "bs_td.ListLayerVersionsResponseTypeDef",
    ) -> "dc_td.ListLayerVersionsResponse":
        return dc_td.ListLayerVersionsResponse.make_one(res)

    def list_layers(
        self,
        res: "bs_td.ListLayersResponseTypeDef",
    ) -> "dc_td.ListLayersResponse":
        return dc_td.ListLayersResponse.make_one(res)

    def list_provisioned_concurrency_configs(
        self,
        res: "bs_td.ListProvisionedConcurrencyConfigsResponseTypeDef",
    ) -> "dc_td.ListProvisionedConcurrencyConfigsResponse":
        return dc_td.ListProvisionedConcurrencyConfigsResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def list_versions_by_function(
        self,
        res: "bs_td.ListVersionsByFunctionResponseTypeDef",
    ) -> "dc_td.ListVersionsByFunctionResponse":
        return dc_td.ListVersionsByFunctionResponse.make_one(res)

    def publish_layer_version(
        self,
        res: "bs_td.PublishLayerVersionResponseTypeDef",
    ) -> "dc_td.PublishLayerVersionResponse":
        return dc_td.PublishLayerVersionResponse.make_one(res)

    def publish_version(
        self,
        res: "bs_td.FunctionConfigurationResponseTypeDef",
    ) -> "dc_td.FunctionConfigurationResponse":
        return dc_td.FunctionConfigurationResponse.make_one(res)

    def put_function_code_signing_config(
        self,
        res: "bs_td.PutFunctionCodeSigningConfigResponseTypeDef",
    ) -> "dc_td.PutFunctionCodeSigningConfigResponse":
        return dc_td.PutFunctionCodeSigningConfigResponse.make_one(res)

    def put_function_concurrency(
        self,
        res: "bs_td.ConcurrencyResponseTypeDef",
    ) -> "dc_td.ConcurrencyResponse":
        return dc_td.ConcurrencyResponse.make_one(res)

    def put_function_event_invoke_config(
        self,
        res: "bs_td.FunctionEventInvokeConfigResponseTypeDef",
    ) -> "dc_td.FunctionEventInvokeConfigResponse":
        return dc_td.FunctionEventInvokeConfigResponse.make_one(res)

    def put_function_recursion_config(
        self,
        res: "bs_td.PutFunctionRecursionConfigResponseTypeDef",
    ) -> "dc_td.PutFunctionRecursionConfigResponse":
        return dc_td.PutFunctionRecursionConfigResponse.make_one(res)

    def put_provisioned_concurrency_config(
        self,
        res: "bs_td.PutProvisionedConcurrencyConfigResponseTypeDef",
    ) -> "dc_td.PutProvisionedConcurrencyConfigResponse":
        return dc_td.PutProvisionedConcurrencyConfigResponse.make_one(res)

    def put_runtime_management_config(
        self,
        res: "bs_td.PutRuntimeManagementConfigResponseTypeDef",
    ) -> "dc_td.PutRuntimeManagementConfigResponse":
        return dc_td.PutRuntimeManagementConfigResponse.make_one(res)

    def remove_layer_version_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_alias(
        self,
        res: "bs_td.AliasConfigurationResponseTypeDef",
    ) -> "dc_td.AliasConfigurationResponse":
        return dc_td.AliasConfigurationResponse.make_one(res)

    def update_code_signing_config(
        self,
        res: "bs_td.UpdateCodeSigningConfigResponseTypeDef",
    ) -> "dc_td.UpdateCodeSigningConfigResponse":
        return dc_td.UpdateCodeSigningConfigResponse.make_one(res)

    def update_event_source_mapping(
        self,
        res: "bs_td.EventSourceMappingConfigurationResponseTypeDef",
    ) -> "dc_td.EventSourceMappingConfigurationResponse":
        return dc_td.EventSourceMappingConfigurationResponse.make_one(res)

    def update_function_code(
        self,
        res: "bs_td.FunctionConfigurationResponseTypeDef",
    ) -> "dc_td.FunctionConfigurationResponse":
        return dc_td.FunctionConfigurationResponse.make_one(res)

    def update_function_configuration(
        self,
        res: "bs_td.FunctionConfigurationResponseTypeDef",
    ) -> "dc_td.FunctionConfigurationResponse":
        return dc_td.FunctionConfigurationResponse.make_one(res)

    def update_function_event_invoke_config(
        self,
        res: "bs_td.FunctionEventInvokeConfigResponseTypeDef",
    ) -> "dc_td.FunctionEventInvokeConfigResponse":
        return dc_td.FunctionEventInvokeConfigResponse.make_one(res)

    def update_function_url_config(
        self,
        res: "bs_td.UpdateFunctionUrlConfigResponseTypeDef",
    ) -> "dc_td.UpdateFunctionUrlConfigResponse":
        return dc_td.UpdateFunctionUrlConfigResponse.make_one(res)


lambda_caster = LAMBDACaster()
