# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: lock_dataspaces"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.DataspaceOSDU", "name": "LockDataspaces", "protocol": "2424", "messageType": "5", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "uris", "type": {"type": "map", "values": "string"}}, {"name": "lock", "type": "boolean"}], "fullName": "Energistics.Etp.v12.Protocol.DataspaceOSDU.LockDataspaces", "depends": []}'
)


class LockDataspaces(ETPModel):

    uris: typing.Mapping[str, str] = Field(alias="uris")

    lock: bool = Field(alias="lock")
