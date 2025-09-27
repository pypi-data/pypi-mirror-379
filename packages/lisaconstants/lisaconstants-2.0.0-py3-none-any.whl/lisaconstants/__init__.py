"""
Constants and aliases
=====================

Constant instances represent one physical quantity and the associated metadata,
such as a name, physical unit, uncertainty, detailed description, or a list of
references.

Retrieving all constants
------------------------

To retrieve all available constants or aliases, use the functions
:func:`get_all_constants` and :func:`get_all_aliases`, respectively. They return
a dictionary with constant names or aliases as keys and the corresponding
:class:`Constant` or :class:`Alias` instances as values.

.. autofunction:: lisaconstants.get_all_constants

.. autofunction:: lisaconstants.get_all_aliases

Retrieving a specific constant
------------------------------

To retrieve a specific constant, use the function :func:`get_constant`. If you
pass the name of an alias, the aliased Constant will be returned.

.. autoexception:: LisaConstantsException

.. autoexception:: ConstantNameUndefined
    :show-inheritance:

.. autofunction:: lisaconstants.get_constant

Creating a constant
-------------------

To create a constant, initialize an instance. It will be automatically added to
the dictionary return by the method :meth:`get_all_constants` of all available
constants with names as keys.

.. code-block:: python

    SPEED_OF_LIGHT: Constant = Constant("SPEED_OF_LIGHT",
        value=299792458.0, unit="m s^{-1}", description="Speed of light in a
        vacuum", error="Exact",
    )

.. autoclass:: Constant
    :members:

.. autoclass:: Error
    :members:

.. autoexception:: ConstantNameAlreadyDefined
    :show-inheritance:


Creating an alias
-----------------

Multiple aliases can be associated with a single quantity, i.e., with a single
constant object. Use the instance method :meth:`Constant.add_alias` to create an
alias. All existing aliases can be obtained by the method :meth:`get_all_aliases` and
the aliases of a specific constant can be obtained via the :meth:`Constant.aliases`
property.

.. code-block:: python

    c: Alias = SPEED_OF_LIGHT.add_alias("c")

The recommended way to initialize both a constant, its aliases, and to import
their value into the main package scope is to define them all in
``lisaconstants.__init__.py`` in a single expression:

.. code-block:: python

    SPEED_OF_LIGHT = c = C = Constant("SPEED_OF_LIGHT",
        value=299792458.0, unit="m s^{-1}", description="Speed of light in a
        vacuum", error="Exact", aliases=["c", "C"]
    ).value

.. autoclass:: Alias
    :members:

"""

# pylint: disable=line-too-long

import importlib.metadata

from . import compat, indexing
from ._constants import (
    Alias,
    Constant,
    ConstantNameAlreadyDefined,
    ConstantNameUndefined,
    Error,
    get_all_aliases,
    get_all_constants,
    get_constant,
)
from ._error import LisaConstantsException

# Automatically set by `poetry dynamic-versioning`
__version__ = "2.0.0"
__version_tuple__ = (2, 0, 0)
__author__: str | list[str]
__email__: str | list[str]

try:
    metadata = importlib.metadata.metadata("lisaconstants").json
    __author__ = metadata["author"]
    __email__ = metadata["author_email"]
except importlib.metadata.PackageNotFoundError:
    __author__ = "NotFound"
    __email__ = "NotFound"

# This __all__ definition implies that constants defined below are not imported
# when running
#  from lisaconstants import *
# They must be imported explicitly like
#  from lisaconstants import SPEED_OF_LIGHT, GM_SUN
# This prevent shadowing local variables or constants whose aliases are common
# variable names (like "c", "h", "e" for instance) and force explicit imports.
__all__ = [
    "Constant",
    "Alias",
    "get_all_constants",
    "get_all_aliases",
    "get_constant",
    "ConstantNameAlreadyDefined",
    "ConstantNameUndefined",
    "LisaConstantsException",
    "compat",
    "indexing",
]

#
# Constant definitions
# --------------------
# Place all constant definitions below.

SPEED_OF_LIGHT = c = C = Constant(
    "SPEED_OF_LIGHT",
    value=299792458.0,
    unit="m s^{-1}",
    description="Speed of light in a vacuum",
    error=Error.EXACT,
    references=[
        "P.J. Mohr, B.N. Taylor, D.B. Newell, 9 July 2015, 'The 2014 CODATA Recommended Values of the Fundamental Physical Constants', National Institute of Standards and Technology, Gaithersburg, MD 20899-8401 (http://www.codata.org/)",
        "http://physics.nist.gov/constants (Web Version 7.0). See also the IAU (2009) System of Astronomical Constants (IAU, August 2009, 'IAU 2009 Astronomical Constants', IAU 2009 Resolution B2 adopted at the XXVII-th General Assembly of the IAU. See also IAU, 10 August 2009, 'IAU WG on NSFA Current Best Estimates' (http://maia.usno.navy.mil/NSFA/NSFA_cbe.html)",
    ],
    aliases=["c", "C"],
).value

