"""
Astropy
=======

This module allows to define and manage mappings between constants defined in
`lisaconstants` and their counterparts in :py:mod:`astropy.constants`. It provides
functions to register mappings, retrieve them, and check for inconsistencies
between the two libraries.

Defining a mapping
------------------

To define a mapping between a LISA constant and an `astropy` constant,
use the :py:func:`register_mapping` function:

.. code-block:: python

    from lisaconstants.compat.astropy import register_mapping

    # Create a mapping between lisaconstants.SPEED_OF_LIGHT and astropy.constants.c
    register_mapping("SPEED_OF_LIGHT", "c")


If a value difference is expected between the two libraries, you can specify
an `offset` parameter to register this expected difference in the mapping.

.. autofunction:: register_mapping

Retrieving a mapping
--------------------

To retrieve a mapping for a specific `lisaconstants` constant, use
:py:func:`get_mapping`. If such a mapping does not exist for the requested
constant, it will return `None`.

.. autofunction:: get_mapping

Detecting inconsistencies
-------------------------

.. attention::
  Following methods can only be used if `astropy` is installed in the python environment.

To ensure that the constants defined in `lisaconstants` are consistent with
their `astropy` counterparts in the `astropy` version you have locally installed,
you can use the :py:func:`find_mismatched_constants` function. It will return a
list of objects for each mismatched constant, which includes the `lisaconstants`
name, the `astropy` name, the expected offset, and the actual values from both
libraries. If this list is empty, it means all constants are consistent.

The function :py:func:`perform_importtime_consistency_check` is automatically called
when the `lisaconstants` package is first imported.

.. autofunction:: find_mismatched_constants

.. autofunction:: perform_importtime_consistency_check

API Reference
-------------

.. autoclass:: lisaconstants.compat.astropy.Mapping
   :members:

.. autoexception:: lisaconstants.compat.astropy.AstropyUnavailable
    :show-inheritance:

.. autoexception:: lisaconstants.compat.astropy.AstropyConstantUndefined
    :show-inheritance:

"""

import dataclasses
import importlib.metadata
import os
import warnings

from .._constants import Constant
from .._error import LisaConstantsException

ASTROPY_AVAILABLE: bool

try:
    import astropy.constants

    ASTROPY_AVAILABLE = True
except ImportError:
    ASTROPY_AVAILABLE = False

REFERENCE_VERSION: str = "7.1.0"
"""Reference version of astropy for constants consistency."""


@dataclasses.dataclass
class Mapping:
    """Definition of lisaconstants to astropy mapping."""

    lisaconstants_name: str
    """Name of the mapped lisaconstants constant."""

    astropy_name: str
    """Name of the mapped astropy constant."""

    comment: str | None = None
    """Optional comment for this mapping."""

    expected_offset: float = 0.0
    """Expected offset between lisaconstants and astropy values."""


LISA2ASTROPY_CONSTANT_MAPPING: dict[str, Mapping] = {}
"""Mapping of lisaconstants to astropy."""


class AstropyUnavailable(LisaConstantsException):
    """Exception raised when astropy is not available."""


class AstropyConstantUndefined(LisaConstantsException):
    """Exception raised when trying to import an undefined astropy constant."""


class AstropyConstantInconsistent(LisaConstantsException):
    """Exception raised when a constant is inconsistent with its astropy counterpart."""

    def __init__(self, mapping: Mapping, lisa_value: float, astropy_value: float):
        super().__init__(
            f"Constant '{mapping.lisaconstants_name}' is inconsistent with "
            f"astropy constant '{mapping.astropy_name}': "
            f"lisaconstants value {lisa_value} != astropy value {astropy_value} "
            f"(absolute difference: {abs(lisa_value - astropy_value)}, "
            f"expected difference: {mapping.expected_offset})"
        )
        self.mapping = mapping
        self.lisa_value = lisa_value
        self.astropy_value = astropy_value


