# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectparticipant import type_defs as bs_td


class CONNECTPARTICIPANTCaster:

    def create_participant_connection(
        self,
        res: "bs_td.CreateParticipantConnectionResponseTypeDef",
    ) -> "dc_td.CreateParticipantConnectionResponse":
        return dc_td.CreateParticipantConnectionResponse.make_one(res)

    def describe_view(
        self,
        res: "bs_td.DescribeViewResponseTypeDef",
    ) -> "dc_td.DescribeViewResponse":
        return dc_td.DescribeViewResponse.make_one(res)

    def get_attachment(
        self,
        res: "bs_td.GetAttachmentResponseTypeDef",
    ) -> "dc_td.GetAttachmentResponse":
        return dc_td.GetAttachmentResponse.make_one(res)

    def get_authentication_url(
        self,
        res: "bs_td.GetAuthenticationUrlResponseTypeDef",
    ) -> "dc_td.GetAuthenticationUrlResponse":
        return dc_td.GetAuthenticationUrlResponse.make_one(res)

    def get_transcript(
        self,
        res: "bs_td.GetTranscriptResponseTypeDef",
    ) -> "dc_td.GetTranscriptResponse":
        return dc_td.GetTranscriptResponse.make_one(res)

    def send_event(
        self,
        res: "bs_td.SendEventResponseTypeDef",
    ) -> "dc_td.SendEventResponse":
        return dc_td.SendEventResponse.make_one(res)

    def send_message(
        self,
        res: "bs_td.SendMessageResponseTypeDef",
    ) -> "dc_td.SendMessageResponse":
        return dc_td.SendMessageResponse.make_one(res)

    def start_attachment_upload(
        self,
        res: "bs_td.StartAttachmentUploadResponseTypeDef",
    ) -> "dc_td.StartAttachmentUploadResponse":
        return dc_td.StartAttachmentUploadResponse.make_one(res)


connectparticipant_caster = CONNECTPARTICIPANTCaster()
