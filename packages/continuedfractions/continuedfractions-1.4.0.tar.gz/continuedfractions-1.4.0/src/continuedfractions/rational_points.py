from __future__ import annotations


__all__ = [
    'RationalPoint',
]

# -- IMPORTS --

# -- Standard libraries --
import decimal
import math
import numbers

from decimal import Decimal
from typing import Any

# -- 3rd party libraries --

# -- Internal libraries --
from continuedfractions.continuedfraction import Fraction, ContinuedFraction


class RationalPoint(tuple):
    """A simple class for representing and operating on rational points as points in the :math:`xy`-plane.

    These are points in :math:`\\mathbb{R}^2` whose coordinates are rational
    i.e. elements of :math:`\\mathbb{Q}`, and thus are points of
    :math:`\\mathbb{Q}^2`.

    The points form an abelian group under component-wise addition, and form a
    closed set under scalar left-multiplication by rational numbers. The scalar
    left-multiplication is distributive over sums of rational points.

    This implemention of rational points uses :py:class:`tuple` objects, with
    exactly two members, both of which must be rational numbers: in Python this
    means the arguments must be instances of :py:class:`~numbers.Rational`,
    which covers values of type:

    * :py:class:`int`
    * :py:class:`~fractions.Fraction`
    * :py:class:`~continuedfractions.continuedfraction.ContinuedFraction`

    Internally, the rational coordinates of the point are stored as
    :py:class:`~continuedfractions.continuedfraction.ContinuedFraction`
    objects.

    Examples
    --------
    >>> RationalPoint(Fraction(3, 5), Fraction(4, 5))
    RationalPoint(3/5, 4/5)
    >>> RationalPoint(3, ContinuedFraction(4, 5))
    RationalPoint(3, 4/5)
    >>> RationalPoint(Fraction(3, 5), ContinuedFraction(4))
    RationalPoint(3/5, 4)
    >>> RationalPoint(-3, 4)
    RationalPoint(-3, 4)
    """
    def __new__(cls, *args: numbers.Rational) -> RationalPoint:
      if len(args) != 2 or any(not isinstance(x, numbers.Rational) for x in args):
          raise ValueError(
              'A `RationalPoint` object must be specified as a pair of '
              'rational numbers `r` and `s`, each of type either integer '
              '(`int`), or fraction (`Fraction` or `ContinuedFraction`).'
          )

      r, s = args
      return super().__new__(cls, (ContinuedFraction(r), ContinuedFraction(s)))

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self[0]}, {self[1]})'

    @property
    def x(self) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction` : The ``x``-coordinate of the rational point.

        Returns
        -------
        ContinuedFraction

        Examples
        --------
        >>> RationalPoint(Fraction(1, 2), Fraction(3, 4)).x
        ContinuedFraction(1, 2)
        """
        return self[0]

    @property
    def y(self) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction` : The ``y``-coordinate of the rational point.

        Returns
        -------
        ContinuedFraction

        Examples
        --------
        >>> RationalPoint(Fraction(1, 2), Fraction(3, 4)).y
        ContinuedFraction(3, 4)

        """
        return self[1]

    @property
    def coordinates(self) -> tuple[ContinuedFraction]:
        """
        :py:class:`tuple` : The pair of coordinates of the rational point.

        Returns
        -------
        tuple
            The pair of coordinates of the rational point as a tuple of
            :py:class:`~continuedfractions.continuedfraction.ContinuedFraction`
            instances.

        Examples
        --------
        >>> r = RationalPoint(Fraction(1, 2), Fraction(3, 4))
        >>> r.coordinates
        (ContinuedFraction(1, 2), ContinuedFraction(3, 4))
        """
        return (self.x, self.y)

    def dot_product(self, other: RationalPoint, /) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction` : The standard Euclidean dot product for two rational points in the plane.

        If :math:`r = \\left( \\frac{a_1}{c_1}, \\frac{a_2}{c_2} \\right)` and
        :math:`s  = \\left( \\frac{b_1}{d_1}, \\frac{b_2}{d_2} \\right)` are two
        rational points in the plane their Eucliean dot product
        :math:`r \\cdot s` is the rational number:

        .. math::
        
           \\begin{align}
           r \\cdot s &= \\frac{a_1b_1}{c_1d_1} + \\frac{a_2b_2}{c_2d_2} \\\\
                      &= \\frac{a_1b_1c_2d_2 + a_2b_2c_1d_1}{c_1c_2d_1d_2}        
           \\end{align}

        This value is returned as a 
        :py:class:`~continuedfractions.continuedfraction.ContinuedFraction` object
        because this is the standard representation of rational numbers in this
        package.

        Returns
        -------
        ContinuedFraction
            The standard Euclidean dot product for two rational points in the
            plane.

        Examples
        --------
        >>> r = RationalPoint(Fraction(1, 2), Fraction(3, 4))
        >>> s = RationalPoint(Fraction(1, 3), Fraction(2, 5))
        >>> r.dot_product(s)
        ContinuedFraction(7, 15)
        >>> r.dot_product(2)
        Traceback (most recent call last):
        ...
        ValueError: The dot product is only defined between `RationalPoint` instances.
        >>> r.dot_product(RationalPoint(0, 0))
        ContinuedFraction(0, 1)
        >>> r.dot_product(RationalPoint(1, 1))
        ContinuedFraction(5, 4)
        """
        if not isinstance(other, self.__class__):
            raise ValueError(
                'The dot product is only defined between `RationalPoint` '
                'instances.'
            )

        if self.coordinates == (0, 0) or other.coordinates == (0, 0):
            return ContinuedFraction(0)

        return (self.x * other.x) + (self.y * other.y)

    @property
    def norm_squared(self) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction` : The square of the Euclidean (:math:`\\ell_2`) norm of a rational point in the plane.

        The Euclidean (:math:`\\ell_2`) norm squared :math:`\\|r\\|_{2}^2` of a
        rational point :math:`r = \\left(\\frac{a}{c}, \\frac{b}{d} \\right)`
        in the plane is the dot product of :math:`r` with itself:

        .. math::

           \\begin{align}
           \\|r\\|_{2}^2 = r \\cdot r &= \\frac{a^2}{c^2} + \\frac{b^2}{d^2} \\\\
                                    &= \\frac{a^2d^2 + b^2c^2}{c^2d^2}
           \\end{align}

        and is also a rational number.

        Returns
        -------
        ContinuedFraction
            The Euclidean norm squared of the rational point.

        Examples
        --------
        >>> RationalPoint(1, 1).norm_squared
        ContinuedFraction(2, 1)
        >>> RationalPoint(Fraction(1, 2), Fraction(3, 5)).norm_squared
        ContinuedFraction(61, 100)
        >>> RationalPoint(0, 0).norm_squared
        ContinuedFraction(0, 1)
        """
        return self.dot_product(self)

    @property
    def norm(self) -> Decimal:
        """:py:class:`~decimal.Decimal` : The Euclidean norm of a rational point in the plane.

        The Euclidean norm :math:`\\|r\\|_2` of a rational point
        :math:`r = \\left( \\frac{a}{c}, \\frac{b}{d} \\right)`, as given by:

        .. math::

           \\begin{align}
           \\|r\\|_2 = \\sqrt{r \\cdot r} &= \\sqrt{\\frac{a^2}{c^2} + \\frac{b^2}{d^2}} \\\\
                                          &= \\sqrt{\\frac{a^2d^2 + b^2c^2}{c^2d^2}}
           \\end{align}

        Returns
        -------
        decimal.Decimal
            The Euclidean norm of the rational point.

        Examples
        --------
        >>> RationalPoint(1, 1).norm
        Decimal('1.414213562373095048801688724')
        >>> RationalPoint(Fraction(1, 2), Fraction(3, 5)).norm
        Decimal('0.7810249675906654394129722736')
        >>> RationalPoint(0, 0).norm
        Decimal('0')
        >>> RationalPoint(Fraction(3, 5), Fraction(4, 5)).norm
        Decimal('1')
        """
        return self.norm_squared.as_decimal().sqrt()

    def distance_squared(self, other: RationalPoint, /) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction` : The square of the Euclidean distance between this point and another rational point in the plane.

        If :math:`r = \\left( \\frac{a_1}{c_1}, \\frac{a_2}{c_2} \\right)` and
        :math:`s  = \\left( \\frac{b_1}{d_1}, \\frac{b_2}{d_2} \\right)` are
        two rational points in the plane the square of their Euclidean distance
        :math:`\\|r - s\\|_{2}^2` is the non-negative rational number:

        .. math::

           \\begin{align}
           \\|r - s\\|^2 &= \\left( \\frac{a_1}{c_1} - \\frac{b_1}{d_1} \\right)^2 + \\left( \\frac{a_2}{c_2} - \\frac{b_2}{d_2} \\right)^2 \\\\
                       &= \\left( \\frac{a_1d_1 - b_1c_1}{c_1d_1} \\right)^2 + \\left( \\frac{a_2d_2 - b_2c_2}{c_2d_2} \\right)^2 \\\\
           \\end{align}

        where :math:`\\|r - s\\|_{2}^2 = 0 \\iff r = s`.

        The Euclidean distance :math:`\\|r - s\\|_2` is simply the square root of
        this quantity.

        Returns
        -------
        ContinuedFraction
            The square of the Euclidean distance between this point and another
            rational point in the plane.

        Examples
        --------
        >>> r = RationalPoint(Fraction(3, 5), Fraction(4, 5))
        >>> r
        RationalPoint(3/5, 4/5)
        >>> r.distance_squared(RationalPoint(0, 0))
        ContinuedFraction(1, 1)
        >>> r.distance_squared(RationalPoint(1, 1))
        ContinuedFraction(1, 5)
        >>> RationalPoint(0, 0).distance_squared(RationalPoint(1, 1))
        ContinuedFraction(2, 1)
        """
        if not isinstance(other, RationalPoint):
            raise ValueError(
                'The square of the Euclidean distance is defined only between '
                'two `RationalPoint` instances.'
            )

        if other == self:
            return ContinuedFraction(0, 1)

        if self == RationalPoint(0, 0):
            return other.norm_squared

        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance(self, other: RationalPoint, /) -> Decimal:
        """:py:class:`~decimal.Decimal` : The Euclidean distance between this point and another rational point in the plane.

        If :math:`r = \\left( \\frac{a_1}{c_1}, \\frac{a_2}{c_2} \\right)` and
        :math:`s  = \\left( \\frac{b_1}{d_1}, \\frac{b_2}{d_2} \\right)` are
        two rational points in the plane their Euclidean distance
        :math:`\\|r - s\\|_2` is the non-negative number:

        .. math::

           \\begin{align}
           \\|r - s\\|_2 &= \\sqrt{\\left( \\frac{a_1}{c_1} - \\frac{b_1}{d_1} \\right)^2 + \\left( \\frac{a_2}{c_2} - \\frac{b_2}{d_2} \\right)^2} \\\\
                       &= \\sqrt{\\left( \\frac{a_1d_1 - b_1c_1}{c_1d_1} \\right)^2 + \\left( \\frac{a_2d_2 - b_2c_2}{c_2d_2} \\right)^2} \\\\
           \\end{align}

        where :math:`\\|r - s\\|_2 = 0 \\iff r = s`.

        Returns
        -------
        decimal.Decimal
            The Euclidean distance between this point and another rational
            point in the plane.

        Examples
        --------
        >>> r = RationalPoint(Fraction(3, 5), Fraction(4, 5))
        >>> r
        RationalPoint(3/5, 4/5)
        >>> r.distance(RationalPoint(0, 0))
        Decimal('1')
        >>> r.distance_squared(RationalPoint(1, 1))
        ContinuedFraction(1, 5)
        >>> RationalPoint(0, 0).distance(RationalPoint(1, 1))
        Decimal('1.414213562373095048801688724')
        """
        if not isinstance(other, RationalPoint):
            raise ValueError(
                'The Euclidean distance is defined only between two '
                '`RationalPoint` instances.'
            )

        return self.distance_squared(other).as_decimal().sqrt()

    def is_unit_point(self) -> bool:
        """:py:class:`bool` : Whether the rational point falls on the unit circle, which is the case if it has unit (:math:`\\ell_2`) norm.

        Returns
        -------
        bool
            Whether the coordinates satisfy the unit circle equation:

            .. math::

               x^2 + y^2 = 1

        Examples
        --------
        >>> RationalPoint(Fraction(3, 5), Fraction(4, 5)).is_unit_point()
        True
        >>> RationalPoint(Fraction(3, 4), Fraction(4, 5)).is_unit_point()
        False
        """
        return self.norm_squared == 1

    def is_lattice_point(self) -> bool:
        """:py:class:`bool` : Whether the rational point is a lattice point, i.e. has integer coordinates.

        Returns
        -------
        bool
            Whether the coordinates correspond to integers. Coordinates in
            fractional form :math:`\\frac{a}{1}` where the numerator :math:`a`
            is an integer are treated as integers.

        Examples
        --------
        >>> RationalPoint(1, 2).is_lattice_point()
        True
        >>> RationalPoint(Fraction(1, 2), 2).is_lattice_point()
        False
        """
        return all(coord.denominator == 1 for coord in self.coordinates)

    @property
    def rectilinear_norm(self) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction`: The rectilinear (:math:`\\ell_1` or taxicab) norm of the rational point.

        The rectilinear (:math:`\\ell_1` or taxicab) norm :math:`\\|r\\|_1` of
        a rational point :math:`r = \\left( \\frac{a}{c}, \\frac{b}{d} \\right)` is given by:

        .. math::

           \\|r\\|_1 = \\lvert\\frac{a}{c}\\rvert + \\lvert\\frac{b}{d}\\rvert

        The rectilinear norm of a rational point is a non-negative rational
        number, hence the property produces 
        :py:class:`~continuedfractions.continuedfraction.ContinuedFraction`
        objects, as this is the standard representation of rationals in this
        package.

        To get the decimal value use the
        :py:class:`~continuedfractions.continuedfraction.ContinuedFraction.as_decimal`
        method.

        Returns
        -------
        ContinuedFraction
            The rectilinear norm of the rational point, which is always a
            non-negative rational number.

        Examples
        --------
        >>> RationalPoint(Fraction(-1, 2), Fraction(3, 4)).rectilinear_norm
        ContinuedFraction(5, 4)
        >>> RationalPoint(Fraction(1, 2), Fraction(-3, 4)).rectilinear_norm
        ContinuedFraction(5, 4)
        >>> RationalPoint(Fraction(1, 2), Fraction(3, 4)).rectilinear_norm
        ContinuedFraction(5, 4)
        """
        return sum(map(abs, self.coordinates))

    def rectilinear_distance(self, other: RationalPoint, /) -> ContinuedFraction:
        """:py:class:`~continuedfractions.continuedfraction.ContinuedFraction` : The rectilinear (:math:`\\ell_1` or taxicab) distance between this rational point and another.

        If :math:`r = \\left( \\frac{a_1}{c_1}, \\frac{a_2}{c_2} \\right)` and
        :math:`s  = \\left( \\frac{b_1}{d_1}, \\frac{b_2}{d_2} \\right)` are
        two rational points in the plane their rectilinear (or taxicab)
        distance :math:`\\|r - s\\|_1` is the non-negative rational number:

        .. math::

           \\begin{align}
           \\|r - s\\|_1 &= \\lvert \\frac{a_1}{c_1} - \\frac{b_1}{d1} \\rvert + \\lvert \\frac{a_2}{c_2} - \\frac{b_2}{d2} \\rvert \\\\
                         &= \\lvert \\frac{a_1d_1 - b_1c_1}{c_1d_1} \\rvert + \\lvert \\frac{a_2d_2 - b_2c_2}{c_2d_2} \\rvert
           \\end{align}

        where :math:`\\|r - s\\| = 0 \\iff r = s`.

        Returns
        -------
        decimal.Decimal
            The rectilinear distance between this point and another rational
            point in the plane.

        Examples
        --------
        >>> RationalPoint(Fraction(3, 5), Fraction(4, 5)).rectilinear_distance(RationalPoint(1, 1))
        ContinuedFraction(3, 5)
        >>> RationalPoint(0, 0).rectilinear_distance(RationalPoint(1, 1))
        ContinuedFraction(2, 1)
        """
        if not isinstance(other, RationalPoint):
            raise ValueError(
                'The Euclidean distance is defined only between two '
                '`RationalPoint` instances.'
            )

        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def homogeneous_coordinates(self) -> tuple[int, int, int]:
        """:py:class:`tuple` : A unique sequence of integer-valued homogeneous coordinates in :math:`\\mathbb{P}^2` for this rational point.

        For a rational point :math:`P = \\left(\\frac{a}{c},\\frac{b}{d}\\right)`
        the triple
        :math:`\\left(\\lambda \\frac{a}{c}, \\lambda \\frac{b}{d}, \\lambda\\right) = \\left(a \\frac{\\lambda}{c}, b \\frac{\\lambda}{d}, \\lambda\\right)`,
        where :math:`\\lambda = \\text{lcm}(c, d) > 0`, represents a unique (up to
        sign) sequence of homogeneous coordinates for :math:`P` in :math:`\\mathbb{P}^2` such
        that
        :math:`\\left(a \\frac{\\lambda}{c}, b \\frac{\\lambda}{d}, \\lambda\\right)`
        are all integers (not all zero) and :math:`\\text{gcd}\\left(a \\frac{\\lambda}{c}, b \\frac{\\lambda}{d}, \\lambda\\right) = 1`.

        Returns
        -------
        tuple
            A tuple of integer-valued homogeneous coordinates in
            :math:`\\mathbb{P}^2` for this rational point.

        Examples
        --------
        >>> from fractions import Fraction as F
        >>> RationalPoint(0, 0).homogeneous_coordinates
        (0, 0, 1)
        >>> RationalPoint(F(1, 2), F(3, 4)).homogeneous_coordinates
        (2, 3, 4)
        >>> RationalPoint(F(1, 2), F(2, 3)).homogeneous_coordinates
        (3, 4, 6)
        >>> RationalPoint(-1, 1).homogeneous_coordinates
        (-1, 1, 1)
        >>> RationalPoint(1, 1).homogeneous_coordinates
        (1, 1, 1)
        """
        lcm = math.lcm(self.x.denominator, self.y.denominator)

        return ((lcm * self.x).numerator, (lcm * self.y).numerator, lcm)

    @property
    def projective_height(self) -> int:
        """:py:class:`int` : The height of the rational point as the height of its unique (up to sign) representative point in the projective space :math:`\\mathbb{P}^2`.

        The projective height :math:`H\\left(\\frac{a}{c},\\frac{b}{d}\\right)`
        of a rational point :math:`P = \\left(\\frac{a}{c},\\frac{b}{d}\\right)`
        as given by:

        .. math::

           \\text{max}\\left(|a|\\lvert \\frac{\\lambda}{c} \\rvert, |b|\\lvert \\frac{\\lambda}{d} \\rvert, \\lambda \\right)

        where :math:`\\lambda = \\text{lcm}(c, d) > 0`, and :math:`\\left(\\lambda \\frac{a}{c}, \\lambda \\frac{b}{d}, \\lambda\\right) = \\left(a \\frac{\\lambda}{c}, b \\frac{\\lambda}{d}, \\lambda\\right)`
        is the unique (up to sign) representative point :math:`\\left(\\lambda \\frac{a}{c}, \\lambda \\frac{b}{d}, \\lambda\\right) = \\left(a \\frac{\\lambda}{c}, b \\frac{\\lambda}{d}, \\lambda\\right)`
        of :math:`P` in :math:`\\mathbb{P}^2`, and also a sequence of homogeneous
        coordinates for :math:`P`.

        Returns
        -------
        int
            The height of this rational point as defined above.

        Examples
        --------
        """
        return max(map(abs, self.homogeneous_coordinates))
        
    @property
    def log_projective_height(self) -> Decimal:
        """:py:class:`~decimal.Decimal` : The natural logarithm of the projective height of the rational point as defined above.

        The (natural) logarithm of the projective height of a rational point
        :math:`P = \\left(\\frac{a}{c},\\frac{b}{d}\\right)` as given by:

        .. math::

           \\text{log}\\left(H\\left(\\frac{a}{c}, \\frac{b}{d}\\right)\\right) = \\text{log}\\left(\\text{max}\\left(|a|\\lvert \\frac{\\lambda}{c} \\rvert, |b|\\lvert \\frac{\\lambda}{d} \\rvert, \\lambda \\right)\\right)

        where :math:`\\lambda = \\text{lcm}(c, d) > 0` and :math:`\\left(\\lambda \\frac{a}{c}, \\lambda \\frac{b}{d}, \\lambda\\right) = \\left(a \\frac{\\lambda}{c}, b \\frac{\\lambda}{d}, \\lambda\\right)`
        is the unique (up to sign) representative point of :math:`P` in
        :math:`\\mathbb{P}^2`, as defined above.

        Returns
        -------
        decimal.Decimal
            The (natural) logarithm of the projective height of this rational
            point in :math:`\\mathbb{P}^2` as defined above.

        Examples
        --------
        """
        return Decimal(math.log(self.projective_height, math.e))

    def __add__(self, other: RationalPoint) -> RationalPoint:
        """:py:class:`~continuedfractions.rational_points.RationalPoint` : Component-wise addition for two rational points.

        Implements component-wise addition of two rational points:

        .. math::

           \\left(\\frac{a_1}{c_1}, \\frac{b_1}{d_1}\\right) + \\left(\\frac{a_2}{c_2}, \\frac{b_2}{d_2}\\right) = \\left(\\frac{a_1c_2 + a_2c_1}{c_1c_2}, \\frac{b_1d_2 + b_2d_1}{d_1d_2}\\right)

        The second operand as represented by ``other`` must be an instance of
        :py:class:`~continuedfractions.rational_points.RationalPoint`.
        """
        if not isinstance(other, RationalPoint):
            raise TypeError(
                'Addition is defined only between two `RationalPoint` '
                'instances.'
            )

        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: RationalPoint) -> RationalPoint:
        """:py:class:`~continuedfractions.rational_points.RationalPoint` : Component-wise subtraction for two rational points.

        Implements component-wise subtraction of two rational points:

        .. math::

           \\left(\\frac{a_1}{c_1}, \\frac{b_1}{d_1}\\right) - \\left(\\frac{a_2}{c_2}, \\frac{b_2}{d_2}\\right) = \\left(\\frac{a_1c_2 - a_2c_1}{c_1c_2}, \\frac{b_1d_2 - b_2d_1}{d_1d_2}\\right)

        The second operand as represented by ``other`` must be an instance of
        :py:class:`~continuedfractions.rational_points.RationalPoint`.
        """
        if not isinstance(other, RationalPoint):
            raise TypeError(                                                    # pragma: no cover
                'Subtraction is defined only between two `RationalPoint` '
                'instances.'
            )

        return self.__class__(self.x - other.x, self.y - other.y)

    def __neg__(self) -> RationalPoint:
        """:py:class:`~continuedfractions.rational_points.RationalPoint` : Component-wise negation for a rational point.

        Implements component-wise negation for a rational point:

        .. math::

           -\\left(\\frac{a}{c}, \\frac{b}{d}\\right) = \\left(-\\frac{a}{c}, -\\frac{b}{d}\\right)
        """
        return self.__class__(-self.x, -self.y)

    def __mul__(self, other: Any) -> RationalPoint:
        """Does not support component-wise right-multiplication by a scalar to respect notational convention.
        """
        raise NotImplementedError(
            'Only rational scalar left-multiplication is supported. This '
            'means the left-most operand must be an instance of '
            '`numbers.Rational`, i.e. an `int`, `fractions.Fraction` or '
            '`ContinuedFraction`.'
        )

    def __rmul__(self, other: int | Fraction | ContinuedFraction) -> RationalPoint:
        """:py:class:`~continuedfractions.rational_points.RationalPoint` : Component-wise scalar left-multiplication of a rational number by an integer or rational number.

        Implements component-wise left-multiplication of a rational point with a rational scalar:

        .. math::

           \\lambda \\left(\\frac{a}{c}, \\frac{b}{d}\\right) = \\left(\\lambda \\frac{a}{c}, \\lambda \\frac{b}{d}\\right), \\hspace{1em} \\lambda \\in \\mathbb{Q}

        The implementation is in terms of ``__rmul__``, because conventionally
        scalar multiples of a vectors in vector spaces (or subspaces) such as
        :math:`\\mathbb{R}^n` are written in left-multiplication style.
        
        The second operand must be a rational number scalar as given by an
        instance of :py:class:`int`, :py:class:`~fractions.Fraction`, or
        :py:class:`~continuedfractions.continuedfraction.ContinuedFraction`.
        """
        if not isinstance(other, (int, Fraction, ContinuedFraction)):
            raise TypeError(                                                        # pragma: no cover
                'Only rational scalar left-multiplication is supported. This '
                'means the left-most operand must be an instance of '
                '`numbers.Rational`, i.e. an `int`, `fractions.Fraction` or '
                '`ContinuedFraction`.'
            )

        if other == 0:
            return self.__class__(0, 0)
        elif other == 1:
            return self

        return self.__class__(self.x * other, self.y * other)

    def __abs__(self) -> Decimal:
        """:py:class:`~decimal.Decimal` : The absolute value of the rational point as the standard Euclidean norm.

        For points in :math:`\\mathbb{R}^n` the notion of absolute value and
        Euclidean norm coincide.

        Returns
        -------
        decimal.Decimal
            The absolute value of the rational point as the standard Euclidean norm.

        Examples
        --------
        >>> abs(RationalPoint(0, 0))
        Decimal('0')
        >>> abs(RationalPoint(Fraction(3, 5), Fraction(4, 5)))
        Decimal('1')
        >>> abs(RationalPoint(1, 1))
        Decimal('1.414213562373095048801688724')
        """
        return self.norm


if __name__ == "__main__":      # pragma: no cover
    # Doctest the module from the project root using
    #
    #     PYTHONPATH="src" python3 -m doctest -v src/continuedfractions/rational_points.py
    #
    # NOTE: the doctest examples using ``decimal.Decimal`` values are based on
    #       a context precision of 28 digits.
    decimal.getcontext().prec = 28
    import doctest
    doctest.testmod()
