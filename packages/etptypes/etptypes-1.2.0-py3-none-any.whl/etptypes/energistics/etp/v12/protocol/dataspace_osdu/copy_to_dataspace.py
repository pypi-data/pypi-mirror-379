# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: copy_to_dataspace"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.DataspaceOSDU", "name": "CopyToDataspace", "protocol": "2424", "messageType": "7", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "uris", "type": {"type": "map", "values": "string"}}, {"name": "dataspaceUri", "type": "string"}], "fullName": "Energistics.Etp.v12.Protocol.DataspaceOSDU.CopyToDataspace", "depends": []}'
)


class CopyToDataspace(ETPModel):

    uris: typing.Mapping[str, str] = Field(alias="uris")

    dataspace_uri: str = Field(alias="dataspaceUri")
