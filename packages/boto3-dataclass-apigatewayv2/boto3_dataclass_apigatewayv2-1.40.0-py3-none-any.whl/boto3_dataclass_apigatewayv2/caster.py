# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apigatewayv2 import type_defs as bs_td


class APIGATEWAYV2Caster:

    def create_api(
        self,
        res: "bs_td.CreateApiResponseTypeDef",
    ) -> "dc_td.CreateApiResponse":
        return dc_td.CreateApiResponse.make_one(res)

    def create_api_mapping(
        self,
        res: "bs_td.CreateApiMappingResponseTypeDef",
    ) -> "dc_td.CreateApiMappingResponse":
        return dc_td.CreateApiMappingResponse.make_one(res)

    def create_authorizer(
        self,
        res: "bs_td.CreateAuthorizerResponseTypeDef",
    ) -> "dc_td.CreateAuthorizerResponse":
        return dc_td.CreateAuthorizerResponse.make_one(res)

    def create_deployment(
        self,
        res: "bs_td.CreateDeploymentResponseTypeDef",
    ) -> "dc_td.CreateDeploymentResponse":
        return dc_td.CreateDeploymentResponse.make_one(res)

    def create_domain_name(
        self,
        res: "bs_td.CreateDomainNameResponseTypeDef",
    ) -> "dc_td.CreateDomainNameResponse":
        return dc_td.CreateDomainNameResponse.make_one(res)

    def create_integration(
        self,
        res: "bs_td.CreateIntegrationResultTypeDef",
    ) -> "dc_td.CreateIntegrationResult":
        return dc_td.CreateIntegrationResult.make_one(res)

    def create_integration_response(
        self,
        res: "bs_td.CreateIntegrationResponseResponseTypeDef",
    ) -> "dc_td.CreateIntegrationResponseResponse":
        return dc_td.CreateIntegrationResponseResponse.make_one(res)

    def create_model(
        self,
        res: "bs_td.CreateModelResponseTypeDef",
    ) -> "dc_td.CreateModelResponse":
        return dc_td.CreateModelResponse.make_one(res)

    def create_route(
        self,
        res: "bs_td.CreateRouteResultTypeDef",
    ) -> "dc_td.CreateRouteResult":
        return dc_td.CreateRouteResult.make_one(res)

    def create_route_response(
        self,
        res: "bs_td.CreateRouteResponseResponseTypeDef",
    ) -> "dc_td.CreateRouteResponseResponse":
        return dc_td.CreateRouteResponseResponse.make_one(res)

    def create_routing_rule(
        self,
        res: "bs_td.CreateRoutingRuleResponseTypeDef",
    ) -> "dc_td.CreateRoutingRuleResponse":
        return dc_td.CreateRoutingRuleResponse.make_one(res)

    def create_stage(
        self,
        res: "bs_td.CreateStageResponseTypeDef",
    ) -> "dc_td.CreateStageResponse":
        return dc_td.CreateStageResponse.make_one(res)

    def create_vpc_link(
        self,
        res: "bs_td.CreateVpcLinkResponseTypeDef",
    ) -> "dc_td.CreateVpcLinkResponse":
        return dc_td.CreateVpcLinkResponse.make_one(res)

    def delete_access_log_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_api(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_api_mapping(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_authorizer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cors_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_deployment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_domain_name(
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

    def delete_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_route(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_route_request_parameter(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_route_response(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_route_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_routing_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stage(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def export_api(
        self,
        res: "bs_td.ExportApiResponseTypeDef",
    ) -> "dc_td.ExportApiResponse":
        return dc_td.ExportApiResponse.make_one(res)

    def reset_authorizers_cache(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_api(
        self,
        res: "bs_td.GetApiResponseTypeDef",
    ) -> "dc_td.GetApiResponse":
        return dc_td.GetApiResponse.make_one(res)

    def get_api_mapping(
        self,
        res: "bs_td.GetApiMappingResponseTypeDef",
    ) -> "dc_td.GetApiMappingResponse":
        return dc_td.GetApiMappingResponse.make_one(res)

    def get_api_mappings(
        self,
        res: "bs_td.GetApiMappingsResponseTypeDef",
    ) -> "dc_td.GetApiMappingsResponse":
        return dc_td.GetApiMappingsResponse.make_one(res)

    def get_apis(
        self,
        res: "bs_td.GetApisResponseTypeDef",
    ) -> "dc_td.GetApisResponse":
        return dc_td.GetApisResponse.make_one(res)

    def get_authorizer(
        self,
        res: "bs_td.GetAuthorizerResponseTypeDef",
    ) -> "dc_td.GetAuthorizerResponse":
        return dc_td.GetAuthorizerResponse.make_one(res)

    def get_authorizers(
        self,
        res: "bs_td.GetAuthorizersResponseTypeDef",
    ) -> "dc_td.GetAuthorizersResponse":
        return dc_td.GetAuthorizersResponse.make_one(res)

    def get_deployment(
        self,
        res: "bs_td.GetDeploymentResponseTypeDef",
    ) -> "dc_td.GetDeploymentResponse":
        return dc_td.GetDeploymentResponse.make_one(res)

    def get_deployments(
        self,
        res: "bs_td.GetDeploymentsResponseTypeDef",
    ) -> "dc_td.GetDeploymentsResponse":
        return dc_td.GetDeploymentsResponse.make_one(res)

    def get_domain_name(
        self,
        res: "bs_td.GetDomainNameResponseTypeDef",
    ) -> "dc_td.GetDomainNameResponse":
        return dc_td.GetDomainNameResponse.make_one(res)

    def get_domain_names(
        self,
        res: "bs_td.GetDomainNamesResponseTypeDef",
    ) -> "dc_td.GetDomainNamesResponse":
        return dc_td.GetDomainNamesResponse.make_one(res)

    def get_integration(
        self,
        res: "bs_td.GetIntegrationResultTypeDef",
    ) -> "dc_td.GetIntegrationResult":
        return dc_td.GetIntegrationResult.make_one(res)

    def get_integration_response(
        self,
        res: "bs_td.GetIntegrationResponseResponseTypeDef",
    ) -> "dc_td.GetIntegrationResponseResponse":
        return dc_td.GetIntegrationResponseResponse.make_one(res)

    def get_integration_responses(
        self,
        res: "bs_td.GetIntegrationResponsesResponseTypeDef",
    ) -> "dc_td.GetIntegrationResponsesResponse":
        return dc_td.GetIntegrationResponsesResponse.make_one(res)

    def get_integrations(
        self,
        res: "bs_td.GetIntegrationsResponseTypeDef",
    ) -> "dc_td.GetIntegrationsResponse":
        return dc_td.GetIntegrationsResponse.make_one(res)

    def get_model(
        self,
        res: "bs_td.GetModelResponseTypeDef",
    ) -> "dc_td.GetModelResponse":
        return dc_td.GetModelResponse.make_one(res)

    def get_model_template(
        self,
        res: "bs_td.GetModelTemplateResponseTypeDef",
    ) -> "dc_td.GetModelTemplateResponse":
        return dc_td.GetModelTemplateResponse.make_one(res)

    def get_models(
        self,
        res: "bs_td.GetModelsResponseTypeDef",
    ) -> "dc_td.GetModelsResponse":
        return dc_td.GetModelsResponse.make_one(res)

    def get_route(
        self,
        res: "bs_td.GetRouteResultTypeDef",
    ) -> "dc_td.GetRouteResult":
        return dc_td.GetRouteResult.make_one(res)

    def get_route_response(
        self,
        res: "bs_td.GetRouteResponseResponseTypeDef",
    ) -> "dc_td.GetRouteResponseResponse":
        return dc_td.GetRouteResponseResponse.make_one(res)

    def get_route_responses(
        self,
        res: "bs_td.GetRouteResponsesResponseTypeDef",
    ) -> "dc_td.GetRouteResponsesResponse":
        return dc_td.GetRouteResponsesResponse.make_one(res)

    def get_routes(
        self,
        res: "bs_td.GetRoutesResponseTypeDef",
    ) -> "dc_td.GetRoutesResponse":
        return dc_td.GetRoutesResponse.make_one(res)

    def get_routing_rule(
        self,
        res: "bs_td.GetRoutingRuleResponseTypeDef",
    ) -> "dc_td.GetRoutingRuleResponse":
        return dc_td.GetRoutingRuleResponse.make_one(res)

    def list_routing_rules(
        self,
        res: "bs_td.ListRoutingRulesResponseTypeDef",
    ) -> "dc_td.ListRoutingRulesResponse":
        return dc_td.ListRoutingRulesResponse.make_one(res)

    def get_stage(
        self,
        res: "bs_td.GetStageResponseTypeDef",
    ) -> "dc_td.GetStageResponse":
        return dc_td.GetStageResponse.make_one(res)

    def get_stages(
        self,
        res: "bs_td.GetStagesResponseTypeDef",
    ) -> "dc_td.GetStagesResponse":
        return dc_td.GetStagesResponse.make_one(res)

    def get_tags(
        self,
        res: "bs_td.GetTagsResponseTypeDef",
    ) -> "dc_td.GetTagsResponse":
        return dc_td.GetTagsResponse.make_one(res)

    def get_vpc_link(
        self,
        res: "bs_td.GetVpcLinkResponseTypeDef",
    ) -> "dc_td.GetVpcLinkResponse":
        return dc_td.GetVpcLinkResponse.make_one(res)

    def get_vpc_links(
        self,
        res: "bs_td.GetVpcLinksResponseTypeDef",
    ) -> "dc_td.GetVpcLinksResponse":
        return dc_td.GetVpcLinksResponse.make_one(res)

    def import_api(
        self,
        res: "bs_td.ImportApiResponseTypeDef",
    ) -> "dc_td.ImportApiResponse":
        return dc_td.ImportApiResponse.make_one(res)

    def put_routing_rule(
        self,
        res: "bs_td.PutRoutingRuleResponseTypeDef",
    ) -> "dc_td.PutRoutingRuleResponse":
        return dc_td.PutRoutingRuleResponse.make_one(res)

    def reimport_api(
        self,
        res: "bs_td.ReimportApiResponseTypeDef",
    ) -> "dc_td.ReimportApiResponse":
        return dc_td.ReimportApiResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_api(
        self,
        res: "bs_td.UpdateApiResponseTypeDef",
    ) -> "dc_td.UpdateApiResponse":
        return dc_td.UpdateApiResponse.make_one(res)

    def update_api_mapping(
        self,
        res: "bs_td.UpdateApiMappingResponseTypeDef",
    ) -> "dc_td.UpdateApiMappingResponse":
        return dc_td.UpdateApiMappingResponse.make_one(res)

    def update_authorizer(
        self,
        res: "bs_td.UpdateAuthorizerResponseTypeDef",
    ) -> "dc_td.UpdateAuthorizerResponse":
        return dc_td.UpdateAuthorizerResponse.make_one(res)

    def update_deployment(
        self,
        res: "bs_td.UpdateDeploymentResponseTypeDef",
    ) -> "dc_td.UpdateDeploymentResponse":
        return dc_td.UpdateDeploymentResponse.make_one(res)

    def update_domain_name(
        self,
        res: "bs_td.UpdateDomainNameResponseTypeDef",
    ) -> "dc_td.UpdateDomainNameResponse":
        return dc_td.UpdateDomainNameResponse.make_one(res)

    def update_integration(
        self,
        res: "bs_td.UpdateIntegrationResultTypeDef",
    ) -> "dc_td.UpdateIntegrationResult":
        return dc_td.UpdateIntegrationResult.make_one(res)

    def update_integration_response(
        self,
        res: "bs_td.UpdateIntegrationResponseResponseTypeDef",
    ) -> "dc_td.UpdateIntegrationResponseResponse":
        return dc_td.UpdateIntegrationResponseResponse.make_one(res)

    def update_model(
        self,
        res: "bs_td.UpdateModelResponseTypeDef",
    ) -> "dc_td.UpdateModelResponse":
        return dc_td.UpdateModelResponse.make_one(res)

    def update_route(
        self,
        res: "bs_td.UpdateRouteResultTypeDef",
    ) -> "dc_td.UpdateRouteResult":
        return dc_td.UpdateRouteResult.make_one(res)

    def update_route_response(
        self,
        res: "bs_td.UpdateRouteResponseResponseTypeDef",
    ) -> "dc_td.UpdateRouteResponseResponse":
        return dc_td.UpdateRouteResponseResponse.make_one(res)

    def update_stage(
        self,
        res: "bs_td.UpdateStageResponseTypeDef",
    ) -> "dc_td.UpdateStageResponse":
        return dc_td.UpdateStageResponse.make_one(res)

    def update_vpc_link(
        self,
        res: "bs_td.UpdateVpcLinkResponseTypeDef",
    ) -> "dc_td.UpdateVpcLinkResponse":
        return dc_td.UpdateVpcLinkResponse.make_one(res)


apigatewayv2_caster = APIGATEWAYV2Caster()
