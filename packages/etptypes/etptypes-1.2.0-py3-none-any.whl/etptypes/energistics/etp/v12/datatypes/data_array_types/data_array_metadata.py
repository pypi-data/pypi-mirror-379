# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: data_array_metadata"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


from etptypes.energistics.etp.v12.datatypes.any_array_type import AnyArrayType

from etptypes.energistics.etp.v12.datatypes.any_logical_array_type import (
    AnyLogicalArrayType,
)

from etptypes.energistics.etp.v12.datatypes.data_value import DataValue


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.DataArrayTypes", "name": "DataArrayMetadata", "fields": [{"name": "dimensions", "type": {"type": "array", "items": "long"}}, {"name": "preferredSubarrayDimensions", "type": {"type": "array", "items": "long"}, "default": []}, {"name": "transportArrayType", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnyArrayType", "symbols": ["arrayOfBoolean", "arrayOfInt", "arrayOfLong", "arrayOfFloat", "arrayOfDouble", "arrayOfString", "bytes"], "fullName": "Energistics.Etp.v12.Datatypes.AnyArrayType", "depends": []}}, {"name": "logicalArrayType", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnyLogicalArrayType", "symbols": ["arrayOfBoolean", "arrayOfInt8", "arrayOfUInt8", "arrayOfInt16LE", "arrayOfInt32LE", "arrayOfInt64LE", "arrayOfUInt16LE", "arrayOfUInt32LE", "arrayOfUInt64LE", "arrayOfFloat32LE", "arrayOfDouble64LE", "arrayOfInt16BE", "arrayOfInt32BE", "arrayOfInt64BE", "arrayOfUInt16BE", "arrayOfUInt32BE", "arrayOfUInt64BE", "arrayOfFloat32BE", "arrayOfDouble64BE", "arrayOfString", "arrayOfCustom"], "fullName": "Energistics.Etp.v12.Datatypes.AnyLogicalArrayType", "depends": []}}, {"name": "storeLastWrite", "type": "long"}, {"name": "storeCreated", "type": "long"}, {"name": "customData", "type": {"type": "map", "values": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "DataValue", "fields": [{"name": "item", "type": ["null", "boolean", "int", "long", "float", "double", "string", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfBoolean", "fields": [{"name": "values", "type": {"type": "array", "items": "boolean"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfNullableBoolean", "fields": [{"name": "values", "type": {"type": "array", "items": ["null", "boolean"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfNullableBoolean", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfInt", "fields": [{"name": "values", "type": {"type": "array", "items": "int"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfInt", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfNullableInt", "fields": [{"name": "values", "type": {"type": "array", "items": ["null", "int"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfNullableInt", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfLong", "fields": [{"name": "values", "type": {"type": "array", "items": "long"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfLong", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfNullableLong", "fields": [{"name": "values", "type": {"type": "array", "items": ["null", "long"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfNullableLong", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfFloat", "fields": [{"name": "values", "type": {"type": "array", "items": "float"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfDouble", "fields": [{"name": "values", "type": {"type": "array", "items": "double"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfString", "fields": [{"name": "values", "type": {"type": "array", "items": "string"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfString", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfBytes", "fields": [{"name": "values", "type": {"type": "array", "items": "bytes"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfBytes", "depends": []}, "bytes", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnySparseArray", "fields": [{"name": "slices", "type": {"type": "array", "items": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnySubarray", "fields": [{"name": "start", "type": "long"}, {"name": "slice", "type": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnyArray", "fields": [{"name": "item", "type": ["Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfInt", "Energistics.Etp.v12.Datatypes.ArrayOfLong", "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "Energistics.Etp.v12.Datatypes.ArrayOfString", "bytes"]}], "fullName": "Energistics.Etp.v12.Datatypes.AnyArray", "depends": ["Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfInt", "Energistics.Etp.v12.Datatypes.ArrayOfLong", "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "Energistics.Etp.v12.Datatypes.ArrayOfString"]}}], "fullName": "Energistics.Etp.v12.Datatypes.AnySubarray", "depends": ["Energistics.Etp.v12.Datatypes.AnyArray"]}}}], "fullName": "Energistics.Etp.v12.Datatypes.AnySparseArray", "depends": ["Energistics.Etp.v12.Datatypes.AnySubarray"]}]}], "fullName": "Energistics.Etp.v12.Datatypes.DataValue", "depends": ["Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfNullableBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfInt", "Energistics.Etp.v12.Datatypes.ArrayOfNullableInt", "Energistics.Etp.v12.Datatypes.ArrayOfLong", "Energistics.Etp.v12.Datatypes.ArrayOfNullableLong", "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "Energistics.Etp.v12.Datatypes.ArrayOfString", "Energistics.Etp.v12.Datatypes.ArrayOfBytes", "Energistics.Etp.v12.Datatypes.AnySparseArray"]}}, "default": {}}], "fullName": "Energistics.Etp.v12.Datatypes.DataArrayTypes.DataArrayMetadata", "depends": ["Energistics.Etp.v12.Datatypes.AnyArrayType", "Energistics.Etp.v12.Datatypes.AnyLogicalArrayType", "Energistics.Etp.v12.Datatypes.DataValue"]}'
)


class DataArrayMetadata(ETPModel):

    dimensions: typing.List[Strict[int]] = Field(alias="dimensions")

    transport_array_type: AnyArrayType = Field(alias="transportArrayType")

    logical_array_type: AnyLogicalArrayType = Field(alias="logicalArrayType")

    store_last_write: int = Field(alias="storeLastWrite")

    store_created: int = Field(alias="storeCreated")

    preferred_subarray_dimensions: typing.List[Strict[int]] = Field(
        alias="preferredSubarrayDimensions", default_factory=lambda: []
    )

    custom_data: typing.Mapping[str, DataValue] = Field(
        alias="customData", default_factory=lambda: {}
    )
