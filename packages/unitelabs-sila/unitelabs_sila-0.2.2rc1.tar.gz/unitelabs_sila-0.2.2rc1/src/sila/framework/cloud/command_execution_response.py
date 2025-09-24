import dataclasses

import typing_extensions as typing

from ..command import CommandExecutionInfo, CommandExecutionUUID
from ..protobuf import Message, Reader, WireType, Writer


@dataclasses.dataclass
class CommandExecutionResponse(Message):
    """
    Message to execute a SiLA command.

    Attributes:
      fully_qualified_command_id: The fully qualified identifier of
        the command to be executed.
      command_parameter: The command parameters.
    """

    command_execution_uuid: CommandExecutionUUID = dataclasses.field(default_factory=CommandExecutionUUID)
    execution_info: CommandExecutionInfo = dataclasses.field(default_factory=CommandExecutionInfo)

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
                message.command_execution_uuid = CommandExecutionUUID.decode(reader, reader.read_uint32())
            elif field_number == 2:
                reader.expect_type(tag, WireType.LEN)
                message.execution_info = CommandExecutionInfo.decode(reader, reader.read_uint32())
            else:
                reader.skip_type(tag & 7)

        return message

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        if number:
            writer.write_uint32((number << 3) | 2).fork()

        self.command_execution_uuid.encode(writer, 1)
        self.execution_info.encode(writer, 2)

        if number:
            writer.ldelim()

        return writer.finish()
