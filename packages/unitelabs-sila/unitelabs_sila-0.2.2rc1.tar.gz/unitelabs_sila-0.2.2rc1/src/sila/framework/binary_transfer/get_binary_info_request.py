import dataclasses

import typing_extensions as typing

from ..protobuf import Message, Reader, WireType, Writer


@dataclasses.dataclass
class GetBinaryInfoRequest(Message):
    """
    Retrieve information about a specific binary transfer session.

    Attributes:
      binary_transfer_uuid: A unique identifier (UUID) for the binary
        transfer session about which information is being requested.
    """

    binary_transfer_uuid: str = ""

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
                reader.expect_type(tag, WireType.LEN)
                message.binary_transfer_uuid = reader.read_string()
            else:
                reader.skip_type(tag & 7)

        return message

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        if number:
            writer.write_uint32((number << 3) | 2).fork()

        if self.binary_transfer_uuid:
            writer.write_uint32(10).write_string(self.binary_transfer_uuid)

        if number:
            writer.ldelim()

        return writer.finish()
