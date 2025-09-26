# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: copy_dataspaces_content"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.DataspaceOSDU", "name": "CopyDataspacesContent", "protocol": "2424", "messageType": "3", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "dataspaces", "type": {"type": "map", "values": "string"}}, {"name": "targetDataspace", "type": "string"}], "fullName": "Energistics.Etp.v12.Protocol.DataspaceOSDU.CopyDataspacesContent", "depends": []}'
)


class CopyDataspacesContent(ETPModel):

    dataspaces: typing.Mapping[str, str] = Field(alias="dataspaces")

    target_dataspace: str = Field(alias="targetDataspace")
