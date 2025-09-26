# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: copy_data_objects_by_value_response"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Protocol.StoreOSDU", "name": "CopyDataObjectsByValueResponse", "protocol": "2404", "messageType": "2", "senderRole": "store", "protocolRoles": "store,customer", "multipartFlag": true, "fields": [{"name": "copiedDataObjects", "type": {"type": "array", "items": "string"}}], "fullName": "Energistics.Etp.v12.Protocol.StoreOSDU.CopyDataObjectsByValueResponse", "depends": []}'
)


class CopyDataObjectsByValueResponse(ETPModel):

    copied_data_objects: typing.List[Strict[str]] = Field(
        alias="copiedDataObjects"
    )
