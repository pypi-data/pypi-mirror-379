import collections.abc
import dataclasses

import typing_extensions as typing

from ..constraints import (
    AllowedTypes,
    Constraint,
    ContentType,
    ElementCount,
    FullyQualifiedIdentifier,
    Length,
    MaximalElementCount,
    MaximalExclusive,
    MaximalInclusive,
    MaximalLength,
    MinimalElementCount,
    MinimalExclusive,
    MinimalInclusive,
    MinimalLength,
    Pattern,
    Schema,
    Set,
    Unit,
)
from ..fdl import Characters, Deserializer, EndElement, Serializer, StartElement
from ..protobuf import Reader, Writer
from .any import Any
from .convertable import Native
from .data_type import BasicType, DataType

if typing.TYPE_CHECKING:
    from ..common import Context
    from .list import List
    from .void import Void

T = typing.TypeVar("T", bound=Native)


@dataclasses.dataclass
class Constrained(DataType[T]):
    """
    a SiLA basic or list type with one or more constraints.

    Multiple constraints act together as a logical conjunction (and).

    Attributes:
      data_type: The SiLA data type of the constrained value.
      constraints: The list of constraints that must be satisfied by
        the constrained value.
      value: The SiLA data type instance.
    """

    data_type: typing.ClassVar[type[typing.Union[BasicType, "List"]]] = Any
    constraints: typing.ClassVar[collections.abc.Sequence["Constraint"]] = []

    value: typing.Union[BasicType, "List"] = dataclasses.field(default_factory=Any)

    @typing.override
    @classmethod
    async def from_native(cls, context: "Context", value: typing.Optional[T] = None, /) -> typing.Self:
        for constraint in cls.constraints:
            await constraint.validate(value)

        return await cls(value=await cls.data_type.from_native(context, value)).validate()

    @typing.override
    async def to_native(self, context: "Context", /) -> T:
        await self.validate()

        value = await self.value.to_native(context)

        for constraint in self.constraints:
            await constraint.validate(value)

        return value

    @typing.override
    async def validate(self) -> typing.Self:
        if not isinstance(self.value, self.data_type):
            msg = f"Expected value of type '{self.data_type.__name__}', received '{type(self.value).__name__}'."
            raise TypeError(msg)

        return self

    @typing.override
    @classmethod
    def decode(cls, reader: typing.Union[Reader, bytes], length: typing.Optional[int] = None) -> typing.Self:
        from .list import List

        reader = reader if isinstance(reader, Reader) else Reader(reader)

        message = cls()
        end = reader.length if length is None else reader.cursor + length

        while reader.cursor < end:
            if isinstance(message.value, List):
                if not message.value.value:
                    message.value = message.data_type.decode(reader, length)
                    break
            else:
                message.value = message.data_type.decode(reader, length)

        return message

    @typing.override
    def encode(self, writer: typing.Optional[Writer] = None, number: typing.Optional[int] = None) -> bytes:
        writer = writer or Writer()

        self.value.encode(writer, number)

        return writer.finish()

    @typing.override
    @classmethod
    def serialize(cls, serializer: Serializer) -> None:
        serializer.start_element("DataType")
        serializer.start_element("Constrained")
        cls.data_type.serialize(serializer)
        serializer.start_element("Constraints")
        for constraint in cls.constraints:
            constraint.serialize(serializer)
        serializer.end_element("Constraints")
        serializer.end_element("Constrained")
        serializer.end_element("DataType")

    @typing.override
    @classmethod
    def deserialize(
        cls, deserializer: Deserializer
    ) -> collections.abc.Generator[None, typing.Any, typing.Union[type["Void"], type["Constrained"]]]:
        from .list import List
        from .string import String
        from .void import Void

        yield from deserializer.read_start_element(name="Constrained")

        data_type = yield from deserializer.read(DataType.deserialize(deserializer))

        if not issubclass(data_type, (BasicType, List)):
            msg = f"Expected constraint's data type to be 'BasicType' or 'List', received '{data_type.__name__}'."
            raise ValueError(msg)

        yield from deserializer.read_start_element(name="Constraints")

        constraints: list[Constraint] = []
        while True:
            token = yield from deserializer.peek()

            if isinstance(token, StartElement):
                if token.name == "Length":
                    constraint = yield from deserializer.read(Length.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MinimalLength":
                    constraint = yield from deserializer.read(MinimalLength.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MaximalLength":
                    constraint = yield from deserializer.read(MaximalLength.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "Set":
                    constraint = yield from deserializer.read(Set.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "Pattern":
                    constraint = yield from deserializer.read(Pattern.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MaximalExclusive":
                    constraint = yield from deserializer.read(MaximalExclusive.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MaximalInclusive":
                    constraint = yield from deserializer.read(MaximalInclusive.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MinimalExclusive":
                    constraint = yield from deserializer.read(MinimalExclusive.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MinimalInclusive":
                    constraint = yield from deserializer.read(MinimalInclusive.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "Unit":
                    constraint = yield from deserializer.read(Unit.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "ContentType":
                    constraint = yield from deserializer.read(ContentType.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "ElementCount":
                    constraint = yield from deserializer.read(ElementCount.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MinimalElementCount":
                    constraint = yield from deserializer.read(MinimalElementCount.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "MaximalElementCount":
                    constraint = yield from deserializer.read(MaximalElementCount.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "FullyQualifiedIdentifier":
                    constraint = yield from deserializer.read(
                        FullyQualifiedIdentifier.deserialize(deserializer, data_type)
                    )
                    constraints.append(constraint)
                elif token.name == "Schema":
                    constraint = yield from deserializer.read(Schema.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                elif token.name == "AllowedTypes":
                    constraint = yield from deserializer.read(AllowedTypes.deserialize(deserializer, data_type))
                    constraints.append(constraint)
                else:
                    msg = (
                        f"Expected start element with a constraint name, "
                        f"received start element with name '{token.name}'."
                    )
                    raise ValueError(msg)

            elif isinstance(token, EndElement):
                if token.name == "Constraints":
                    yield from deserializer.read_end_element("Constraints")
                    break
                else:
                    break  # pragma: no cover

            elif isinstance(token, Characters):
                msg = f"Expected start element with a constraint name, received characters '{token.value}'."
                raise ValueError(msg)

        yield from deserializer.read_end_element(name="Constrained")

        if data_type == String and constraints == [Length(0)]:
            return Void

        return cls.create(data_type, constraints)

    @classmethod
    def create(
        cls,
        data_type: type[typing.Union[BasicType, "List"]] = Any,
        constraints: typing.Optional[collections.abc.Sequence["Constraint"]] = None,
        name: str = "",
    ) -> type[typing.Self]:
        """
        Create a new SiLA `Constrained` class with the provided data type and constraints.

        Args:
          data_type: The SiLA data type of the constrained value.
          constraints: A sequence of constraints to apply to the data
            type.
          name: An optional name for the new `Constrained` class.

        Returns:
          A new `Constrained` class with the specified data type.
        """

        return dataclasses.make_dataclass(
            name or cls.__name__,
            [("value", data_type, dataclasses.field(default_factory=data_type))],
            bases=(cls,),
            namespace={"data_type": data_type, "constraints": constraints or []},
            eq=False,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Constrained):
            return NotImplemented

        return (
            self.data_type.__name__ == other.data_type.__name__
            and self.constraints == other.constraints
            and self.value == other.value
        )
