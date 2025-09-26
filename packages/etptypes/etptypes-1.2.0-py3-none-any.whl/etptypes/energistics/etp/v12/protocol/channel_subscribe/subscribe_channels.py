# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: subscribe_channels"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


from etptypes.energistics.etp.v12.datatypes.channel_data.channel_subscribe_info import (
    ChannelSubscribeInfo,
)


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.ChannelSubscribe", "name": "SubscribeChannels", "protocol": "21", "messageType": "3", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "channels", "type": {"type": "map", "values": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "ChannelSubscribeInfo", "fields": [{"name": "channelId", "type": "long"}, {"name": "startIndex", "type": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "IndexValue", "fields": [{"name": "item", "type": ["null", "long", "double", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "PassIndexedDepth", "fields": [{"name": "pass", "type": "long"}, {"name": "direction", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "PassDirection", "symbols": ["Up", "HoldingSteady", "Down"], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.PassDirection", "depends": []}}, {"name": "depth", "type": "double"}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.PassIndexedDepth", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.PassDirection"]}]}], "fullName": "Energistics.Etp.v12.Datatypes.IndexValue", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.PassIndexedDepth"]}}, {"name": "dataChanges", "type": "boolean", "default": true}, {"name": "requestLatestIndexCount", "type": ["null", "int"]}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.ChannelSubscribeInfo", "depends": ["Energistics.Etp.v12.Datatypes.IndexValue"]}}}], "fullName": "Energistics.Etp.v12.Protocol.ChannelSubscribe.SubscribeChannels", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.ChannelSubscribeInfo"]}'
)


class SubscribeChannels(ETPModel):

    channels: typing.Mapping[str, ChannelSubscribeInfo] = Field(
        alias="channels"
    )
