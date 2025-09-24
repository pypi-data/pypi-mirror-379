from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from typing import Callable, Generic, Iterator, Mapping, Sequence, TypeVar

TItem_co = TypeVar("TItem_co", covariant=True)
TItem = TypeVar("TItem")
TOther = TypeVar("TOther")


@dataclass(frozen=True)
class MaybeNamedCollection(Generic[TItem_co]):
    positional_items: Sequence[TItem_co]
    named_items: Mapping[str, TItem_co] = dataclasses.field(default_factory=dict)

    def zip(self, other: MaybeNamedCollection[TOther]) -> MaybeNamedCollection[tuple[TItem_co, TOther]]:
        if set(self.named_items) != set(other.named_items):
            raise ValueError("Cannot zip collections with different item names")
        return MaybeNamedCollection(
            positional_items=list(zip(self.positional_items, other.positional_items, strict=True)),
            named_items={name: (item, other.named_items[name]) for name, item in self.named_items.items()},
        )

    def enumerate(self) -> Iterator[tuple[int | str, TItem_co]]:
        yield from enumerate(self.positional_items)
        yield from self.named_items.items()

    def map(self, fn: Callable[[TItem_co], TOther]) -> MaybeNamedCollection[TOther]:
        return MaybeNamedCollection(
            positional_items=[fn(item) for item in self.positional_items],
            named_items={name: fn(item) for name, item in self.named_items.items()},
        )

    def pprint(self):
        return f"({', '.join([str(x) for x in self.positional_items] + [f'{name}={item}' for name, item in self.named_items.items()])})"

    def get(self, location: int | str) -> TItem_co:
        if isinstance(location, int):
            return self.positional_items[location]
        return self.named_items[location]

    def has_exactly_n_and_only_positional_items(self, n: int) -> bool:
        return len(self.positional_items) == n and len(self.named_items) == 0

    def has_exactly_n_positional_items(self, n: int) -> bool:
        return len(self.positional_items) == n


@dataclass(frozen=True)
class MaybeNamedCollectionBuilder(MaybeNamedCollection[TItem], Generic[TItem]):
    positional_items: list[TItem] = dataclasses.field(default_factory=list)
    named_items: dict[str, TItem] = dataclasses.field(default_factory=dict)

    def add(self, location: int | str, item: TItem):
        if isinstance(location, int):
            if location != len(self.positional_items):
                raise ValueError("Cannot add to a specific index in a positional collection")
            self.positional_items.append(item)
        else:
            self.named_items[location] = item
