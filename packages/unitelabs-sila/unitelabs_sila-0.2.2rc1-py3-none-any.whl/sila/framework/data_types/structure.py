import collections.abc
import dataclasses

import typing_extensions as typing

from ..fdl import Characters, Deserializer, EndElement, Serializer, StartElement
from ..protobuf import ConversionError, DecodeError, Reader, WireType, Writer
from ..validators import check_display_name, check_identifier
from .any import Any
from .convertable import Native
from .data_type import DataType
from .element import Element

if typing.TYPE_CHECKING:
    from ..common import Context

T = typing.TypeVar("T", bound=dict[str, Native])


@dataclasses.dataclass
class Structure(DataType[T]):
    """
    A structure composed of one or more named elements with the same or different SiLA types.

    Attributes:
      presence: A list of element names that were present in the
        protobuf message.
      **kwargs: Key and value pairs of the SiLA structure instances.
    """

    elements: typing.ClassVar[dict[str, Element]] = {}

    value: dict[str, DataType] = dataclasses.field(default_factory=dict)

    @typing.override
    @classmethod
    async def from_native(cls, context: "Context", value: typing.Optional[T] = None, /) -> typing.Self:
        value = value or {}

        structure = cls()
        for name, element in cls.elements.items():
            item = value.get(name, None)

            if item is None and not issubclass(element.data_type, Any):
                msg = f"Missing field '{element.identifier}' in message '{cls.__name__}'."
                raise ConversionError(msg, [element.identifier])

            try:
                structure.value[name] = await element.data_type.from_native(context, item)
            except ConversionError as error:
                raise ConversionError(error.message, [element.identifier, *error.path]) from error
            except Exception as error:  # noqa: BLE001
                raise ConversionError(str(error), [element.identifier]) from None

        return await structure.validate()

    @typing.override
    async def to_native(self, context: "Context", /) -> T:
        await self.validate()

        values: T = typing.cast(T, {})
        for name, element in self.elements.items():
            if name not in self.value:
                msg = f"Missing field '{element.identifier}' in message '{self.__class__.__name__}'."
                raise ConversionError(msg, [element.identifier])

            item = self.value.get(name, element.data_type())
            if not isinstance(item, element.data_type):
                msg = f"Expected value of type '{element.data_type.__name__}', received '{type(item).__name__}'."
                raise ConversionError(msg, [element.identifier])

            try:
                values[name] = await item.to_native(context)
            except ConversionError as error:
                raise ConversionError(error.message, [element.identifier, *error.path]) from None
            except Exception as error:  # noqa: BLE001
                raise ConversionError(str(error), [element.identifier]) from None

        return values

    @typing.override
    async def validate(self) -> typing.Self:
        return self

    @typing.override
    @classmethod
    def decode(cls, reader: typing.Union[Reader, bytes], length: typing.Optional[int] = None) -> typing.Self:
        from .constrained import Constrained
        from .list import List

        reader = reader if isinstance(reader, Reader) else Reader(reader)

        message = cls()
        end = reader.length if length is None else reader.cursor + length

        elements = list(cls.elements.items())
        while reader.cursor < end:
            pos = reader.cursor
            tag = reader.read_uint32()
            index = (tag >> 3) - 1

            if index >= len(elements):
                reader.skip_type(tag & 7)
                continue

            reader.expect_type(tag, WireType.LEN)
            name, element = elements[index]

            try:
                if issubclass(element.data_type, List) or (
                    issubclass(element.data_type, Constrained) and issubclass(element.data_type.data_type, List)
                ):
                    if name not in message.value:
                        values = element.data_type.decode(reader.buffer[pos:end])
                        message.value[name] = values

                    reader.skip_type(tag & 7)
                else:
                    value = element.data_type.decode(reader, reader.read_uint32())
                    message.value[name] = value
            except DecodeError as error:
                msg = f"Invalid field '{element.identifier}' in message '{cls.__name__}': {error.message}"
                raise DecodeError(msg, error.offset, [element.identifier, *error.path]) from None

        return message

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        if number:
            writer.write_uint32((number << 3) | 2).fork()

        for field_number, (name, element) in enumerate(self.elements.items(), start=1):
            value = self.value.get(name, None) or element.data_type()

            value.encode(writer, field_number)

        if number:
            writer.ldelim()

        return writer.finish()

    @typing.override
    @classmethod
    def serialize(cls, serializer: Serializer) -> None:
        serializer.start_element("DataType")
        serializer.start_element("Structure")

        for element in cls.elements.values():
            serializer.start_element("Element")
            serializer.write_str("Identifier", element.identifier)
            serializer.write_str("DisplayName", element.display_name)
            serializer.write_str("Description", element.description)
            element.data_type.serialize(serializer)
            serializer.end_element("Element")

        serializer.end_element("Structure")
        serializer.end_element("DataType")

    @typing.override
    @classmethod
    def deserialize(cls, deserializer: Deserializer) -> collections.abc.Generator[None, typing.Any, type[typing.Self]]:
        yield from deserializer.read_start_element(name="Structure")

        elements: dict[str, Element] = {}
        while True:
            token = yield

            if isinstance(token, StartElement):
                if token.name == "Element":
                    # Identifier
                    yield from deserializer.read_start_element("Identifier")
                    identifier = yield from deserializer.read_str()
                    check_identifier(identifier)
                    yield from deserializer.read_end_element("Identifier")

                    # DisplayName
                    yield from deserializer.read_start_element("DisplayName")
                    display_name = yield from deserializer.read_str()
                    check_display_name(display_name)
                    yield from deserializer.read_end_element("DisplayName")

                    # Description
                    yield from deserializer.read_start_element("Description")
                    description = yield from deserializer.read_str()
                    yield from deserializer.read_end_element("Description")

                    # DataType
                    data_type = yield from deserializer.read(DataType.deserialize(deserializer))

                    elements[identifier] = Element(
                        identifier=identifier,
                        display_name=display_name,
                        description=description,
                        data_type=data_type,
                    )
                else:
                    msg = (
                        f"Expected start element with name 'Element', received start element with name '{token.name}'."
                    )
                    raise ValueError(msg)

            elif isinstance(token, EndElement):
                if token.name == "Element":
                    continue
                else:
                    break  # pragma: no cover

            elif isinstance(token, Characters):
                msg = f"Expected start element with name 'Element', received characters '{token.value}'."
                raise ValueError(msg)

        if not elements:
            msg = "Expected at least one 'Element' element inside the 'Structure' element."
            raise ValueError(msg)

        return cls.create(elements)

    @classmethod
    def create(
        cls,
        elements: typing.Optional[dict[str, Element]] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
    ) -> type[typing.Self]:
        """
        Create a new SiLA `Structure` class with the provided elements.

        Args:
          elements: A mapping of names and their corresponding SiLA
            elements.
          name: An optional name for the new `Structure` class.
          description: An optional description for the new `Structure` class.

        Returns:
          A new `Structure` class with the specified elements.
        """

        elements = elements or {}

        return dataclasses.make_dataclass(
            name or cls.__name__,
            [],
            bases=(cls,),
            namespace={"__doc__": description, "elements": elements},
            eq=False,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Structure):
            return NotImplemented

        return (
            self.elements.keys() == other.elements.keys()
            and all(
                a.identifier == b.identifier
                and a.display_name == b.display_name
                and a.description == b.description
                and a.data_type.__name__ == b.data_type.__name__
                for a, b in zip(self.elements.values(), other.elements.values())
            )
            and self.value == other.value
        )