compat.astropy.register_mapping("SPEED_OF_LIGHT", "c")

PLANCK_CONSTANT = h = Constant(
    "PLANCK_CONSTANT",
    value=6.62607015e-34,
    unit="J Hz^{-1}",
    description="Planck constant",
    error=Error.EXACT,
    references=[
        "The NIST Reference on Constants, Units, and Uncertainty. NIST. 20 May 2019. Retrieved 2021-04-28.",
        "BIPM. 2018-11-16 (https://web.archive.org/web/20181119214326/https://www.bipm.org/utils/common/pdf/CGPM-2018/26th-CGPM-Resolutions.pdf).",
    ],
    aliases="h",
).value

compat.astropy.register_mapping("PLANCK_CONSTANT", "h")

SIDEREALYEAR_J2000DAY = Constant(
    "SIDEREALYEAR_J2000DAY",
    value=365.256363004,
    unit="day",
    description="Sideral year (in ephemeris days) for the J2000.0 epoch",
    references=[
        "J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994, 'Numerical expressions for precession formulae and mean elements for the Moon and the planets', A&A, 282, 663 (1994A&A...282..663S)",
    ],
    longdescr="A sidereal year is the time taken by the Earth to orbit the Sun once with respect to the fixed stars. Hence, it is also the time taken for the Sun to return to the same position with respect to the fixed stars after apparently travelling once around the ecliptic.",
).value

TROPICALYEAR_J2000DAY = Constant(
    "TROPICALYEAR_J2000DAY",
    value=365.242190402,
    unit="day",
    description="Mean tropical year (in ephemeris days) for the J2000.0 epoch",
    references=[
        "J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994, 'Numerical expressions for precession formulae and mean elements for the Moon and the planets', A&A, 282, 663 (1994A&A...282..663S)",
    ],
    longdescr="A tropical year (also known as a solar year) is the time that the Sun takes to return to the same position in the cycle of seasons, as seen from Earth; for example, the time from vernal equinox to vernal equinox, or from summer solstice to summer solstice. This differs from the time it takes Earth to complete one full orbit around the Sun as measured with respect to the fixed stars (the sidereal year) by about 20 minutes because of the precession of the equinoxes.",
).value

ASTRONOMICAL_YEAR = Constant(
    "ASTRONOMICAL_YEAR",
    value=SIDEREALYEAR_J2000DAY * 60 * 60 * 24,
    unit="s",
    description="Astronomical year",
    references=[
        "J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994, 'Numerical expressions for precession formulae and mean elements for the Moon and the planets', A&A, 282, 663 (1994A&A...282..663S)",
    ],
).value

ASTRONOMICAL_UNIT = au = Constant(
    "ASTRONOMICAL_UNIT",
    value=149597870700.0,
    unit="m",
    description="Astronomical unit",
    references=[
        "IAU, August 2012, 'Re-definition of the astronomical unit of length', IAU 2012 Resolution B2 adopted at the XXVIII-th General Assembly of the IAU",
    ],
    longdescr="The astronomical unit (symbol: au) is a unit of length, roughly the distance from Earth to the Sun and equal to about 150 million kilometres (93 million miles) or ~8 light minutes. The actual distance varies by about 3% as Earth orbits the Sun, from a maximum (aphelion) to a minimum (perihelion) and back again once each year. The astronomical unit was originally conceived as the average of Earth's aphelion and perihelion; however, since 2012 it has been defined as exactly 149597870700 m.",
    aliases="au",
).value

compat.astropy.register_mapping("ASTRONOMICAL_UNIT", "au")

PARSEC = PARSEC_METER = Constant(
    "PARSEC",
    value=3.0856775814913674e16,
    unit="m",
    description="Parsec expressed in meters",
    longdescr="The parsec is obtained by the use of parallax and trigonometry, and is defined as the distance at which 1 au subtends an angle of one arcsecond.",
    aliases="PARSEC_METER",
).value
compat.astropy.register_mapping("PARSEC", "pc")

SOLAR_MASS_PARAMETER = GM_SUN = Constant(
    "SOLAR_MASS_PARAMETER",
    value=1.3271244e20,
    unit="m^3 s^{-2}",
    description="Nominal Solar mass parameter",
    longdescr="The nominal Solar mass parameter GM value is adopted as an exact number (see IAU 2015 Resolution B3), given with a precision within which its TCB and TDB values agree.",
    references=[
        "IAU 2015 Resolution B3, passed by the XXIXth IAU General Assembly in Honolulu, 13 August 2015 (https://arxiv.org/pdf/1510.07674)",
    ],
    aliases="GM_SUN",
).value

