# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: lock_dataspaces_response"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.DataspaceOSDU", "name": "LockDataspacesResponse", "protocol": "2424", "messageType": "6", "senderRole": "store", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "success", "type": {"type": "map", "values": "string"}}], "fullName": "Energistics.Etp.v12.Protocol.DataspaceOSDU.LockDataspacesResponse", "depends": []}'
)


class LockDataspacesResponse(ETPModel):

    success: typing.Mapping[str, str] = Field(alias="success")
