# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: copy_to_dataspace_response"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.DataspaceOSDU", "name": "CopyToDataspaceResponse", "protocol": "2424", "messageType": "8", "senderRole": "store", "protocolRoles": "store,customer", "multipartFlag": true, "fields": [{"name": "success", "type": {"type": "map", "values": "string"}}], "fullName": "Energistics.Etp.v12.Protocol.DataspaceOSDU.CopyToDataspaceResponse", "depends": []}'
)


class CopyToDataspaceResponse(ETPModel):

    success: typing.Mapping[str, str] = Field(alias="success")
