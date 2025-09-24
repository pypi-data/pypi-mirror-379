import dataclasses

import typing_extensions as typing

from ..protobuf import Reader, WireType, Writer
from .data_type import BasicType

if typing.TYPE_CHECKING:
    from ..common import Context


@dataclasses.dataclass
class Boolean(BasicType[bool]):
    """
    Represents a boolean value.

    Attributes:
      value: The encapsulated boolean value. Defaults to false.
    """

    value: bool = False

    @typing.override
    @classmethod
    async def from_native(cls, context: "Context", value: typing.Optional[bool] = None, /) -> typing.Self:
        if value is None:
            return await cls().validate()

        return await cls(value=value).validate()

    @typing.override
    async def to_native(self, context: "Context", /) -> bool:
        await self.validate()

        return self.value

    @typing.override
    async def validate(self) -> typing.Self:
        if not isinstance(self.value, bool):
            msg = f"Expected value of type 'bool', received '{type(self.value).__name__}'."
            raise TypeError(msg)

        return self

    @typing.override
    @classmethod
    def decode(cls, reader: typing.Union[Reader, bytes], length: typing.Optional[int] = None) -> typing.Self:
        reader = reader if isinstance(reader, Reader) else Reader(reader)

        message = cls()
        end = reader.length if length is None else reader.cursor + length

        while reader.cursor < end:
            tag = reader.read_uint32()
            field_number = tag >> 3

            if field_number == 1:
                reader.expect_type(tag, WireType.VARINT)
                message.value = reader.read_bool()
            else:
                reader.skip_type(tag & 7)

        return message

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        if number:
            writer.write_uint32((number << 3) | 2).fork()

        if self.value:
            writer.write_uint32(8).write_bool(self.value)

        if number:
            writer.ldelim()

        return writer.finish()
