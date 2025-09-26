# Copyright (c) 2022-2023 Geosiris.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-

"""Top-level package for etptypes."""

__author__ = """Valentin Gauthier <valentin.gauthier@geosiris.com>"""
__version__ = "1.2.0"


from enum import Enum
from pydantic import BaseModel, Field as Field
from sys import modules
from types import ModuleType, new_class
from typing import (
    cast,
    Type,
    TypeVar,
    Any,
    Generic,
    Generator,
    Callable,
    Optional,
)
from typingx import isinstancex
from pydantic.fields import ModelField
from pydantic.schema import add_field_type_to_schema


class ETPModel(BaseModel):
    class Config:
        allow_population_by_field_name: bool = True
        smart_union: bool = True


class StrEnum(str, Enum):
    pass


def avro_schema(class_: Type[ETPModel]) -> str:
    mod: ModuleType = modules[class_.__module__]
    return cast(
        str, getattr(mod, "avro_schema")
    )  # cast is not a runtime check !


T = TypeVar("T")


def _display_type(v: Any) -> str:
    try:
        return v.__name__
    except AttributeError:
        # happens with typing objects
        return str(v).replace("typing.", "")


class Strict(Generic[T]):
    __typelike__: T

    @classmethod
    def __class_getitem__(cls, typelike: T) -> T:
        new_cls = new_class(
            f"Strict[{_display_type(typelike)}]",
            (cls,),
            {},
            lambda ns: ns.update({"__typelike__": typelike}),
        )
        return cast(T, new_cls)

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., Any], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> T:
        if not isinstancex(value, cls.__typelike__):
            raise TypeError(
                f"{type(value)} : -- {value!r} is not of valid type"
            )
        return value

    @classmethod
    def __modify_schema__(
        cls, field_schema, field: Optional[ModelField] = None
    ):
        add_field_type_to_schema(cls.__typelike__, field_schema)
