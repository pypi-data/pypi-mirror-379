# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: get_parts"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.GrowingObject", "name": "GetParts", "protocol": "6", "messageType": "3", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "uri", "type": "string"}, {"name": "format", "type": "string", "default": "xml"}, {"name": "uids", "type": {"type": "map", "values": "string"}}], "fullName": "Energistics.Etp.v12.Protocol.GrowingObject.GetParts", "depends": []}'
)


class GetParts(ETPModel):

    uri: str = Field(alias="uri")

    uids: typing.Mapping[str, str] = Field(alias="uids")

    format_: str = Field(alias="format", default="xml")
