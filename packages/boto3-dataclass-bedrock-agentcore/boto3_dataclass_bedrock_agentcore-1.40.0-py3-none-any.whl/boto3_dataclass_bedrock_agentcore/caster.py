# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agentcore import type_defs as bs_td


class BEDROCK_AGENTCORECaster:

    def create_event(
        self,
        res: "bs_td.CreateEventOutputTypeDef",
    ) -> "dc_td.CreateEventOutput":
        return dc_td.CreateEventOutput.make_one(res)

    def delete_event(
        self,
        res: "bs_td.DeleteEventOutputTypeDef",
    ) -> "dc_td.DeleteEventOutput":
        return dc_td.DeleteEventOutput.make_one(res)

    def delete_memory_record(
        self,
        res: "bs_td.DeleteMemoryRecordOutputTypeDef",
    ) -> "dc_td.DeleteMemoryRecordOutput":
        return dc_td.DeleteMemoryRecordOutput.make_one(res)

    def get_browser_session(
        self,
        res: "bs_td.GetBrowserSessionResponseTypeDef",
    ) -> "dc_td.GetBrowserSessionResponse":
        return dc_td.GetBrowserSessionResponse.make_one(res)

    def get_code_interpreter_session(
        self,
        res: "bs_td.GetCodeInterpreterSessionResponseTypeDef",
    ) -> "dc_td.GetCodeInterpreterSessionResponse":
        return dc_td.GetCodeInterpreterSessionResponse.make_one(res)

    def get_event(
        self,
        res: "bs_td.GetEventOutputTypeDef",
    ) -> "dc_td.GetEventOutput":
        return dc_td.GetEventOutput.make_one(res)

    def get_memory_record(
        self,
        res: "bs_td.GetMemoryRecordOutputTypeDef",
    ) -> "dc_td.GetMemoryRecordOutput":
        return dc_td.GetMemoryRecordOutput.make_one(res)

    def get_resource_api_key(
        self,
        res: "bs_td.GetResourceApiKeyResponseTypeDef",
    ) -> "dc_td.GetResourceApiKeyResponse":
        return dc_td.GetResourceApiKeyResponse.make_one(res)

    def get_resource_oauth2_token(
        self,
        res: "bs_td.GetResourceOauth2TokenResponseTypeDef",
    ) -> "dc_td.GetResourceOauth2TokenResponse":
        return dc_td.GetResourceOauth2TokenResponse.make_one(res)

    def get_workload_access_token(
        self,
        res: "bs_td.GetWorkloadAccessTokenResponseTypeDef",
    ) -> "dc_td.GetWorkloadAccessTokenResponse":
        return dc_td.GetWorkloadAccessTokenResponse.make_one(res)

    def get_workload_access_token_for_jwt(
        self,
        res: "bs_td.GetWorkloadAccessTokenForJWTResponseTypeDef",
    ) -> "dc_td.GetWorkloadAccessTokenForJWTResponse":
        return dc_td.GetWorkloadAccessTokenForJWTResponse.make_one(res)

    def get_workload_access_token_for_user_id(
        self,
        res: "bs_td.GetWorkloadAccessTokenForUserIdResponseTypeDef",
    ) -> "dc_td.GetWorkloadAccessTokenForUserIdResponse":
        return dc_td.GetWorkloadAccessTokenForUserIdResponse.make_one(res)

    def invoke_agent_runtime(
        self,
        res: "bs_td.InvokeAgentRuntimeResponseTypeDef",
    ) -> "dc_td.InvokeAgentRuntimeResponse":
        return dc_td.InvokeAgentRuntimeResponse.make_one(res)

    def invoke_code_interpreter(
        self,
        res: "bs_td.InvokeCodeInterpreterResponseTypeDef",
    ) -> "dc_td.InvokeCodeInterpreterResponse":
        return dc_td.InvokeCodeInterpreterResponse.make_one(res)

    def list_actors(
        self,
        res: "bs_td.ListActorsOutputTypeDef",
    ) -> "dc_td.ListActorsOutput":
        return dc_td.ListActorsOutput.make_one(res)

    def list_browser_sessions(
        self,
        res: "bs_td.ListBrowserSessionsResponseTypeDef",
    ) -> "dc_td.ListBrowserSessionsResponse":
        return dc_td.ListBrowserSessionsResponse.make_one(res)

    def list_code_interpreter_sessions(
        self,
        res: "bs_td.ListCodeInterpreterSessionsResponseTypeDef",
    ) -> "dc_td.ListCodeInterpreterSessionsResponse":
        return dc_td.ListCodeInterpreterSessionsResponse.make_one(res)

    def list_events(
        self,
        res: "bs_td.ListEventsOutputTypeDef",
    ) -> "dc_td.ListEventsOutput":
        return dc_td.ListEventsOutput.make_one(res)

    def list_memory_records(
        self,
        res: "bs_td.ListMemoryRecordsOutputTypeDef",
    ) -> "dc_td.ListMemoryRecordsOutput":
        return dc_td.ListMemoryRecordsOutput.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsOutputTypeDef",
    ) -> "dc_td.ListSessionsOutput":
        return dc_td.ListSessionsOutput.make_one(res)

    def retrieve_memory_records(
        self,
        res: "bs_td.RetrieveMemoryRecordsOutputTypeDef",
    ) -> "dc_td.RetrieveMemoryRecordsOutput":
        return dc_td.RetrieveMemoryRecordsOutput.make_one(res)

    def start_browser_session(
        self,
        res: "bs_td.StartBrowserSessionResponseTypeDef",
    ) -> "dc_td.StartBrowserSessionResponse":
        return dc_td.StartBrowserSessionResponse.make_one(res)

    def start_code_interpreter_session(
        self,
        res: "bs_td.StartCodeInterpreterSessionResponseTypeDef",
    ) -> "dc_td.StartCodeInterpreterSessionResponse":
        return dc_td.StartCodeInterpreterSessionResponse.make_one(res)

    def stop_browser_session(
        self,
        res: "bs_td.StopBrowserSessionResponseTypeDef",
    ) -> "dc_td.StopBrowserSessionResponse":
        return dc_td.StopBrowserSessionResponse.make_one(res)

    def stop_code_interpreter_session(
        self,
        res: "bs_td.StopCodeInterpreterSessionResponseTypeDef",
    ) -> "dc_td.StopCodeInterpreterSessionResponse":
        return dc_td.StopCodeInterpreterSessionResponse.make_one(res)

    def update_browser_stream(
        self,
        res: "bs_td.UpdateBrowserStreamResponseTypeDef",
    ) -> "dc_td.UpdateBrowserStreamResponse":
        return dc_td.UpdateBrowserStreamResponse.make_one(res)


bedrock_agentcore_caster = BEDROCK_AGENTCORECaster()
