import dataclasses
import datetime

import typing_extensions as typing

from sila import datetime as sila_datetime

from ..protobuf import Reader, WireType, Writer
from .data_type import BasicType
from .timezone import Timezone

if typing.TYPE_CHECKING:
    from ..common import Context


@dataclasses.dataclass
class Date(BasicType[datetime.date]):
    """
    Represents an ISO 8601 date in the Gregorian calendar, with an additional timezone (as an offset from UTC).

    A SiLA date type consists of the top-open interval of exactly one
    day in length, beginning on the beginning moment of each day (in
    each timezone), i.e. 00:00:00, up to but not including 24:00:00
    (which is identical with '00:00:00' of the next day).

    Attributes:
      year: The year of the date value in range [1-9999]. Defaults to
        zero.
      month: The month of the date value in range [1-12]. Defaults to
        zero.
      day: The day of the date value in range [1-31]. Defaults to
        zero.
      timezone: The timezone of the date value. Defaults to UTC.
    """

    year: int = 0
    month: int = 0
    day: int = 0
    timezone: Timezone = dataclasses.field(default_factory=Timezone)

    @typing.overload
    @classmethod
    async def from_native(cls, context: "Context", value: typing.Optional[datetime.date] = None, /) -> typing.Self: ...

    @typing.overload
    @classmethod
    async def from_native(
        cls, context: "Context", /, *, year: int = 0, month: int = 0, day: int = 0, hours: int = 0, minutes: int = 0
    ) -> typing.Self: ...

    @typing.override
    @classmethod
    async def from_native(
        cls,
        context: "Context",
        value: typing.Optional[datetime.date] = None,
        /,
        *,
        year: int = 0,
        month: int = 0,
        day: int = 0,
        hours: int = 0,
        minutes: int = 0,
    ) -> typing.Self:
        if value is None:
            return await cls(
                year=year,
                month=month,
                day=day,
                timezone=await Timezone.from_native(context, hours=hours, minutes=minutes),
            ).validate()

        return await cls(
            year=value.year,
            month=value.month,
            day=value.day,
            timezone=await Timezone.from_native(
                context,
                datetime.timezone(offset)
                if (tzinfo := getattr(value, "tzinfo", None))
                and isinstance(tzinfo, datetime.tzinfo)
                and (offset := tzinfo.utcoffset(None))
                else datetime.timezone.utc,
            ),
        ).validate()

    @typing.override
    async def to_native(self, context: "Context", /) -> datetime.date:
        await self.validate()

        return sila_datetime.date(
            year=int(self.year),
            month=int(self.month),
            day=int(self.day),
            tzinfo=await self.timezone.to_native(context) if self.timezone else None,
        )

    @typing.override
    async def validate(self) -> typing.Self:
        if not isinstance(self.year, int):
            msg = f"Expected year of type 'int', received '{type(self.year).__name__}'."
            raise TypeError(msg)

        if not isinstance(self.month, int):
            msg = f"Expected month of type 'int', received '{type(self.month).__name__}'."
            raise TypeError(msg)

        if not isinstance(self.day, int):
            msg = f"Expected day of type 'int', received '{type(self.day).__name__}'."
            raise TypeError(msg)

        if not (1 <= self.year <= 9999):
            msg = f"Year must be between 1 and 9999, received '{self.year}'."
            raise ValueError(msg)

        if not (1 <= self.month <= 12):
            msg = f"Month must be between 1 and 12, received '{self.month}'."
            raise ValueError(msg)

        if not (1 <= self.day <= 31):
            msg = f"Day must be between 1 and 31, received '{self.day}'."
            raise ValueError(msg)

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
                message.day = reader.read_uint32()
            elif field_number == 2:
                reader.expect_type(tag, WireType.VARINT)
                message.month = reader.read_uint32()
            elif field_number == 3:
                reader.expect_type(tag, WireType.VARINT)
                message.year = reader.read_uint32()
            elif field_number == 4:
                reader.expect_type(tag, WireType.LEN)
                message.timezone = Timezone.decode(reader, reader.read_uint32())
            else:
                reader.skip_type(tag & 7)

        return message

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        if number:
            writer.write_uint32((number << 3) | 2).fork()

        if self.day:
            writer.write_uint32(8).write_uint32(self.day)
        if self.month:
            writer.write_uint32(16).write_uint32(self.month)
        if self.year:
            writer.write_uint32(24).write_uint32(self.year)
        self.timezone.encode(writer, 4)

        if number:
            writer.ldelim()

        return writer.finish()
