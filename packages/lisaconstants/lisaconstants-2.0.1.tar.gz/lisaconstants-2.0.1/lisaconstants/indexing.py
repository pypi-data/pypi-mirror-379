"""
Element indexing
================

Following the DDPC Convention Document, this module primarily defines indexing
conventions for the LISA spacecraft and MOSAs. It also defines convenience
functions to convert or transform these indices.

Any subsystem or quantity uniquely attached to a spacecraft or a MOSA will be
labelled acoording to the latter. For example, the reference interferometer on
the optical bench :math:`ij` will be indexed :math:`ij`.

Preferrably, quantities related to spacecraft or MOSAs should be arranged in the
order given by :attr:`SPACECRAFT` and :attr:`MOSAS`.

Spacecraft indexing
-------------------

.. autodata:: SPACECRAFT


MOSA indexing
-------------

.. autodata:: MOSAS

.. autodata:: LEFT_MOSAS

.. autodata:: RIGHT_MOSAS

.. autodata:: LINKS

Utility functions
-----------------

.. autofunction:: mosa2sc

.. autofunction:: link2sc

.. autofunction:: distant_mosa

.. autofunction:: adjacent_mosa

"""

import numpy as np

SPACECRAFT = np.array([1, 2, 3])
"""Ordered array of spacecraft indices.

Spacecraft are indexed 1, 2, 3, going clockwise when looking down from the
ecliptic North, i.e. when looking down at the solar panels.

Spacecraft 1 is the reference spacecraft, i.e. the spacecraft on top of the
stack and the first to be separated from the upper stage.

Note that at the time of the writing, this required confirmation but matches
current ESA conventions.
"""

MOSAS = np.array([12, 23, 31, 13, 32, 21])
r"""Ordered array of MOSA indices.

The moavable optical sub-assemblies (MOSAs) are labelled with two indices
:math:`ij`. The former matches the index :math:`i` of the hosting spacecraft
(i.e. the local spacecraft) while the second index is that of the spacecraft
:math:`j` exchanging light with the considered MOSA (i.e. the distance
spacecraft).

In other words, the first index :math:`i` denotes the receiving spacecraft and
the second index :math:`j` denotes the emitting spacecraft. For example,

.. math::

    \mathbf{r}_{ij} = \mathbf{x}_i - \mathbf{x}_j.

The same convention is used to denote the light trabel time (LTT) :math:`L_{ij}`
from spacecraft :math:`j` to :math:`i`, which can only be measured on the
similarly-indexed optical bench :math:`ij`.
"""

LEFT_MOSAS = np.array([12, 23, 31])
"""Ordered array of left-side MOSA indices."""

RIGHT_MOSAS = np.array([13, 32, 21])
"""Ordered array of right-side MOSA indices."""

LINKS = MOSAS
"""Ordered array of link indices.

This is the same as :attr:`MOSAS`, as links can be uniquely attached to the MOSA
on which link quantities can be measured.
"""


def link2sc(link: int) -> tuple[int, int]:
    """Convert link to emitter and receiver spacecraft indices.

    Parameters
    ----------
    link:
        Link index.

    Returns
    -------
    Tuple of emitter and receiver spacecraft indices.

    Raises
    ------
    ValueError
        If the passed link index is invalid.
    """
    # Check we have a valid link index
    if link not in LINKS:
        raise ValueError(f"Invalid link index '{link}'")

    rec = int(str(link)[0])
    emi = int(str(link)[1])
    return emi, rec


def mosa2sc(mosa: int) -> tuple[int, int]:
    """Convert MOSA to local and distant spacecraft indices.

    Parameters
    ----------
    mosa:
        MOSA index.

    Returns
    -------
    Tuple of local and distant spacecraft indices.

    Raises
    ------
    ValueError
        If the passed MOSA index is invalid.
    """
    # Check we have a valid link index
    if mosa not in MOSAS:
        raise ValueError(f"Invalid MOSA index '{mosa}'")

    loc = int(str(mosa)[0])
    dist = int(str(mosa)[1])
    return loc, dist


def distant_mosa(mosa: int) -> int:
    """Return the index of the distant MOSA.

    .. code-block:: python

        distants = distant_mosa(MOSAS)

    Parameters
    ----------
    mosa:
        MOSA index.

    Returns
    -------
    Distant MOSA index.

    Raises
    ------
    ValueError
        If the passed MOSA index is invalid.
    """
    # Check we have a valid link index
    if mosa not in MOSAS:
        raise ValueError(f"Invalid MOSA index '{mosa}'")

    loc = str(mosa)
    dist = f"{loc[1]}{loc[0]}"
    return int(dist)


def adjacent_mosa(mosa: int) -> int:
    """Return the index of the adjacent MOSA.

    .. code-block:: python

        adjacents = adjacent_mosa(MOSAS)

    Parameters
    ----------
    mosa:
        MOSA index.

    Returns
    -------
    Adjacent MOSA index.

    Raises
    ------
    ValueError
        If the passed MOSA index is invalid.
    """
    # Check we have a valid link index
    if mosa not in MOSAS:
        raise ValueError(f"Invalid MOSA index '{mosa}'")

    loc = str(mosa)
    all_sc = set(SPACECRAFT)
    all_sc.remove(int(loc[0]))
    all_sc.remove(int(loc[1]))
    # Only the third SC index should remain
    assert len(all_sc) == 1
    third_sc = all_sc.pop()

    adj = f"{loc[0]}{third_sc}"
    return int(adj)
