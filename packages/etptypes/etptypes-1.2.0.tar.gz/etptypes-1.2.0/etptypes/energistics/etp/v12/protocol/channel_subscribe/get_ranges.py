# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: get_ranges"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


from etptypes.energistics.etp.v12.datatypes.uuid import Uuid

from etptypes.energistics.etp.v12.datatypes.channel_data.channel_range_info import (
    ChannelRangeInfo,
)


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.ChannelSubscribe", "name": "GetRanges", "protocol": "21", "messageType": "9", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "requestUuid", "type": {"type": "fixed", "namespace": "Energistics.Etp.v12.Datatypes", "name": "Uuid", "size": 16, "fullName": "Energistics.Etp.v12.Datatypes.Uuid", "depends": []}}, {"name": "channelRanges", "type": {"type": "array", "items": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "ChannelRangeInfo", "fields": [{"name": "channelIds", "type": {"type": "array", "items": "long"}}, {"name": "interval", "type": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.Object", "name": "IndexInterval", "fields": [{"name": "startIndex", "type": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "IndexValue", "fields": [{"name": "item", "type": ["null", "long", "double", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "PassIndexedDepth", "fields": [{"name": "pass", "type": "long"}, {"name": "direction", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "PassDirection", "symbols": ["Up", "HoldingSteady", "Down"], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.PassDirection", "depends": []}}, {"name": "depth", "type": "double"}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.PassIndexedDepth", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.PassDirection"]}]}], "fullName": "Energistics.Etp.v12.Datatypes.IndexValue", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.PassIndexedDepth"]}}, {"name": "endIndex", "type": "Energistics.Etp.v12.Datatypes.IndexValue"}, {"name": "uom", "type": "string"}, {"name": "depthDatum", "type": "string", "default": ""}], "fullName": "Energistics.Etp.v12.Datatypes.Object.IndexInterval", "depends": ["Energistics.Etp.v12.Datatypes.IndexValue"]}}, {"name": "secondaryIntervals", "type": {"type": "array", "items": "Energistics.Etp.v12.Datatypes.Object.IndexInterval"}, "default": []}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.ChannelRangeInfo", "depends": ["Energistics.Etp.v12.Datatypes.Object.IndexInterval"]}}}], "fullName": "Energistics.Etp.v12.Protocol.ChannelSubscribe.GetRanges", "depends": ["Energistics.Etp.v12.Datatypes.Uuid", "Energistics.Etp.v12.Datatypes.ChannelData.ChannelRangeInfo"]}'
)


class GetRanges(ETPModel):

    request_uuid: Uuid = Field(alias="requestUuid")

    channel_ranges: typing.List[ChannelRangeInfo] = Field(
        alias="channelRanges"
    )
