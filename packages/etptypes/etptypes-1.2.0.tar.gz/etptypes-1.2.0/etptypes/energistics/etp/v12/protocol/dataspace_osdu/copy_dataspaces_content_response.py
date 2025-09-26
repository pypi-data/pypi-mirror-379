# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: copy_dataspaces_content_response"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.DataspaceOSDU", "name": "CopyDataspacesContentResponse", "protocol": "2424", "messageType": "4", "senderRole": "store", "protocolRoles": "store,customer", "multipartFlag": true, "fields": [{"name": "success", "type": {"type": "map", "values": "string"}}], "fullName": "Energistics.Etp.v12.Protocol.DataspaceOSDU.CopyDataspacesContentResponse", "depends": []}'
)


class CopyDataspacesContentResponse(ETPModel):

    success: typing.Mapping[str, str] = Field(alias="success")
