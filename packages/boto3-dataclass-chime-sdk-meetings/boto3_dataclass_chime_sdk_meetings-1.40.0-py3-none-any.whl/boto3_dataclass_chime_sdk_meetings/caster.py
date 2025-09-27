# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_meetings import type_defs as bs_td


class CHIME_SDK_MEETINGSCaster:

    def batch_create_attendee(
        self,
        res: "bs_td.BatchCreateAttendeeResponseTypeDef",
    ) -> "dc_td.BatchCreateAttendeeResponse":
        return dc_td.BatchCreateAttendeeResponse.make_one(res)

    def batch_update_attendee_capabilities_except(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_attendee(
        self,
        res: "bs_td.CreateAttendeeResponseTypeDef",
    ) -> "dc_td.CreateAttendeeResponse":
        return dc_td.CreateAttendeeResponse.make_one(res)

    def create_meeting(
        self,
        res: "bs_td.CreateMeetingResponseTypeDef",
    ) -> "dc_td.CreateMeetingResponse":
        return dc_td.CreateMeetingResponse.make_one(res)

    def create_meeting_with_attendees(
        self,
        res: "bs_td.CreateMeetingWithAttendeesResponseTypeDef",
    ) -> "dc_td.CreateMeetingWithAttendeesResponse":
        return dc_td.CreateMeetingWithAttendeesResponse.make_one(res)

    def delete_attendee(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_meeting(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_attendee(
        self,
        res: "bs_td.GetAttendeeResponseTypeDef",
    ) -> "dc_td.GetAttendeeResponse":
        return dc_td.GetAttendeeResponse.make_one(res)

    def get_meeting(
        self,
        res: "bs_td.GetMeetingResponseTypeDef",
    ) -> "dc_td.GetMeetingResponse":
        return dc_td.GetMeetingResponse.make_one(res)

    def list_attendees(
        self,
        res: "bs_td.ListAttendeesResponseTypeDef",
    ) -> "dc_td.ListAttendeesResponse":
        return dc_td.ListAttendeesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_meeting_transcription(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_meeting_transcription(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_attendee_capabilities(
        self,
        res: "bs_td.UpdateAttendeeCapabilitiesResponseTypeDef",
    ) -> "dc_td.UpdateAttendeeCapabilitiesResponse":
        return dc_td.UpdateAttendeeCapabilitiesResponse.make_one(res)


chime_sdk_meetings_caster = CHIME_SDK_MEETINGSCaster()