SUN_SCHWARZSCHILD_RADIUS = Constant(
    "SUN_SCHWARZSCHILD_RADIUS",
    value=2 * GM_SUN / SPEED_OF_LIGHT**2,
    unit="m",
    description="Sun Schwarzschild radius",
).value

GRAVITATIONAL_CONSTANT = NEWTON_CONSTANT = Constant(
    "GRAVITATIONAL_CONSTANT",
    value=6.674080e-11,
    unit="m^3 kg^{-1} s^{-2}",
    description="Newton's universal constant of gravitation",
    longdescr="In Newton's law, it is the proportionality constant connecting the gravitational force between two bodies with the product of their masses and the inverse square of their distance. In the Einstein field equations, it quantifies the relation between the geometry of spacetime and the energy-momentum tensor (also referred to as the stress-energy tensor). It is noted in IAU 2015 Resolution B3 that this constant is one of the least precisely determined constant, and the use of the Solar mass parameter should be prefered (the error is five orders of magnitude smaller). The value here is taken from 2014 CODATA.",
    references=[
        "2014 CODATA (https://physics.nist.gov/cuu/pdf/wallet_2014.pdf)",
        "IAU 2015 Resolution B3, passed by the XXIXth IAU General Assembly in Honolulu, 13 August 2015 (https://arxiv.org/pdf/1510.07674)",
    ],
    aliases="NEWTON_CONSTANT",
).value

compat.astropy.register_mapping(
    "GRAVITATIONAL_CONSTANT", "G", offset=-2.1999999999904385e-15
)

SUN_MASS = SOLAR_MASS = Constant(
    "SUN_MASS",
    value=SOLAR_MASS_PARAMETER / GRAVITATIONAL_CONSTANT,
    unit="kg",
    description="Solar mass",
    longdescr="Value set to SOLAR_MASS_PARAMETER / GRAVITATIONAL_CONSTANT, where `GM_SUN` is the nominal Solar mass parameter and `GRAVITATIONAL_CONSTANT` is an (relatively high-error) estimate of Newton's constant. It is noted in IAU 2015 Resolution B3 that this constant is one of the least precisely determined constant, and the use of the Solar mass parameter should be prefered (the error is five orders of magnitude smaller).",
    references=[
        "2014 CODATA (https://physics.nist.gov/cuu/pdf/wallet_2014.pdf)",
        "IAU 2015 Resolution B3, passed by the XXIXth IAU General Assembly in Honolulu, 13 August 2015 (https://arxiv.org/pdf/1510.07674)",
    ],
    aliases="SOLAR_MASS",
).value

compat.astropy.register_mapping("SUN_MASS", "M_sun", offset=6.554464009287141e25)

SOLAR_RADIUS = Constant(
    "SOLAR_RADIUS",
    value=6.957e8,
    unit="m",
    description="Nominal Solar radius",
    references=[
        "IAU 2015 Resolution B3, passed by the XXIXth IAU General Assembly in Honolulu, 13 August 2015 (https://arxiv.org/pdf/1510.07674)",
    ],
).value

compat.astropy.register_mapping("SOLAR_RADIUS", "R_sun", offset=0.0)

OBLIQUITY = Constant(
    "OBLIQUITY",
    value=84381.406 / (60 * 60),
    unit="deg",
    description="Obliquity of the ecliptic plane",
    longdescr="The Earth obliquity, or axial tilt angle, is the angle between Earth’s axis of rotation and the normal to the Earth's orbital plane around the Sun. It the IAU 2006 value for the obliquity of the ecliptic plane at J2000.0.",
    references=[
        "'Adoption of the P03 Precession Theory and Definition of the Ecliptic', IAU 2006 Resolution B1, XXVIth International Astronomical Union General Assembly",
        "'Precession-nutation procedures consistent with IAU 2006 resolutions', P. T.  Wallace, N.  Capitaine, A&A 459 (3) 981-985 (2006), DOI: 10.1051/0004-6361:20065897",
        "'A new determination of lunar orbital parameters, precession constant and tidal acceleration from LLR measurements', J. Chapront, M. Chapront-Touzé and G. Francou, A&A, 387 2 (2002) 700-709, DOI: https://doi.org/10.1051/0004-6361:20020420",
    ],
).value

ELEMENTARY_CHARGE = e = E = Constant(
    "ELEMENTARY_CHARGE",
    value=1.602176634e-19,
    unit="C",
    description="Elementary positive charge",
    error=Error.EXACT,
    references=[
        "2018 CODATA Value: elementary charge. The NIST Reference on Constants, Units, and Uncertainty. NIST. 20 May 2019. Retrieved 2019-05-20.",
    ],
    longdescr="The elementary charge is the electric charge carried by a single proton or, equivalently, the magnitude of the negative electric charge carried by a single electron.",
    aliases=["e", "E"],
).value

