# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""avro python class for file: frame_channel_metadata_record"""

import typing
from pydantic import validator
from etptypes import ETPModel, Field, Strict


from etptypes.energistics.etp.v12.datatypes.channel_data.channel_data_kind import (
    ChannelDataKind,
)

from etptypes.energistics.etp.v12.datatypes.object.active_status_kind import (
    ActiveStatusKind,
)

from etptypes.energistics.etp.v12.datatypes.attribute_metadata_record import (
    AttributeMetadataRecord,
)

from etptypes.energistics.etp.v12.datatypes.data_value import DataValue


avro_schema: typing.Final[str] = (
    '{"type": "record", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "FrameChannelMetadataRecord", "fields": [{"name": "uri", "type": "string"}, {"name": "channelName", "type": "string"}, {"name": "dataKind", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes.ChannelData", "name": "ChannelDataKind", "symbols": ["DateTime", "ElapsedTime", "MeasuredDepth", "PassIndexedDepth", "TrueVerticalDepth", "typeBoolean", "typeInt", "typeLong", "typeFloat", "typeDouble", "typeString", "typeBytes"], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.ChannelDataKind", "depends": []}}, {"name": "uom", "type": "string"}, {"name": "depthDatum", "type": "string"}, {"name": "channelPropertyKindUri", "type": "string"}, {"name": "status", "type": {"type": "enum", "namespace": "Energistics.Etp.v12.Datatypes.Object", "name": "ActiveStatusKind", "symbols": ["Active", "Inactive"], "fullName": "Energistics.Etp.v12.Datatypes.Object.ActiveStatusKind", "depends": []}}, {"name": "source", "type": "string"}, {"name": "axisVectorLengths", "type": {"type": "array", "items": "int"}}, {"name": "attributeMetadata", "type": {"type": "array", "items": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AttributeMetadataRecord", "fields": [{"name": "attributeId", "type": "int"}, {"name": "attributeName", "type": "string"}, {"name": "dataKind", "type": "Energistics.Etp.v12.Datatypes.ChannelData.ChannelDataKind"}, {"name": "uom", "type": "string"}, {"name": "depthDatum", "type": "string"}, {"name": "attributePropertyKindUri", "type": "string"}, {"name": "axisVectorLengths", "type": {"type": "array", "items": "int"}}], "fullName": "Energistics.Etp.v12.Datatypes.AttributeMetadataRecord", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.ChannelDataKind"]}}, "default": []}, {"name": "customData", "type": {"type": "map", "values": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "DataValue", "fields": [{"name": "item", "type": ["null", "boolean", "int", "long", "float", "double", "string", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfBoolean", "fields": [{"name": "values", "type": {"type": "array", "items": "boolean"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfNullableBoolean", "fields": [{"name": "values", "type": {"type": "array", "items": ["null", "boolean"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfNullableBoolean", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfInt", "fields": [{"name": "values", "type": {"type": "array", "items": "int"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfInt", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfNullableInt", "fields": [{"name": "values", "type": {"type": "array", "items": ["null", "int"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfNullableInt", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfLong", "fields": [{"name": "values", "type": {"type": "array", "items": "long"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfLong", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfNullableLong", "fields": [{"name": "values", "type": {"type": "array", "items": ["null", "long"]}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfNullableLong", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfFloat", "fields": [{"name": "values", "type": {"type": "array", "items": "float"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfDouble", "fields": [{"name": "values", "type": {"type": "array", "items": "double"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfString", "fields": [{"name": "values", "type": {"type": "array", "items": "string"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfString", "depends": []}, {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "ArrayOfBytes", "fields": [{"name": "values", "type": {"type": "array", "items": "bytes"}}], "fullName": "Energistics.Etp.v12.Datatypes.ArrayOfBytes", "depends": []}, "bytes", {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnySparseArray", "fields": [{"name": "slices", "type": {"type": "array", "items": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnySubarray", "fields": [{"name": "start", "type": "long"}, {"name": "slice", "type": {"type": "record", "namespace": "Energistics.Etp.v12.Datatypes", "name": "AnyArray", "fields": [{"name": "item", "type": ["Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfInt", "Energistics.Etp.v12.Datatypes.ArrayOfLong", "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "Energistics.Etp.v12.Datatypes.ArrayOfString", "bytes"]}], "fullName": "Energistics.Etp.v12.Datatypes.AnyArray", "depends": ["Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfInt", "Energistics.Etp.v12.Datatypes.ArrayOfLong", "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "Energistics.Etp.v12.Datatypes.ArrayOfString"]}}], "fullName": "Energistics.Etp.v12.Datatypes.AnySubarray", "depends": ["Energistics.Etp.v12.Datatypes.AnyArray"]}}}], "fullName": "Energistics.Etp.v12.Datatypes.AnySparseArray", "depends": ["Energistics.Etp.v12.Datatypes.AnySubarray"]}]}], "fullName": "Energistics.Etp.v12.Datatypes.DataValue", "depends": ["Energistics.Etp.v12.Datatypes.ArrayOfBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfNullableBoolean", "Energistics.Etp.v12.Datatypes.ArrayOfInt", "Energistics.Etp.v12.Datatypes.ArrayOfNullableInt", "Energistics.Etp.v12.Datatypes.ArrayOfLong", "Energistics.Etp.v12.Datatypes.ArrayOfNullableLong", "Energistics.Etp.v12.Datatypes.ArrayOfFloat", "Energistics.Etp.v12.Datatypes.ArrayOfDouble", "Energistics.Etp.v12.Datatypes.ArrayOfString", "Energistics.Etp.v12.Datatypes.ArrayOfBytes", "Energistics.Etp.v12.Datatypes.AnySparseArray"]}}, "default": {}}], "fullName": "Energistics.Etp.v12.Datatypes.ChannelData.FrameChannelMetadataRecord", "depends": ["Energistics.Etp.v12.Datatypes.ChannelData.ChannelDataKind", "Energistics.Etp.v12.Datatypes.Object.ActiveStatusKind", "Energistics.Etp.v12.Datatypes.AttributeMetadataRecord", "Energistics.Etp.v12.Datatypes.DataValue"]}'
)


class FrameChannelMetadataRecord(ETPModel):

    uri: str = Field(alias="uri")

    channel_name: str = Field(alias="channelName")

    data_kind: ChannelDataKind = Field(alias="dataKind")

    uom: str = Field(alias="uom")

    depth_datum: str = Field(alias="depthDatum")

    channel_property_kind_uri: str = Field(alias="channelPropertyKindUri")

    status: ActiveStatusKind = Field(alias="status")

    source: str = Field(alias="source")

    axis_vector_lengths: typing.List[Strict[int]] = Field(
        alias="axisVectorLengths"
    )

    attribute_metadata: typing.List[AttributeMetadataRecord] = Field(
        alias="attributeMetadata", default_factory=lambda: []
    )

    custom_data: typing.Mapping[str, DataValue] = Field(
        alias="customData", default_factory=lambda: {}
    )
