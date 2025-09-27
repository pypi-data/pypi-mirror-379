# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agent_runtime import type_defs as bs_td


class BEDROCK_AGENT_RUNTIMECaster:

    def create_invocation(
        self,
        res: "bs_td.CreateInvocationResponseTypeDef",
    ) -> "dc_td.CreateInvocationResponse":
        return dc_td.CreateInvocationResponse.make_one(res)

    def create_session(
        self,
        res: "bs_td.CreateSessionResponseTypeDef",
    ) -> "dc_td.CreateSessionResponse":
        return dc_td.CreateSessionResponse.make_one(res)

    def end_session(
        self,
        res: "bs_td.EndSessionResponseTypeDef",
    ) -> "dc_td.EndSessionResponse":
        return dc_td.EndSessionResponse.make_one(res)

    def generate_query(
        self,
        res: "bs_td.GenerateQueryResponseTypeDef",
    ) -> "dc_td.GenerateQueryResponse":
        return dc_td.GenerateQueryResponse.make_one(res)

    def get_agent_memory(
        self,
        res: "bs_td.GetAgentMemoryResponseTypeDef",
    ) -> "dc_td.GetAgentMemoryResponse":
        return dc_td.GetAgentMemoryResponse.make_one(res)

    def get_execution_flow_snapshot(
        self,
        res: "bs_td.GetExecutionFlowSnapshotResponseTypeDef",
    ) -> "dc_td.GetExecutionFlowSnapshotResponse":
        return dc_td.GetExecutionFlowSnapshotResponse.make_one(res)

    def get_flow_execution(
        self,
        res: "bs_td.GetFlowExecutionResponseTypeDef",
    ) -> "dc_td.GetFlowExecutionResponse":
        return dc_td.GetFlowExecutionResponse.make_one(res)

    def get_invocation_step(
        self,
        res: "bs_td.GetInvocationStepResponseTypeDef",
    ) -> "dc_td.GetInvocationStepResponse":
        return dc_td.GetInvocationStepResponse.make_one(res)

    def get_session(
        self,
        res: "bs_td.GetSessionResponseTypeDef",
    ) -> "dc_td.GetSessionResponse":
        return dc_td.GetSessionResponse.make_one(res)

    def invoke_agent(
        self,
        res: "bs_td.InvokeAgentResponseTypeDef",
    ) -> "dc_td.InvokeAgentResponse":
        return dc_td.InvokeAgentResponse.make_one(res)

    def invoke_flow(
        self,
        res: "bs_td.InvokeFlowResponseTypeDef",
    ) -> "dc_td.InvokeFlowResponse":
        return dc_td.InvokeFlowResponse.make_one(res)

    def invoke_inline_agent(
        self,
        res: "bs_td.InvokeInlineAgentResponseTypeDef",
    ) -> "dc_td.InvokeInlineAgentResponse":
        return dc_td.InvokeInlineAgentResponse.make_one(res)

    def list_flow_execution_events(
        self,
        res: "bs_td.ListFlowExecutionEventsResponseTypeDef",
    ) -> "dc_td.ListFlowExecutionEventsResponse":
        return dc_td.ListFlowExecutionEventsResponse.make_one(res)

    def list_flow_executions(
        self,
        res: "bs_td.ListFlowExecutionsResponseTypeDef",
    ) -> "dc_td.ListFlowExecutionsResponse":
        return dc_td.ListFlowExecutionsResponse.make_one(res)

    def list_invocation_steps(
        self,
        res: "bs_td.ListInvocationStepsResponseTypeDef",
    ) -> "dc_td.ListInvocationStepsResponse":
        return dc_td.ListInvocationStepsResponse.make_one(res)

    def list_invocations(
        self,
        res: "bs_td.ListInvocationsResponseTypeDef",
    ) -> "dc_td.ListInvocationsResponse":
        return dc_td.ListInvocationsResponse.make_one(res)

    def list_sessions(
        self,
        res: "bs_td.ListSessionsResponseTypeDef",
    ) -> "dc_td.ListSessionsResponse":
        return dc_td.ListSessionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def optimize_prompt(
        self,
        res: "bs_td.OptimizePromptResponseTypeDef",
    ) -> "dc_td.OptimizePromptResponse":
        return dc_td.OptimizePromptResponse.make_one(res)

    def put_invocation_step(
        self,
        res: "bs_td.PutInvocationStepResponseTypeDef",
    ) -> "dc_td.PutInvocationStepResponse":
        return dc_td.PutInvocationStepResponse.make_one(res)

    def rerank(
        self,
        res: "bs_td.RerankResponseTypeDef",
    ) -> "dc_td.RerankResponse":
        return dc_td.RerankResponse.make_one(res)

    def retrieve(
        self,
        res: "bs_td.RetrieveResponseTypeDef",
    ) -> "dc_td.RetrieveResponse":
        return dc_td.RetrieveResponse.make_one(res)

    def retrieve_and_generate(
        self,
        res: "bs_td.RetrieveAndGenerateResponseTypeDef",
    ) -> "dc_td.RetrieveAndGenerateResponse":
        return dc_td.RetrieveAndGenerateResponse.make_one(res)

    def retrieve_and_generate_stream(
        self,
        res: "bs_td.RetrieveAndGenerateStreamResponseTypeDef",
    ) -> "dc_td.RetrieveAndGenerateStreamResponse":
        return dc_td.RetrieveAndGenerateStreamResponse.make_one(res)

    def start_flow_execution(
        self,
        res: "bs_td.StartFlowExecutionResponseTypeDef",
    ) -> "dc_td.StartFlowExecutionResponse":
        return dc_td.StartFlowExecutionResponse.make_one(res)

    def stop_flow_execution(
        self,
        res: "bs_td.StopFlowExecutionResponseTypeDef",
    ) -> "dc_td.StopFlowExecutionResponse":
        return dc_td.StopFlowExecutionResponse.make_one(res)

    def update_session(
        self,
        res: "bs_td.UpdateSessionResponseTypeDef",
    ) -> "dc_td.UpdateSessionResponse":
        return dc_td.UpdateSessionResponse.make_one(res)


bedrock_agent_runtime_caster = BEDROCK_AGENT_RUNTIMECaster()
