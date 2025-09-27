# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agentcore_control import type_defs as bs_td


class BEDROCK_AGENTCORE_CONTROLCaster:

    def create_agent_runtime(
        self,
        res: "bs_td.CreateAgentRuntimeResponseTypeDef",
    ) -> "dc_td.CreateAgentRuntimeResponse":
        return dc_td.CreateAgentRuntimeResponse.make_one(res)

    def create_agent_runtime_endpoint(
        self,
        res: "bs_td.CreateAgentRuntimeEndpointResponseTypeDef",
    ) -> "dc_td.CreateAgentRuntimeEndpointResponse":
        return dc_td.CreateAgentRuntimeEndpointResponse.make_one(res)

    def create_api_key_credential_provider(
        self,
        res: "bs_td.CreateApiKeyCredentialProviderResponseTypeDef",
    ) -> "dc_td.CreateApiKeyCredentialProviderResponse":
        return dc_td.CreateApiKeyCredentialProviderResponse.make_one(res)

    def create_browser(
        self,
        res: "bs_td.CreateBrowserResponseTypeDef",
    ) -> "dc_td.CreateBrowserResponse":
        return dc_td.CreateBrowserResponse.make_one(res)

    def create_code_interpreter(
        self,
        res: "bs_td.CreateCodeInterpreterResponseTypeDef",
    ) -> "dc_td.CreateCodeInterpreterResponse":
        return dc_td.CreateCodeInterpreterResponse.make_one(res)

    def create_gateway(
        self,
        res: "bs_td.CreateGatewayResponseTypeDef",
    ) -> "dc_td.CreateGatewayResponse":
        return dc_td.CreateGatewayResponse.make_one(res)

    def create_gateway_target(
        self,
        res: "bs_td.CreateGatewayTargetResponseTypeDef",
    ) -> "dc_td.CreateGatewayTargetResponse":
        return dc_td.CreateGatewayTargetResponse.make_one(res)

    def create_memory(
        self,
        res: "bs_td.CreateMemoryOutputTypeDef",
    ) -> "dc_td.CreateMemoryOutput":
        return dc_td.CreateMemoryOutput.make_one(res)

    def create_oauth2_credential_provider(
        self,
        res: "bs_td.CreateOauth2CredentialProviderResponseTypeDef",
    ) -> "dc_td.CreateOauth2CredentialProviderResponse":
        return dc_td.CreateOauth2CredentialProviderResponse.make_one(res)

    def create_workload_identity(
        self,
        res: "bs_td.CreateWorkloadIdentityResponseTypeDef",
    ) -> "dc_td.CreateWorkloadIdentityResponse":
        return dc_td.CreateWorkloadIdentityResponse.make_one(res)

    def delete_agent_runtime(
        self,
        res: "bs_td.DeleteAgentRuntimeResponseTypeDef",
    ) -> "dc_td.DeleteAgentRuntimeResponse":
        return dc_td.DeleteAgentRuntimeResponse.make_one(res)

    def delete_agent_runtime_endpoint(
        self,
        res: "bs_td.DeleteAgentRuntimeEndpointResponseTypeDef",
    ) -> "dc_td.DeleteAgentRuntimeEndpointResponse":
        return dc_td.DeleteAgentRuntimeEndpointResponse.make_one(res)

    def delete_browser(
        self,
        res: "bs_td.DeleteBrowserResponseTypeDef",
    ) -> "dc_td.DeleteBrowserResponse":
        return dc_td.DeleteBrowserResponse.make_one(res)

    def delete_code_interpreter(
        self,
        res: "bs_td.DeleteCodeInterpreterResponseTypeDef",
    ) -> "dc_td.DeleteCodeInterpreterResponse":
        return dc_td.DeleteCodeInterpreterResponse.make_one(res)

    def delete_gateway(
        self,
        res: "bs_td.DeleteGatewayResponseTypeDef",
    ) -> "dc_td.DeleteGatewayResponse":
        return dc_td.DeleteGatewayResponse.make_one(res)

    def delete_gateway_target(
        self,
        res: "bs_td.DeleteGatewayTargetResponseTypeDef",
    ) -> "dc_td.DeleteGatewayTargetResponse":
        return dc_td.DeleteGatewayTargetResponse.make_one(res)

    def delete_memory(
        self,
        res: "bs_td.DeleteMemoryOutputTypeDef",
    ) -> "dc_td.DeleteMemoryOutput":
        return dc_td.DeleteMemoryOutput.make_one(res)

    def get_agent_runtime(
        self,
        res: "bs_td.GetAgentRuntimeResponseTypeDef",
    ) -> "dc_td.GetAgentRuntimeResponse":
        return dc_td.GetAgentRuntimeResponse.make_one(res)

    def get_agent_runtime_endpoint(
        self,
        res: "bs_td.GetAgentRuntimeEndpointResponseTypeDef",
    ) -> "dc_td.GetAgentRuntimeEndpointResponse":
        return dc_td.GetAgentRuntimeEndpointResponse.make_one(res)

    def get_api_key_credential_provider(
        self,
        res: "bs_td.GetApiKeyCredentialProviderResponseTypeDef",
    ) -> "dc_td.GetApiKeyCredentialProviderResponse":
        return dc_td.GetApiKeyCredentialProviderResponse.make_one(res)

    def get_browser(
        self,
        res: "bs_td.GetBrowserResponseTypeDef",
    ) -> "dc_td.GetBrowserResponse":
        return dc_td.GetBrowserResponse.make_one(res)

    def get_code_interpreter(
        self,
        res: "bs_td.GetCodeInterpreterResponseTypeDef",
    ) -> "dc_td.GetCodeInterpreterResponse":
        return dc_td.GetCodeInterpreterResponse.make_one(res)

    def get_gateway(
        self,
        res: "bs_td.GetGatewayResponseTypeDef",
    ) -> "dc_td.GetGatewayResponse":
        return dc_td.GetGatewayResponse.make_one(res)

    def get_gateway_target(
        self,
        res: "bs_td.GetGatewayTargetResponseTypeDef",
    ) -> "dc_td.GetGatewayTargetResponse":
        return dc_td.GetGatewayTargetResponse.make_one(res)

    def get_memory(
        self,
        res: "bs_td.GetMemoryOutputTypeDef",
    ) -> "dc_td.GetMemoryOutput":
        return dc_td.GetMemoryOutput.make_one(res)

    def get_oauth2_credential_provider(
        self,
        res: "bs_td.GetOauth2CredentialProviderResponseTypeDef",
    ) -> "dc_td.GetOauth2CredentialProviderResponse":
        return dc_td.GetOauth2CredentialProviderResponse.make_one(res)

    def get_token_vault(
        self,
        res: "bs_td.GetTokenVaultResponseTypeDef",
    ) -> "dc_td.GetTokenVaultResponse":
        return dc_td.GetTokenVaultResponse.make_one(res)

    def get_workload_identity(
        self,
        res: "bs_td.GetWorkloadIdentityResponseTypeDef",
    ) -> "dc_td.GetWorkloadIdentityResponse":
        return dc_td.GetWorkloadIdentityResponse.make_one(res)

    def list_agent_runtime_endpoints(
        self,
        res: "bs_td.ListAgentRuntimeEndpointsResponseTypeDef",
    ) -> "dc_td.ListAgentRuntimeEndpointsResponse":
        return dc_td.ListAgentRuntimeEndpointsResponse.make_one(res)

    def list_agent_runtime_versions(
        self,
        res: "bs_td.ListAgentRuntimeVersionsResponseTypeDef",
    ) -> "dc_td.ListAgentRuntimeVersionsResponse":
        return dc_td.ListAgentRuntimeVersionsResponse.make_one(res)

    def list_agent_runtimes(
        self,
        res: "bs_td.ListAgentRuntimesResponseTypeDef",
    ) -> "dc_td.ListAgentRuntimesResponse":
        return dc_td.ListAgentRuntimesResponse.make_one(res)

    def list_api_key_credential_providers(
        self,
        res: "bs_td.ListApiKeyCredentialProvidersResponseTypeDef",
    ) -> "dc_td.ListApiKeyCredentialProvidersResponse":
        return dc_td.ListApiKeyCredentialProvidersResponse.make_one(res)

    def list_browsers(
        self,
        res: "bs_td.ListBrowsersResponseTypeDef",
    ) -> "dc_td.ListBrowsersResponse":
        return dc_td.ListBrowsersResponse.make_one(res)

    def list_code_interpreters(
        self,
        res: "bs_td.ListCodeInterpretersResponseTypeDef",
    ) -> "dc_td.ListCodeInterpretersResponse":
        return dc_td.ListCodeInterpretersResponse.make_one(res)

    def list_gateway_targets(
        self,
        res: "bs_td.ListGatewayTargetsResponseTypeDef",
    ) -> "dc_td.ListGatewayTargetsResponse":
        return dc_td.ListGatewayTargetsResponse.make_one(res)

    def list_gateways(
        self,
        res: "bs_td.ListGatewaysResponseTypeDef",
    ) -> "dc_td.ListGatewaysResponse":
        return dc_td.ListGatewaysResponse.make_one(res)

    def list_memories(
        self,
        res: "bs_td.ListMemoriesOutputTypeDef",
    ) -> "dc_td.ListMemoriesOutput":
        return dc_td.ListMemoriesOutput.make_one(res)

    def list_oauth2_credential_providers(
        self,
        res: "bs_td.ListOauth2CredentialProvidersResponseTypeDef",
    ) -> "dc_td.ListOauth2CredentialProvidersResponse":
        return dc_td.ListOauth2CredentialProvidersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_workload_identities(
        self,
        res: "bs_td.ListWorkloadIdentitiesResponseTypeDef",
    ) -> "dc_td.ListWorkloadIdentitiesResponse":
        return dc_td.ListWorkloadIdentitiesResponse.make_one(res)

    def set_token_vault_cmk(
        self,
        res: "bs_td.SetTokenVaultCMKResponseTypeDef",
    ) -> "dc_td.SetTokenVaultCMKResponse":
        return dc_td.SetTokenVaultCMKResponse.make_one(res)

    def update_agent_runtime(
        self,
        res: "bs_td.UpdateAgentRuntimeResponseTypeDef",
    ) -> "dc_td.UpdateAgentRuntimeResponse":
        return dc_td.UpdateAgentRuntimeResponse.make_one(res)

    def update_agent_runtime_endpoint(
        self,
        res: "bs_td.UpdateAgentRuntimeEndpointResponseTypeDef",
    ) -> "dc_td.UpdateAgentRuntimeEndpointResponse":
        return dc_td.UpdateAgentRuntimeEndpointResponse.make_one(res)

    def update_api_key_credential_provider(
        self,
        res: "bs_td.UpdateApiKeyCredentialProviderResponseTypeDef",
    ) -> "dc_td.UpdateApiKeyCredentialProviderResponse":
        return dc_td.UpdateApiKeyCredentialProviderResponse.make_one(res)

    def update_gateway(
        self,
        res: "bs_td.UpdateGatewayResponseTypeDef",
    ) -> "dc_td.UpdateGatewayResponse":
        return dc_td.UpdateGatewayResponse.make_one(res)

    def update_gateway_target(
        self,
        res: "bs_td.UpdateGatewayTargetResponseTypeDef",
    ) -> "dc_td.UpdateGatewayTargetResponse":
        return dc_td.UpdateGatewayTargetResponse.make_one(res)

    def update_memory(
        self,
        res: "bs_td.UpdateMemoryOutputTypeDef",
    ) -> "dc_td.UpdateMemoryOutput":
        return dc_td.UpdateMemoryOutput.make_one(res)

    def update_oauth2_credential_provider(
        self,
        res: "bs_td.UpdateOauth2CredentialProviderResponseTypeDef",
    ) -> "dc_td.UpdateOauth2CredentialProviderResponse":
        return dc_td.UpdateOauth2CredentialProviderResponse.make_one(res)

    def update_workload_identity(
        self,
        res: "bs_td.UpdateWorkloadIdentityResponseTypeDef",
    ) -> "dc_td.UpdateWorkloadIdentityResponse":
        return dc_td.UpdateWorkloadIdentityResponse.make_one(res)


bedrock_agentcore_control_caster = BEDROCK_AGENTCORE_CONTROLCaster()