def register_mapping(
    lisaconstants_name: str,
    astropy_name: str,
    comment: str | None = None,
    offset: float = 0.0,
) -> None:
    """Register a mapping between a LISA constant and an Astropy constant.

    Args:
        lisaconstants_name: Name of the LISA constant.
        astropy_name: Name of the Astropy constant.
        comment: Optional comment for this mapping.
        offset: Optional expected offset between lisaconstants and astropy values.

    """
    LISA2ASTROPY_CONSTANT_MAPPING[lisaconstants_name] = Mapping(
        lisaconstants_name=lisaconstants_name,
        astropy_name=astropy_name,
        comment=comment,
        expected_offset=offset,
    )


def get_mapping(lisaconstant: str | Constant) -> Mapping | None:
    """Get the astropy mapping of a specific LISA Constant (if defined).

    Args:
        lisaconstant: Name of the LISA constant or a :py:class:`Constant <lisaconstants.Constant>` object.

    Returns:
        Mapping: The mapping object if it exists.
    """
    lisaconstants_name: str = (
        lisaconstant if isinstance(lisaconstant, str) else lisaconstant.name
    )
    return LISA2ASTROPY_CONSTANT_MAPPING.get(lisaconstants_name, None)


def _detect_inconsistency(mapping: Mapping) -> AstropyConstantInconsistent | None:
    """Detect if value is matching between LISA Constants and astropy."""
    if not ASTROPY_AVAILABLE:
        raise AstropyUnavailable

    from .._constants import (  # pylint: disable=import-outside-toplevel,cyclic-import
        get_constant,
    )

    lisa_constant = get_constant(mapping.lisaconstants_name)
    try:
        astropy_constant = getattr(astropy.constants, mapping.astropy_name)
    except AttributeError as e:
        raise AstropyConstantUndefined from e

    if lisa_constant.value - astropy_constant.value != mapping.expected_offset:
        return AstropyConstantInconsistent(
            mapping=mapping,
            lisa_value=lisa_constant.value,
            astropy_value=astropy_constant.value,
        )

    return None


def find_mismatched_constants() -> list[AstropyConstantInconsistent]:
    """Detect mapped LISA constants which differ from their Astropy counterparts.

    Raises:
        AstropyUnavailable: If astropy is not available.
        AstropyConstantUndefined: If a mapping refers to an undefined astropy constant
    """
    return [
        inconsistency
        for mapping in LISA2ASTROPY_CONSTANT_MAPPING.values()
        if (inconsistency := _detect_inconsistency(mapping)) is not None
    ]


def perform_importtime_consistency_check() -> None:
    """Perform package import-time consistency check with astropy.

    If `astropy` is not available, or if the environment variable
    LISACONSTANTS_DISABLE_RUNTIME_CHECKS is defined, it will return silently.

    Otherwise, it will check for inconsistencies between
    `lisaconstants` and the locally installed `astropy` version.
    If any inconsistencies are found, it will raise a warning with the names of
    the mismatched constants and the recommended version of `astropy`.
    """

    # First check if environment variable LISACONSTANTS_DISABLE_RUNTIME_CHECKS
    # is defined and skip this test if it is
    if os.getenv("LISACONSTANTS_DISABLE_RUNTIME_CHECKS", None) is not None:
        return

    # Find mismatched constants (and return quietly if astropy unavailable)
    try:
        mismatches = find_mismatched_constants()
    except AstropyUnavailable:
        return

    if not mismatches:
        return

    mismatches_names = [m.mapping.lisaconstants_name for m in mismatches]

    # Raise warning if any constant is inconsistent between lisaconstants and
    # astropy
    repo_url = "https://gitlab.esa.int/lisa-sgs/commons/lisa-constants"
    astropy_ver = importlib.metadata.version("astropy")
    list_failed = (
        mismatches_names[0]
        if len(mismatches_names) == 1
        else ", ".join(mismatches_names)
    )
    warnings.warn(
        "The following constants differ between lisaconstants and the "
        f"version of astropy you have installed: {list_failed}. "
        f"The recommended version of astropy is {REFERENCE_VERSION}. "
        "Use a different one at your own risks. \n"
        f"You may also open an issue at {repo_url} to warn that "
        f"lisaconstants is not compatible with astropy v{astropy_ver}"
    )
