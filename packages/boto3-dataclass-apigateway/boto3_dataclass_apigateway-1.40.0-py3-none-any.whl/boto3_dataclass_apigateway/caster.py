# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apigateway import type_defs as bs_td


class APIGATEWAYCaster:

    def create_api_key(
        self,
        res: "bs_td.ApiKeyResponseTypeDef",
    ) -> "dc_td.ApiKeyResponse":
        return dc_td.ApiKeyResponse.make_one(res)

    def create_authorizer(
        self,
        res: "bs_td.AuthorizerResponseTypeDef",
    ) -> "dc_td.AuthorizerResponse":
        return dc_td.AuthorizerResponse.make_one(res)

    def create_base_path_mapping(
        self,
        res: "bs_td.BasePathMappingResponseTypeDef",
    ) -> "dc_td.BasePathMappingResponse":
        return dc_td.BasePathMappingResponse.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.DeploymentResponseTypeDef",
    ) -> "dc_td.DeploymentResponse":
        return dc_td.DeploymentResponse.make_one(res)

    def create_documentation_part(
        self,
        res: "bs_td.DocumentationPartResponseTypeDef",
    ) -> "dc_td.DocumentationPartResponse":
        return dc_td.DocumentationPartResponse.make_one(res)

    def create_documentation_version(
        self,
        res: "bs_td.DocumentationVersionResponseTypeDef",
    ) -> "dc_td.DocumentationVersionResponse":
        return dc_td.DocumentationVersionResponse.make_one(res)

    def create_domain_name(
        self,
        res: "bs_td.DomainNameResponseTypeDef",
    ) -> "dc_td.DomainNameResponse":
        return dc_td.DomainNameResponse.make_one(res)

    def create_domain_name_access_association(
        self,
        res: "bs_td.DomainNameAccessAssociationResponseTypeDef",
    ) -> "dc_td.DomainNameAccessAssociationResponse":
        return dc_td.DomainNameAccessAssociationResponse.make_one(res)

    def create_model(
        self,
        res: "bs_td.ModelResponseTypeDef",
    ) -> "dc_td.ModelResponse":
        return dc_td.ModelResponse.make_one(res)

    def create_request_validator(
        self,
        res: "bs_td.RequestValidatorResponseTypeDef",
    ) -> "dc_td.RequestValidatorResponse":
        return dc_td.RequestValidatorResponse.make_one(res)

    def create_resource(
        self,
        res: "bs_td.ResourceResponseTypeDef",
    ) -> "dc_td.ResourceResponse":
        return dc_td.ResourceResponse.make_one(res)

    def create_rest_api(
        self,
        res: "bs_td.RestApiResponseTypeDef",
    ) -> "dc_td.RestApiResponse":
        return dc_td.RestApiResponse.make_one(res)

    def create_stage(
        self,
        res: "bs_td.StageResponseTypeDef",
    ) -> "dc_td.StageResponse":
        return dc_td.StageResponse.make_one(res)

    def create_usage_plan(
        self,
        res: "bs_td.UsagePlanResponseTypeDef",
    ) -> "dc_td.UsagePlanResponse":
        return dc_td.UsagePlanResponse.make_one(res)

    def create_usage_plan_key(
        self,
        res: "bs_td.UsagePlanKeyResponseTypeDef",
    ) -> "dc_td.UsagePlanKeyResponse":
        return dc_td.UsagePlanKeyResponse.make_one(res)

    def create_vpc_link(
        self,
        res: "bs_td.VpcLinkResponseTypeDef",
    ) -> "dc_td.VpcLinkResponse":
        return dc_td.VpcLinkResponse.make_one(res)

    def delete_api_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_authorizer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_base_path_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_client_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_deployment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_documentation_part(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_documentation_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_domain_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_domain_name_access_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_gateway_response(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_integration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_integration_response(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_method(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_method_response(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_request_validator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_rest_api(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stage(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_usage_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_usage_plan_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vpc_link(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def flush_stage_authorizers_cache(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def flush_stage_cache(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def generate_client_certificate(
        self,
        res: "bs_td.ClientCertificateResponseTypeDef",
    ) -> "dc_td.ClientCertificateResponse":
        return dc_td.ClientCertificateResponse.make_one(res)

    def get_account(
        self,
        res: "bs_td.AccountTypeDef",
    ) -> "dc_td.Account":
        return dc_td.Account.make_one(res)

    def get_api_key(
        self,
        res: "bs_td.ApiKeyResponseTypeDef",
    ) -> "dc_td.ApiKeyResponse":
        return dc_td.ApiKeyResponse.make_one(res)

    def get_api_keys(
        self,
        res: "bs_td.ApiKeysTypeDef",
    ) -> "dc_td.ApiKeys":
        return dc_td.ApiKeys.make_one(res)

    def get_authorizer(
        self,
        res: "bs_td.AuthorizerResponseTypeDef",
    ) -> "dc_td.AuthorizerResponse":
        return dc_td.AuthorizerResponse.make_one(res)

    def get_authorizers(
        self,
        res: "bs_td.AuthorizersTypeDef",
    ) -> "dc_td.Authorizers":
        return dc_td.Authorizers.make_one(res)

    def get_base_path_mapping(
        self,
        res: "bs_td.BasePathMappingResponseTypeDef",
    ) -> "dc_td.BasePathMappingResponse":
        return dc_td.BasePathMappingResponse.make_one(res)

    def get_base_path_mappings(
        self,
        res: "bs_td.BasePathMappingsTypeDef",
    ) -> "dc_td.BasePathMappings":
        return dc_td.BasePathMappings.make_one(res)

    def get_client_certificate(
        self,
        res: "bs_td.ClientCertificateResponseTypeDef",
    ) -> "dc_td.ClientCertificateResponse":
        return dc_td.ClientCertificateResponse.make_one(res)

    def get_client_certificates(
        self,
        res: "bs_td.ClientCertificatesTypeDef",
    ) -> "dc_td.ClientCertificates":
        return dc_td.ClientCertificates.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.DeploymentResponseTypeDef",
    ) -> "dc_td.DeploymentResponse":
        return dc_td.DeploymentResponse.make_one(res)

    def get_deployments(
        self,
        res: "bs_td.DeploymentsTypeDef",
    ) -> "dc_td.Deployments":
        return dc_td.Deployments.make_one(res)

    def get_documentation_part(
        self,
        res: "bs_td.DocumentationPartResponseTypeDef",
    ) -> "dc_td.DocumentationPartResponse":
        return dc_td.DocumentationPartResponse.make_one(res)

    def get_documentation_parts(
        self,
        res: "bs_td.DocumentationPartsTypeDef",
    ) -> "dc_td.DocumentationParts":
        return dc_td.DocumentationParts.make_one(res)

    def get_documentation_version(
        self,
        res: "bs_td.DocumentationVersionResponseTypeDef",
    ) -> "dc_td.DocumentationVersionResponse":
        return dc_td.DocumentationVersionResponse.make_one(res)

    def get_documentation_versions(
        self,
        res: "bs_td.DocumentationVersionsTypeDef",
    ) -> "dc_td.DocumentationVersions":
        return dc_td.DocumentationVersions.make_one(res)

    def get_domain_name(
        self,
        res: "bs_td.DomainNameResponseTypeDef",
    ) -> "dc_td.DomainNameResponse":
        return dc_td.DomainNameResponse.make_one(res)

    def get_domain_name_access_associations(
        self,
        res: "bs_td.DomainNameAccessAssociationsTypeDef",
    ) -> "dc_td.DomainNameAccessAssociations":
        return dc_td.DomainNameAccessAssociations.make_one(res)

    def get_domain_names(
        self,
        res: "bs_td.DomainNamesTypeDef",
    ) -> "dc_td.DomainNames":
        return dc_td.DomainNames.make_one(res)

    def get_export(
        self,
        res: "bs_td.ExportResponseTypeDef",
    ) -> "dc_td.ExportResponse":
        return dc_td.ExportResponse.make_one(res)

    def get_gateway_response(
        self,
        res: "bs_td.GatewayResponseResponseTypeDef",
    ) -> "dc_td.GatewayResponseResponse":
        return dc_td.GatewayResponseResponse.make_one(res)

    def get_gateway_responses(
        self,
        res: "bs_td.GatewayResponsesTypeDef",
    ) -> "dc_td.GatewayResponses":
        return dc_td.GatewayResponses.make_one(res)

    def get_integration(
        self,
        res: "bs_td.IntegrationResponseExtraTypeDef",
    ) -> "dc_td.IntegrationResponseExtra":
        return dc_td.IntegrationResponseExtra.make_one(res)

    def get_integration_response(
        self,
        res: "bs_td.IntegrationResponseResponseTypeDef",
    ) -> "dc_td.IntegrationResponseResponse":
        return dc_td.IntegrationResponseResponse.make_one(res)

    def get_method(
        self,
        res: "bs_td.MethodResponseExtraTypeDef",
    ) -> "dc_td.MethodResponseExtra":
        return dc_td.MethodResponseExtra.make_one(res)

    def get_method_response(
        self,
        res: "bs_td.MethodResponseResponseTypeDef",
    ) -> "dc_td.MethodResponseResponse":
        return dc_td.MethodResponseResponse.make_one(res)

    def get_model(
        self,
        res: "bs_td.ModelResponseTypeDef",
    ) -> "dc_td.ModelResponse":
        return dc_td.ModelResponse.make_one(res)

    def get_model_template(
        self,
        res: "bs_td.TemplateTypeDef",
    ) -> "dc_td.Template":
        return dc_td.Template.make_one(res)

    def get_models(
        self,
        res: "bs_td.ModelsTypeDef",
    ) -> "dc_td.Models":
        return dc_td.Models.make_one(res)

    def get_request_validator(
        self,
        res: "bs_td.RequestValidatorResponseTypeDef",
    ) -> "dc_td.RequestValidatorResponse":
        return dc_td.RequestValidatorResponse.make_one(res)

    def get_request_validators(
        self,
        res: "bs_td.RequestValidatorsTypeDef",
    ) -> "dc_td.RequestValidators":
        return dc_td.RequestValidators.make_one(res)

    def get_resource(
        self,
        res: "bs_td.ResourceResponseTypeDef",
    ) -> "dc_td.ResourceResponse":
        return dc_td.ResourceResponse.make_one(res)

    def get_resources(
        self,
        res: "bs_td.ResourcesTypeDef",
    ) -> "dc_td.Resources":
        return dc_td.Resources.make_one(res)

    def get_rest_api(
        self,
        res: "bs_td.RestApiResponseTypeDef",
    ) -> "dc_td.RestApiResponse":
        return dc_td.RestApiResponse.make_one(res)

    def get_rest_apis(
        self,
        res: "bs_td.RestApisTypeDef",
    ) -> "dc_td.RestApis":
        return dc_td.RestApis.make_one(res)

    def get_sdk(
        self,
        res: "bs_td.SdkResponseTypeDef",
    ) -> "dc_td.SdkResponse":
        return dc_td.SdkResponse.make_one(res)

    def get_sdk_type(
        self,
        res: "bs_td.SdkTypeResponseTypeDef",
    ) -> "dc_td.SdkTypeResponse":
        return dc_td.SdkTypeResponse.make_one(res)

    def get_sdk_types(
        self,
        res: "bs_td.SdkTypesTypeDef",
    ) -> "dc_td.SdkTypes":
        return dc_td.SdkTypes.make_one(res)

    def get_stage(
        self,
        res: "bs_td.StageResponseTypeDef",
    ) -> "dc_td.StageResponse":
        return dc_td.StageResponse.make_one(res)

    def get_stages(
        self,
        res: "bs_td.StagesTypeDef",
    ) -> "dc_td.Stages":
        return dc_td.Stages.make_one(res)

    def get_tags(
        self,
        res: "bs_td.TagsTypeDef",
    ) -> "dc_td.Tags":
        return dc_td.Tags.make_one(res)

    def get_usage(
        self,
        res: "bs_td.UsageTypeDef",
    ) -> "dc_td.Usage":
        return dc_td.Usage.make_one(res)

    def get_usage_plan(
        self,
        res: "bs_td.UsagePlanResponseTypeDef",
    ) -> "dc_td.UsagePlanResponse":
        return dc_td.UsagePlanResponse.make_one(res)

    def get_usage_plan_key(
        self,
        res: "bs_td.UsagePlanKeyResponseTypeDef",
    ) -> "dc_td.UsagePlanKeyResponse":
        return dc_td.UsagePlanKeyResponse.make_one(res)

    def get_usage_plan_keys(
        self,
        res: "bs_td.UsagePlanKeysTypeDef",
    ) -> "dc_td.UsagePlanKeys":
        return dc_td.UsagePlanKeys.make_one(res)

    def get_usage_plans(
        self,
        res: "bs_td.UsagePlansTypeDef",
    ) -> "dc_td.UsagePlans":
        return dc_td.UsagePlans.make_one(res)

    def get_vpc_link(
        self,
        res: "bs_td.VpcLinkResponseTypeDef",
    ) -> "dc_td.VpcLinkResponse":
        return dc_td.VpcLinkResponse.make_one(res)

    def get_vpc_links(
        self,
        res: "bs_td.VpcLinksTypeDef",
    ) -> "dc_td.VpcLinks":
        return dc_td.VpcLinks.make_one(res)

    def import_api_keys(
        self,
        res: "bs_td.ApiKeyIdsTypeDef",
    ) -> "dc_td.ApiKeyIds":
        return dc_td.ApiKeyIds.make_one(res)

    def import_documentation_parts(
        self,
        res: "bs_td.DocumentationPartIdsTypeDef",
    ) -> "dc_td.DocumentationPartIds":
        return dc_td.DocumentationPartIds.make_one(res)

    def import_rest_api(
        self,
        res: "bs_td.RestApiResponseTypeDef",
    ) -> "dc_td.RestApiResponse":
        return dc_td.RestApiResponse.make_one(res)

    def put_gateway_response(
        self,
        res: "bs_td.GatewayResponseResponseTypeDef",
    ) -> "dc_td.GatewayResponseResponse":
        return dc_td.GatewayResponseResponse.make_one(res)

    def put_integration(
        self,
        res: "bs_td.IntegrationResponseExtraTypeDef",
    ) -> "dc_td.IntegrationResponseExtra":
        return dc_td.IntegrationResponseExtra.make_one(res)

    def put_integration_response(
        self,
        res: "bs_td.IntegrationResponseResponseTypeDef",
    ) -> "dc_td.IntegrationResponseResponse":
        return dc_td.IntegrationResponseResponse.make_one(res)

    def put_method(
        self,
        res: "bs_td.MethodResponseExtraTypeDef",
    ) -> "dc_td.MethodResponseExtra":
        return dc_td.MethodResponseExtra.make_one(res)

    def put_method_response(
        self,
        res: "bs_td.MethodResponseResponseTypeDef",
    ) -> "dc_td.MethodResponseResponse":
        return dc_td.MethodResponseResponse.make_one(res)

    def put_rest_api(
        self,
        res: "bs_td.RestApiResponseTypeDef",
    ) -> "dc_td.RestApiResponse":
        return dc_td.RestApiResponse.make_one(res)

    def reject_domain_name_access_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def test_invoke_authorizer(
        self,
        res: "bs_td.TestInvokeAuthorizerResponseTypeDef",
    ) -> "dc_td.TestInvokeAuthorizerResponse":
        return dc_td.TestInvokeAuthorizerResponse.make_one(res)

    def test_invoke_method(
        self,
        res: "bs_td.TestInvokeMethodResponseTypeDef",
    ) -> "dc_td.TestInvokeMethodResponse":
        return dc_td.TestInvokeMethodResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_account(
        self,
        res: "bs_td.AccountTypeDef",
    ) -> "dc_td.Account":
        return dc_td.Account.make_one(res)

    def update_api_key(
        self,
        res: "bs_td.ApiKeyResponseTypeDef",
    ) -> "dc_td.ApiKeyResponse":
        return dc_td.ApiKeyResponse.make_one(res)

    def update_authorizer(
        self,
        res: "bs_td.AuthorizerResponseTypeDef",
    ) -> "dc_td.AuthorizerResponse":
        return dc_td.AuthorizerResponse.make_one(res)

    def update_base_path_mapping(
        self,
        res: "bs_td.BasePathMappingResponseTypeDef",
    ) -> "dc_td.BasePathMappingResponse":
        return dc_td.BasePathMappingResponse.make_one(res)

    def update_client_certificate(
        self,
        res: "bs_td.ClientCertificateResponseTypeDef",
    ) -> "dc_td.ClientCertificateResponse":
        return dc_td.ClientCertificateResponse.make_one(res)

    def update_deployment(
        self,
        res: "bs_td.DeploymentResponseTypeDef",
    ) -> "dc_td.DeploymentResponse":
        return dc_td.DeploymentResponse.make_one(res)

    def update_documentation_part(
        self,
        res: "bs_td.DocumentationPartResponseTypeDef",
    ) -> "dc_td.DocumentationPartResponse":
        return dc_td.DocumentationPartResponse.make_one(res)

    def update_documentation_version(
        self,
        res: "bs_td.DocumentationVersionResponseTypeDef",
    ) -> "dc_td.DocumentationVersionResponse":
        return dc_td.DocumentationVersionResponse.make_one(res)

    def update_domain_name(
        self,
        res: "bs_td.DomainNameResponseTypeDef",
    ) -> "dc_td.DomainNameResponse":
        return dc_td.DomainNameResponse.make_one(res)

    def update_gateway_response(
        self,
        res: "bs_td.GatewayResponseResponseTypeDef",
    ) -> "dc_td.GatewayResponseResponse":
        return dc_td.GatewayResponseResponse.make_one(res)

    def update_integration(
        self,
        res: "bs_td.IntegrationResponseExtraTypeDef",
    ) -> "dc_td.IntegrationResponseExtra":
        return dc_td.IntegrationResponseExtra.make_one(res)

    def update_integration_response(
        self,
        res: "bs_td.IntegrationResponseResponseTypeDef",
    ) -> "dc_td.IntegrationResponseResponse":
        return dc_td.IntegrationResponseResponse.make_one(res)

    def update_method(
        self,
        res: "bs_td.MethodResponseExtraTypeDef",
    ) -> "dc_td.MethodResponseExtra":
        return dc_td.MethodResponseExtra.make_one(res)

    def update_method_response(
        self,
        res: "bs_td.MethodResponseResponseTypeDef",
    ) -> "dc_td.MethodResponseResponse":
        return dc_td.MethodResponseResponse.make_one(res)

    def update_model(
        self,
        res: "bs_td.ModelResponseTypeDef",
    ) -> "dc_td.ModelResponse":
        return dc_td.ModelResponse.make_one(res)

    def update_request_validator(
        self,
        res: "bs_td.RequestValidatorResponseTypeDef",
    ) -> "dc_td.RequestValidatorResponse":
        return dc_td.RequestValidatorResponse.make_one(res)

    def update_resource(
        self,
        res: "bs_td.ResourceResponseTypeDef",
    ) -> "dc_td.ResourceResponse":
        return dc_td.ResourceResponse.make_one(res)

    def update_rest_api(
        self,
        res: "bs_td.RestApiResponseTypeDef",
    ) -> "dc_td.RestApiResponse":
        return dc_td.RestApiResponse.make_one(res)

    def update_stage(
        self,
        res: "bs_td.StageResponseTypeDef",
    ) -> "dc_td.StageResponse":
        return dc_td.StageResponse.make_one(res)

    def update_usage(
        self,
        res: "bs_td.UsageTypeDef",
    ) -> "dc_td.Usage":
        return dc_td.Usage.make_one(res)

    def update_usage_plan(
        self,
        res: "bs_td.UsagePlanResponseTypeDef",
    ) -> "dc_td.UsagePlanResponse":
        return dc_td.UsagePlanResponse.make_one(res)

    def update_vpc_link(
        self,
        res: "bs_td.VpcLinkResponseTypeDef",
    ) -> "dc_td.VpcLinkResponse":
        return dc_td.VpcLinkResponse.make_one(res)


apigateway_caster = APIGATEWAYCaster()
