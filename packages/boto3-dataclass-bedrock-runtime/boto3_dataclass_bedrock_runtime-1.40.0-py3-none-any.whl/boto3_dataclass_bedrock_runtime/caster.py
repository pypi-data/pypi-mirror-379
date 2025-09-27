# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_runtime import type_defs as bs_td


class BEDROCK_RUNTIMECaster:

    def apply_guardrail(
        self,
        res: "bs_td.ApplyGuardrailResponseTypeDef",
    ) -> "dc_td.ApplyGuardrailResponse":
        return dc_td.ApplyGuardrailResponse.make_one(res)

    def converse(
        self,
        res: "bs_td.ConverseResponseTypeDef",
    ) -> "dc_td.ConverseResponse":
        return dc_td.ConverseResponse.make_one(res)

    def converse_stream(
        self,
        res: "bs_td.ConverseStreamResponseTypeDef",
    ) -> "dc_td.ConverseStreamResponse":
        return dc_td.ConverseStreamResponse.make_one(res)

    def count_tokens(
        self,
        res: "bs_td.CountTokensResponseTypeDef",
    ) -> "dc_td.CountTokensResponse":
        return dc_td.CountTokensResponse.make_one(res)

    def get_async_invoke(
        self,
        res: "bs_td.GetAsyncInvokeResponseTypeDef",
    ) -> "dc_td.GetAsyncInvokeResponse":
        return dc_td.GetAsyncInvokeResponse.make_one(res)

    def invoke_model(
        self,
        res: "bs_td.InvokeModelResponseTypeDef",
    ) -> "dc_td.InvokeModelResponse":
        return dc_td.InvokeModelResponse.make_one(res)

    def invoke_model_with_bidirectional_stream(
        self,
        res: "bs_td.InvokeModelWithBidirectionalStreamResponseTypeDef",
    ) -> "dc_td.InvokeModelWithBidirectionalStreamResponse":
        return dc_td.InvokeModelWithBidirectionalStreamResponse.make_one(res)

    def invoke_model_with_response_stream(
        self,
        res: "bs_td.InvokeModelWithResponseStreamResponseTypeDef",
    ) -> "dc_td.InvokeModelWithResponseStreamResponse":
        return dc_td.InvokeModelWithResponseStreamResponse.make_one(res)

    def list_async_invokes(
        self,
        res: "bs_td.ListAsyncInvokesResponseTypeDef",
    ) -> "dc_td.ListAsyncInvokesResponse":
        return dc_td.ListAsyncInvokesResponse.make_one(res)

    def start_async_invoke(
        self,
        res: "bs_td.StartAsyncInvokeResponseTypeDef",
    ) -> "dc_td.StartAsyncInvokeResponse":
        return dc_td.StartAsyncInvokeResponse.make_one(res)


bedrock_runtime_caster = BEDROCK_RUNTIMECaster()