compat.astropy.register_mapping("ELEMENTARY_CHARGE", "e")

BOLTZMANN_CONSTANT = Kb = KB = Constant(
    "BOLTZMANN_CONSTANT",
    value=1.380649e-23,
    unit="J K^{-1}",
    description="Boltzmann constant",
    error=Error.EXACT,
    references=[
        "2018 CODATA Value: Boltzmann constant. The NIST Reference on Constants, Units, and Uncertainty. NIST. 20 May 2019. Retrieved 20 May 2019.",
    ],
    longdescr="The Boltzmann constant is the proportionality factor that relates the average relative kinetic energy of particles in a gas with the thermodynamic temperature of the gas.",
    aliases=["Kb", "KB"],
).value

compat.astropy.register_mapping("BOLTZMANN_CONSTANT", "k_B")

STEFAN_BOLTZMANN_CONSTANT = sigma_SB = Constant(
    "STEFAN_BOLTZMANN_CONSTANT",
    value=5.670374419184429453970e-8,
    unit="kg s^{-3} K^{-4}",
    description="Stefan-Boltzmann constant",
    error=Error.EXACT_NUMERICAL,
    references=[
        "2018 CODATA Value: Stefan-Boltzmann constant. The NIST Reference on Constants, Units, and Uncertainty. NIST. 20 May 2019. Retrieved 2019-05-20.",
    ],
    longdescr="The Stefan-Boltzmann constant is the constant of proportionality in the Stefan-Boltzmann law: 'the total intensity radiated over all wavelengths increases as the temperature increases', of a black body which is proportional to the fourth power of the thermodynamic temperature.",
    aliases="sigma_SB",
).value

compat.astropy.register_mapping(
    "STEFAN_BOLTZMANN_CONSTANT", "sigma_sb", offset=-1.9852334701272664e-23
)

VACUUM_PERMEABILITY = MU0 = Constant(
    "VACUUM_PERMEABILITY",
    value=1.25663706143592e-06,
    unit="kg m s^{-2} A^{-2}",
    description="Magnetic permeability in a vacuum",
    aliases="MU0",
).value

compat.astropy.register_mapping(
    "VACUUM_PERMEABILITY", "mu0", offset=-6.840799018285708e-16
)

FUSED_SILICA_THERMAL_OPD = FOM_Si = Constant(
    "FUSED_SILICA_THERMAL_OPD",
    value=9.82e-6,
    unit="K^{-1}",
    description="Thermal optical path difference change of fused silica",
    aliases="FOM_Si",
).value

FUSED_SILICAL_THERMAL_EXPANSION = exp_Si = Constant(
    "FUSED_SILICAL_THERMAL_EXPANSION",
    value=5e-7,
    unit="K^{-1}",
    description="Thermal expansion of fused silica",
    aliases="exp_Si",
).value

CRYSTAL_QUARTZ_THERMAL_OPD = FOM_Qtz = Constant(
    "CRYSTAL_QUARTZ_THERMAL_OPD",
    value=6.1e-7,
    unit="K^{-1}",
    description="Thermal optical path difference change of crystal quartz",
    aliases="FOM_Qtz",
).value

ZERODUR_THERMAL_EXPANSION = exp_zer = Constant(
    "ZERODUR_THERMAL_EXPANSION",
    value=2e-8,
    unit="K^{-1}",
    description="Thermal expansion of Zerodur",
    aliases="exp_zer",
).value

TITANIUM_THERMAL_EXPANSION = exp_Ti = Constant(
    "TITANIUM_THERMAL_EXPANSION",
    value=8.6e-6,
    unit="K^{-1}",
    description="Thermal expansion of titanium",
    aliases="exp_Ti",
).value

GOLD_PLATINUM_THERMAL_EXPANSION = exp_AuPt = Constant(
    "GOLD_PLATINUM_THERMAL_EXPANSION",
    value=1.52e-5,
    unit="K^{-1}",
    description="Thermal expansion of gold-platinum",
    aliases="exp_AuPt",
).value

WATER_MOLECULAR_WEIGHT = H2Omo = Constant(
    "WATER_MOLECULAR_WEIGHT",
    value=2.99150711295358e-26,
    unit="kg",
    description="Molecular weight (mass) of water",
    aliases="H2Omo",
).value

LISA_EPOCH_TCB = Constant(
    "LISA_EPOCH_TCB",
    value="2035-01-01T00:00:00.000",
    error=Error.EXACT,
    description="LISA epoch (ISO 8601 format)",
    longdescr="Currently set to January, 1st 2035, 00:00 TCB. This temporary value will be aligned to the official ESA LISA epoch when decided. Note that this epoch is defined in the TCB time frame; use Astropy for conversion.",
).value


#
# Constant consistency
# --------------------
# Do not add any constant below this line

compat.astropy.perform_importtime_consistency_check()
