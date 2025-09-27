"""
Implementation of the base classes for the lisaconstants package.
"""

from __future__ import annotations

import enum
import typing as t

from ._error import LisaConstantsException


class ConstantNameAlreadyDefined(LisaConstantsException):
    """Exception raised when a constant or alias with same name already exists."""


class ConstantNameUndefined(LisaConstantsException):
    """Exception raised when refering to a constant name which is undefined."""


class Error(enum.Enum):
    """Enumeration of possible values for error argument."""

    EXACT = "Exact"
    """Value defined exactly."""

    EXACT_NUMERICAL = "Exact (numerical approximation)"
    """Value defined through numerical approximation up to machine precision."""

    UNDEFINED = "Undefined"
    """Value precision is unspecified."""

    def __str__(self) -> str:
        return self.value


T = t.TypeVar("T")


def _make_into_list(value: list[T] | T | None) -> list[T]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


_all_constants: dict[str, Constant] = {}
"""Dictionary of all defined constants with their names as keys.

This dictionary is automatically populated when a new Constant is created. Use
:func:`get_all_constants` to access it.
"""

_all_aliases: dict[str, Alias] = {}
"""Dictionary of all defined aliases with their names as keys.

This dictionary is automatically populated when a new Alias is created. Use
:func:`get_all_aliases` to access it.
"""


class Constant(t.Generic[T]):
    """Definition of a constant with associated metadata.

    Args:
        name: Constant name.
        value: Constant value.
        unit: Associated unit, or None.
        description: Short one-liner description.
        error: Uncertainty on value.
        references: List of references.
        longdescr: Long multi-line description.
        aliases: Name(s) of constant alias(es).

    Raises:
        ConstantNameAlreadyDefined: If a constant or alias with the same name
            already exists.
    """

    # pylint: disable=too-many-instance-attributes

    name: str
    """Original name of the constant."""

    value: T
    """Constant value."""

    unit: str | None
    """Unit of the value."""

    description: str
    """Constant short one-liner description."""

    error: Error
    """Uncertainty on value."""

    references: list[str]
    """List of references, possibly empty."""

    longdescr: str | None
    """Long multi-line description."""

    _aliases: list[Alias[T]]

    def __init__(
        self,
        name: str,
        value: T,
        description: str,
        *,
        unit: str | None = None,
        error: Error = Error.UNDEFINED,
        references: list[str] | str | None = None,
        longdescr: str | None = None,
        aliases: list[str] | str | None = None,
    ) -> None:
        self.name = name
        self.value = value
        self.description = description
        self.unit = unit
        self.error = error
        self.references = _make_into_list(references)
        self.longdescr = longdescr
        self._aliases = []

        for alias in _make_into_list(aliases):
            self.add_alias(alias)

        if (name in _all_constants) or (name in _all_aliases):
            raise ConstantNameAlreadyDefined(f"Constant of {name=} is already defined")
        _all_constants[name] = self

    def __repr__(self) -> str:
        if self.unit is None:
            return f"<{self.name} ({self.value})>"
        return f"<{self.name} ({self.value} {self.unit})>"

    def add_alias(self, name: str) -> Alias[T]:
        """Add an alias to the constant."""

        alias = Alias(name, self)
        self._aliases.append(alias)
        return alias

    @property
    def aliases(self) -> t.Sequence[Alias]:
        """Return sequence of aliases attached to this constant."""
        return self._aliases

    @property
    def all_names(self) -> t.Sequence[str]:
        """All names (including aliases) for this constant."""
        return [self.name] + [alias.name for alias in self.aliases]


class Alias(t.Generic[T]):
    """Alias of a Constant.

    Args:
        name: Alias name.
        constant: Aliased constant instance.
    """

    # pylint: disable=too-few-public-methods

    name: str
    """Alias name."""

    constant: Constant[T]
    """Aliased constant instance."""

    def __init__(self, name: str, constant: Constant[T]) -> None:
        self.name = name
        self.constant = constant

        if (name in _all_constants) or (name in _all_aliases):
            raise ConstantNameAlreadyDefined(f"Constant of {name=} is already defined")
        _all_aliases[name] = self

    @property
    def constant_name(self) -> str:
        """Original name of the associated constant."""
        return self.constant.name

    def __repr__(self) -> str:
        if self.constant.unit is None:
            return f"<{self.name} [{self.constant_name}] ({self.constant.value})>"
        return f"<{self.name} [{self.constant_name}] ({self.constant.value} {self.constant.unit})>"


def get_all_constants() -> t.Mapping[str, Constant]:
    """Return a dictionnary of all constants with their names as keys."""
    return _all_constants


def get_all_aliases() -> t.Mapping[str, Alias]:
    """Return a dictionnary of all aliases with their names as keys."""
    return _all_aliases


def get_constant(name: str) -> Constant:
    """Return a constant by its name (or an alias name).

    Args:
        name: Name of the constant or alias.

    Raises:
        ConstantNameUndefined: If the name is not defined as a constant or an alias.
    """
    if name in _all_constants:
        return _all_constants[name]
    if name in _all_aliases:
        return _all_aliases[name].constant
    raise ConstantNameUndefined(f"{name} is neither a Constant nor an Alias.")


def get_constant_or_alias(name: str) -> Constant | Alias:
    """Return a constant or an alias by its name.

    Args:
        name: Name of the constant or alias.

    Raises:
        ConstantNameUndefined: If the name is not defined as a constant or an alias.
    """
    if name in _all_aliases:
        return _all_aliases[name]
    if name in _all_constants:
        return _all_constants[name]
    raise ConstantNameUndefined(f"{name} is neither a Constant nor an Alias.")
