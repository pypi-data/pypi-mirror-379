# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: channels_truncated"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


from etptypes.energistics.etp.v12.datatypes.channel_data.truncate_info import (
    TruncateInfo,
)


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.ChannelSubscribe", "name": "ChannelsTruncated", "protocol": "21", "messageType": "13", "senderRole": "store", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "channels", "type": {"type": "array", "items": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "TruncateInfo", "fields": [{"name": "channelId", "type": "long"}, {"name": "newEndIndex", "type": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "IndexValue", "fields": [{"name": "item", "type": ["null", "long", "double", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "PassIndexedDepth", "fields": [{"name": "pass", "type": "long"}, {"name": "direction", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "PassDirection", "symbols": ["Up", "HoldingSteady", "Down"], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.PassDirection", "depends": []}}, {"name": "depth", "type": "double"}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.PassIndexedDepth", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.PassDirection"]}]}], "fullName": "Energistics.Etp.v12.Datatypes.IndexValue", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.PassIndexedDepth"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.TruncateInfo", "depends": ["Energistics.Etp.v12.Datatypes.IndexValue"]}}}, {"name": "changeTime", "type": "long"}], "fullName": "Energistics.Etp.v12.Protocol.ChannelSubscribe.ChannelsTruncated", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.TruncateInfo"]}'
)


class ChannelsTruncated(ETPModel):

    channels: typing.List[TruncateInfo] = Field(alias="channels")

    change_time: int = Field(alias="changeTime")
