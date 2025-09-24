import dataclasses
import datetime

import typing_extensions as typing

from ..fdl import Deserializer, ParseError, Serializer
from ..protobuf import DecodeError, Reader, WireType, Writer
from .binary import Binary
from .boolean import Boolean
from .convertable import Native
from .data_type import BasicType, DataType
from .date import Date
from .integer import Integer
from .real import Real
from .string import String
from .time import Time
from .timestamp import Timestamp
from .void import Void

if typing.TYPE_CHECKING:
    from ..common import Context
    from .constrained import Constrained
    from .list import List
    from .structure import Structure


@dataclasses.dataclass
class Any(BasicType[Native]):
    """Represents information that can be of any SiLA data type, except for a custom data type."""

    value: typing.Union[BasicType, "List", "Structure", "Constrained"] = dataclasses.field(default_factory=Void)

    @property
    def schema(self) -> str:
        """The xml representation of the data type definition."""
        serializer = Serializer(remove_whitespace=True)
        self.value.serialize(serializer)

        return serializer.buffer.getvalue()

    @classmethod
    def from_schema(cls, schema: str, payload: bytes = b"") -> typing.Self:
        """
        Create a new `Any` instance from a given schema and payload.

        Args:
          schema: The xml representation of the data type definition.
          payload: The data type's binary protobuf value.

        Returns:
          The newly create `Any` data type instance.
        """

        deserializer = Deserializer()

        data_type: type[DataType] = deserializer.deserialize(schema, DataType.deserialize)

        from .constrained import Constrained
        from .list import List
        from .structure import Structure

        assert issubclass(data_type, (BasicType, List, Structure, Constrained))

        return cls(value=data_type.decode(payload))

    @typing.override
    @classmethod
    async def from_native(cls, context: "Context", value: typing.Optional[Native] = None, /) -> typing.Self:
        from .element import Element
        from .list import List
        from .structure import Structure

        data_type: typing.Union[BasicType, "List", "Structure"] = Void()
        if value is None:
            data_type = await Void.from_native(context, value)
        elif isinstance(value, str):
            data_type = await String.from_native(context, value)
        elif isinstance(value, bytes):
            data_type = await Binary.from_native(context, value)
        elif isinstance(value, bool):
            data_type = await Boolean.from_native(context, value)
        elif isinstance(value, int):
            data_type = await Integer.from_native(context, value)
        elif isinstance(value, float):
            data_type = await Real.from_native(context, value)
        elif isinstance(value, datetime.datetime):
            data_type = await Timestamp.from_native(context, value)
        elif isinstance(value, datetime.date):
            data_type = await Date.from_native(context, value)
        elif isinstance(value, datetime.time):
            data_type = await Time.from_native(context, value)
        elif isinstance(value, list):
            item_type = Void
            items: list[typing.Union["BasicType", "Structure", "Constrained"]] = []
            for child_value in value:
                item_data_type = (await Any.from_native(context, child_value)).value

                if isinstance(item_data_type, List):
                    msg = "List may not contain other lists."
                    raise ValueError(msg)

                if items and type(item_data_type).__name__ is not item_type.__name__:
                    msg = "Only same type lists are allowed."
                    raise ValueError(msg)

                item_type = type(item_data_type)
                items.append(item_data_type)

            data_type = List.create(item_type)(items)
        elif isinstance(value, dict):
            elements: dict[str, Element] = {}
            values: dict[str, DataType] = {}
            for key, child_value in value.items():
                item_data_type = (await Any.from_native(context, child_value)).value

                values[key] = item_data_type
                elements[key] = Element(identifier=key, display_name=key, data_type=type(item_data_type))

            data_type = Structure.create(elements)(values)

        return await cls(value=data_type).validate()

    @typing.override
    async def to_native(self, context: "Context", /) -> Native:
        return await self.value.to_native(context)

    @typing.override
    async def validate(self) -> typing.Self:
        return self

    @typing.override
    @classmethod
    def decode(cls, reader: typing.Union[Reader, bytes], length: typing.Optional[int] = None) -> typing.Self:
        reader = reader if isinstance(reader, Reader) else Reader(reader)

        end = reader.length if length is None else reader.cursor + length

        offset = 0
        schema: str = ""
        payload: bytes = b""

        while reader.cursor < end:
            tag = reader.read_uint32()
            field_number = tag >> 3

            if field_number == 1:
                reader.expect_type(tag, WireType.LEN)
                schema = reader.read_string()
                offset = reader.cursor - len(schema)
            elif field_number == 2:
                reader.expect_type(tag, WireType.LEN)
                payload = reader.read_bytes()
            else:
                reader.skip_type(tag & 7)

        try:
            return cls.from_schema(schema, payload)
        except ParseError as error:
            raise DecodeError(error.message, offset=offset + error.column) from error

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        if number:
            writer.write_uint32((number << 3) | 2).fork()

        if self.schema:
            writer.write_uint32(10).write_string(self.schema)
        writer.write_uint32(18).write_bytes(self.value.encode())

        if number:
            writer.ldelim()

        return writer.finish()
