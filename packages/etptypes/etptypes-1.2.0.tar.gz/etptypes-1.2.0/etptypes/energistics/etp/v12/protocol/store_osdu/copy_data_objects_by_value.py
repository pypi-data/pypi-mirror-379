# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: copy_data_objects_by_value"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.StoreOSDU", "name": "CopyDataObjectsByValue", "protocol": "2404", "messageType": "1", "senderRole": "customer", "protocolRoles": "store,customer", "multipartFlag": false, "fields": [{"name": "uri", "type": "string"}, {"name": "sourcesDepth", "type": "int"}, {"name": "dataObjectTypes", "type": {"type": "array", "items": "string"}, "default": []}], "fullName": "Energistics.Etp.v12.Protocol.StoreOSDU.CopyDataObjectsByValue", "depends": []}'
)


class CopyDataObjectsByValue(ETPModel):

    uri: str = Field(alias="uri")

    sources_depth: int = Field(alias="sourcesDepth")

    data_object_types: typing.List[Strict[str]] = Field(
        alias="dataObjectTypes", default_factory=lambda: []
    )
