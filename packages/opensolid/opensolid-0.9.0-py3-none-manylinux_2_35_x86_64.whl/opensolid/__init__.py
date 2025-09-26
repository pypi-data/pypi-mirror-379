"""A collection of classes for 2D/3D geometric modelling."""

from __future__ import annotations

import contextvars
import ctypes
import platform
from contextvars import ContextVar
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int64, c_size_t, c_void_p
from functools import cached_property
from pathlib import Path
from typing import Any, Never, Union, overload


def _load_library() -> CDLL:
    """Load the native library from the same directory as __init__.py."""
    match platform.system():
        case "Windows":
            lib_file_name = "opensolid-ffi.dll"
        case "Darwin":
            lib_file_name = "libopensolid-ffi.dylib"
        case "Linux":
            lib_file_name = "libopensolid-ffi.so"
        case unsupported_system:
            raise OSError(unsupported_system + " is not yet supported")
    self_dir = Path(__file__).parent
    lib_path = self_dir / lib_file_name
    return ctypes.cdll.LoadLibrary(str(lib_path))


_lib: CDLL = _load_library()

# Define the signatures of the C API functions
# (also an early sanity check to make sure the library has been loaded OK)
_lib.opensolid_init.argtypes = []
_lib.opensolid_malloc.argtypes = [c_size_t]
_lib.opensolid_malloc.restype = c_void_p
_lib.opensolid_free.argtypes = [c_void_p]
_lib.opensolid_release.argtypes = [c_void_p]

# Initialize the Haskell runtime
_lib.opensolid_init()


class Error(Exception):
    """An error that may be thrown by OpenSolid functions."""


class _Text(ctypes.Union):
    _fields_ = (("as_char", c_char_p), ("as_void", c_void_p))


def _text_to_str(ptr: _Text) -> str:
    decoded = ptr.as_char.decode("utf-8")
    _lib.opensolid_free(ptr.as_void)
    return decoded


def _str_to_text(s: str) -> _Text:
    encoded = s.encode("utf-8")
    buffer = ctypes.create_string_buffer(encoded)
    return _Text(as_char=ctypes.cast(buffer, c_char_p))


def _list_argument(list_type: Any, array: Any) -> Any:  # noqa: ANN401
    return list_type(len(array), array)


def _sign_argument(value: int) -> int:
    if value in (1, -1):
        return value
    return _error("Sign value must be 1 or -1")


def _error(message: str) -> Never:
    raise Error(message)


class Tolerance:
    """Manages a tolerance context value.

    Many functions in OpenSolid require a tolerance to be set.
    You should generally choose a value that is
    much smaller than any meaningful size/dimension in the geometry you're modelling,
    but significantly *larger* than any expected numerical roundoff that might occur.
    A good default choice is roughly one-billionth of the overall size of your geometry;
    for 'human-scale' things (say, from an earring up to a house)
    that means that one nanometer is a reasonable value to use.

    Passing a tolerance into every function that needed one would get very verbose,
    and it's very common to choose a single tolerance value and use it throughout a project.
    However, it's also occasionally necessary to set a different tolerance for some code.
    This class allows managing tolerances using Python's ``with`` statement, e.g.::

        with Tolerance(Length.nanometer):
            do_something()
            do_something_else()
            with Tolerance(Angle.degrees(0.001)):
                compare_two_angles()
            do_more_things()

    In the above code, the ``Length.nanometer`` tolerance value
    will be used for ``do_something()`` and ``do_something_else()``
    (and any functions they call).
    The ``Angle.degrees(0.001))`` tolerance value
    will then be used for ``compare_two_angles()``,
    and then the ``Length.nanometer`` tolerance value will be restored
    and used for ``do_more_things()``.
    """

    Value = Union[float, "Length", "Area", "Angle"]

    _value: Value
    _token: contextvars.Token[Value] | None = None

    def __init__(self, value: Value) -> None:
        self._value = value

    def __enter__(self) -> None:
        """Set the given tolerance as the currently active one."""
        assert self._token is None
        self._token = _tolerance.set(self._value)

    def __exit__(
        self, _exception_type: object, _exception_value: object, _traceback: object
    ) -> None:
        """Restore the previous tolerance as the currently active one."""
        assert self._token is not None
        _tolerance.reset(self._token)
        self._token = None

    @staticmethod
    def current() -> Value:
        """Get the current tolerance value."""
        try:
            return _tolerance.get()
        except LookupError as error:
            message = 'No tolerance set, please set one using "with Tolerance(...)"'
            raise LookupError(message) from error


_tolerance: ContextVar[Tolerance.Value] = ContextVar("tolerance")


def _current_tolerance[T](expected_type: type[T]) -> T:
    current_tolerance = Tolerance.current()
    if not isinstance(current_tolerance, expected_type):
        message = (
            "Expected a tolerance of type "
            + expected_type.__name__
            + " but current tolerance is of type "
            + type(current_tolerance).__name__
        )
        raise TypeError(message)
    return current_tolerance


def _float_tolerance() -> float:
    return _current_tolerance(float)


def _length_tolerance() -> Length:
    return _current_tolerance(Length)


def _area_tolerance() -> Area:
    return _current_tolerance(Area)


def _angle_tolerance() -> Angle:
    return _current_tolerance(Angle)


class _Tuple3_Text_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", _Text), ("field1", c_void_p), ("field2", c_void_p)]


class _Result_c_int64(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", _Text), ("field2", c_int64)]


class _Tuple2_c_void_p_Text(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", _Text)]


class _Tuple3_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_void_p), ("field2", c_void_p)]


class _Tuple5_c_void_p_c_void_p_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", c_void_p),
        ("field2", c_void_p),
        ("field3", c_void_p),
        ("field4", c_void_p),
    ]


class _Tuple2_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_void_p)]


class _List_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", POINTER(c_void_p))]


class _Tuple2_c_int64_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", c_void_p)]


class _Tuple2_List_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", _List_c_void_p), ("field1", c_void_p)]


class _Tuple2_c_double_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", c_void_p)]


class _Tuple2_Text_c_void_p(ctypes.Structure):
    _fields_ = [("field0", _Text), ("field1", c_void_p)]


class _Tuple2_List_c_void_p_List_c_void_p(ctypes.Structure):
    _fields_ = [("field0", _List_c_void_p), ("field1", _List_c_void_p)]


class _Tuple3_c_void_p_List_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", _List_c_void_p), ("field2", c_void_p)]


class _Tuple3_c_void_p_c_double_c_double(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_double), ("field2", c_double)]


class _Tuple2_c_void_p_c_double(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_double)]


class _Tuple4_c_void_p_Text_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", _Text),
        ("field2", c_void_p),
        ("field3", c_void_p),
    ]


class _Tuple5_c_void_p_Text_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", _Text),
        ("field2", c_void_p),
        ("field3", c_void_p),
        ("field4", c_void_p),
    ]


class _Result_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", _Text), ("field2", c_void_p)]


class _Tuple4_c_void_p_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", c_void_p),
        ("field2", c_void_p),
        ("field3", c_void_p),
    ]


class _List_List_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", POINTER(_List_c_void_p))]


class _Tuple3_c_double_c_void_p_c_double(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", c_void_p), ("field2", c_double)]


class _Tuple2_c_double_List_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", _List_c_void_p)]


class _Tuple3_c_void_p_c_double_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_double), ("field2", c_void_p)]


class _Tuple4_c_void_p_List_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", _List_c_void_p),
        ("field2", c_void_p),
        ("field3", c_void_p),
    ]


class _Tuple4_c_void_p_c_int64_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", c_int64),
        ("field2", c_void_p),
        ("field3", c_void_p),
    ]


class _Tuple2_c_void_p_List_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", _List_c_void_p)]


class _Tuple4_c_void_p_List_c_void_p_c_void_p_List_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", _List_c_void_p),
        ("field2", c_void_p),
        ("field3", _List_c_void_p),
    ]


class _Tuple5_c_double_c_void_p_c_void_p_c_void_p_c_double(ctypes.Structure):
    _fields_ = [
        ("field0", c_double),
        ("field1", c_void_p),
        ("field2", c_void_p),
        ("field3", c_void_p),
        ("field4", c_double),
    ]


class _Tuple4_c_void_p_c_double_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_void_p),
        ("field1", c_double),
        ("field2", c_void_p),
        ("field3", c_void_p),
    ]


class _Tuple4_c_double_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [
        ("field0", c_double),
        ("field1", c_void_p),
        ("field2", c_void_p),
        ("field3", c_void_p),
    ]


class _Tuple2_c_void_p_Tuple3_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", _Tuple3_c_void_p_c_void_p_c_void_p)]


class _Tuple3_c_double_c_double_c_double(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", c_double), ("field2", c_double)]


class _Tuple2_c_void_p_Tuple3_c_double_c_double_c_double(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", _Tuple3_c_double_c_double_c_double)]


class _Tuple3_List_c_void_p_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", _List_c_void_p), ("field1", c_void_p), ("field2", c_void_p)]


class _Tuple3_c_double_c_void_p_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", c_void_p), ("field2", c_void_p)]


class _Result_List_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", _Text), ("field2", _List_c_void_p)]


class _Tuple3_c_double_c_double_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", c_double), ("field2", c_void_p)]


class _Tuple2_c_double_c_double(ctypes.Structure):
    _fields_ = [("field0", c_double), ("field1", c_double)]


class _Tuple3_c_int64_c_int64_c_int64(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", c_int64), ("field2", c_int64)]


class _Maybe_c_void_p(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", c_void_p)]


class _List_c_double(ctypes.Structure):
    _fields_ = [("field0", c_int64), ("field1", POINTER(c_double))]


class _Tuple3_c_void_p_c_void_p_c_int64(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_void_p), ("field2", c_int64)]


class _Tuple3_c_void_p_c_void_p_c_double(ctypes.Structure):
    _fields_ = [("field0", c_void_p), ("field1", c_void_p), ("field2", c_double)]


class Length:
    """A length in millimeters, meters, inches etc.

    Represented internally as a value in meters.
    """

    _length_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Length:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Length)
        obj._length_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._length_ptr)

    zero: Length = None  # type: ignore[assignment]
    """The zero value."""

    @staticmethod
    def interpolate(start: Length, end: Length, parameter_value: float) -> Length:
        """Interpolate from one value to another, based on a parameter that ranges from 0 to 1."""
        inputs = _Tuple3_c_void_p_c_void_p_c_double(
            start._length_ptr, end._length_ptr, parameter_value
        )
        output = c_void_p()
        _lib.opensolid_Length_interpolate_Length_Length_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @staticmethod
    def steps(start: Length, end: Length, n: int) -> list[Length]:
        """Interpolate between two values by subdividing into the given number of steps.

        The result is an empty list if the given number of steps is zero (or negative).
        Otherwise, the number of values in the resulting list will be equal to one plus the number of steps.
        For example, for one step the returned values will just be the given start and end values;
        for two steps the returned values will be the start value, the midpoint and then the end value.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(
            start._length_ptr, end._length_ptr, n
        )
        output = _List_c_void_p()
        _lib.opensolid_Length_steps_Length_Length_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Length._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def leading(start: Length, end: Length, n: int) -> list[Length]:
        """Interpolate between two values like 'steps', but skip the first value."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(
            start._length_ptr, end._length_ptr, n
        )
        output = _List_c_void_p()
        _lib.opensolid_Length_leading_Length_Length_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Length._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def trailing(start: Length, end: Length, n: int) -> list[Length]:
        """Interpolate between two values like 'steps', but skip the last value."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(
            start._length_ptr, end._length_ptr, n
        )
        output = _List_c_void_p()
        _lib.opensolid_Length_trailing_Length_Length_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Length._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def in_between(start: Length, end: Length, n: int) -> list[Length]:
        """Interpolate between two values like 'steps', but skip the first and last values."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(
            start._length_ptr, end._length_ptr, n
        )
        output = _List_c_void_p()
        _lib.opensolid_Length_inBetween_Length_Length_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Length._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def midpoints(start: Length, end: Length, n: int) -> list[Length]:
        """Subdivide a given range into the given number of steps, and return the midpoint of each step.

        This can be useful if you want to sample a curve or other function at the midpoint of several intervals.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(
            start._length_ptr, end._length_ptr, n
        )
        output = _List_c_void_p()
        _lib.opensolid_Length_midpoints_Length_Length_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Length._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def meters(value: float) -> Length:
        """Construct a length from a number of meters."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_meters_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @staticmethod
    def centimeters(value: float) -> Length:
        """Construct a length from a number of centimeters."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_centimeters_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @staticmethod
    def cm(value: float) -> Length:
        """Construct a length from a number of centimeters.

        Short form alias for 'centimeters'.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_cm_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @staticmethod
    def millimeters(value: float) -> Length:
        """Construct a length value from a number of millimeters."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_millimeters_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @staticmethod
    def mm(value: float) -> Length:
        """Construct a length value from a number of millimeters.

        Short form alias for 'millimeters'.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_mm_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @staticmethod
    def micrometers(value: float) -> Length:
        """Construct a length from a number of micrometers."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_micrometers_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @staticmethod
    def nanometers(value: float) -> Length:
        """Construct a length from a number of nanometers."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_nanometers_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @staticmethod
    def inches(value: float) -> Length:
        """Construct a length from a number of inches."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_inches_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @staticmethod
    def pixels(value: float) -> Length:
        """Construct a length from a number of CSS pixels."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Length_pixels_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    def in_meters(self) -> float:
        """Convert a length to a number of meters."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inMeters(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_centimeters(self) -> float:
        """Convert a length to a number of centimeters."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inCentimeters(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_millimeters(self) -> float:
        """Convert a length to a number of millimeters."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inMillimeters(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_micrometers(self) -> float:
        """Convert a length to a number of micrometers."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inMicrometers(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_nanometers(self) -> float:
        """Convert a length to a number of nanometers."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inNanometers(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_inches(self) -> float:
        """Convert a length to a number of inches."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inInches(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_pixels(self) -> float:
        """Convert a length into a number of CSS pixels."""
        inputs = self._length_ptr
        output = c_double()
        _lib.opensolid_Length_inPixels(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def is_zero(self) -> bool:
        """Check if a length is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._length_ptr
        )
        output = c_int64()
        _lib.opensolid_Length_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __eq__(self, other: object) -> bool:
        """Return ``self == other``.

        Note that this is an *exact* comparison; for a tolerant comparison
        (one which will return true if two values are *almost* equal)
        you'll likely want to use an ``is_zero()`` method instead.
        """
        if not isinstance(other, Length):
            return False
        inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, other._length_ptr)
        output = c_int64()
        _lib.opensolid_Length_eq(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __hash__(self) -> int:
        """Return a hash code for ``self``."""
        inputs = self._length_ptr
        output = c_int64()
        _lib.opensolid_Length_hash(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def _compare(self, other: Length) -> int:
        inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, other._length_ptr)
        output = c_int64()
        _lib.opensolid_Length_compare(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def __lt__(self, other: Length) -> bool:
        """Return ``self < other``."""
        return self._compare(other) < 0

    def __le__(self, other: Length) -> bool:
        """Return ``self <= other``."""
        return self._compare(other) <= 0

    def __ge__(self, other: Length) -> bool:
        """Return ``self >= other``."""
        return self._compare(other) >= 0

    def __gt__(self, other: Length) -> bool:
        """Return ``self > other``."""
        return self._compare(other) > 0

    def __neg__(self) -> Length:
        """Return ``-self``."""
        inputs = self._length_ptr
        output = c_void_p()
        _lib.opensolid_Length_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    def __abs__(self) -> Length:
        """Return ``abs(self)``."""
        inputs = self._length_ptr
        output = c_void_p()
        _lib.opensolid_Length_abs(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @overload
    def __add__(self, rhs: Length) -> Length:
        pass

    @overload
    def __add__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    @overload
    def __add__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Length_add_Length_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_add_Length_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_add_Length_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: Length) -> Length:
        pass

    @overload
    def __sub__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    @overload
    def __sub__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Length_sub_Length_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_sub_Length_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_sub_Length_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> Length:
        pass

    @overload
    def __mul__(self, rhs: Length) -> Area:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> LengthBounds:
        pass

    @overload
    def __mul__(self, rhs: LengthBounds) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> LengthCurve:
        pass

    @overload
    def __mul__(self, rhs: LengthCurve) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: Direction2d) -> Displacement2d:
        pass

    @overload
    def __mul__(self, rhs: Vector2d) -> Displacement2d:
        pass

    @overload
    def __mul__(self, rhs: Displacement2d) -> AreaVector2d:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._length_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Direction2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._direction2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Direction2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Vector2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._vector2d_ptr)
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Vector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Displacement2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._displacement2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_mul_Length_Displacement2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector2d._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Length:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> float:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> LengthBounds:
        pass

    @overload
    def __truediv__(self, rhs: LengthBounds) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> LengthCurve:
        pass

    @overload
    def __truediv__(self, rhs: LengthCurve) -> Curve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._length_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Length_div_Length_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._length_ptr)
                output = c_double()
                _lib.opensolid_Length_div_Length_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return output.value
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Length_div_Length_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._length_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Length_div_Length_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._length_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_Length_div_Length_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    LengthCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case LengthCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _length_tolerance()._length_ptr,
                    self._length_ptr,
                    rhs._lengthcurve_ptr,
                )
                output = _Result_c_void_p()
                _lib.opensolid_Length_div_Length_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __floordiv__(self, rhs: Length) -> int:
        """Return ``self // rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._length_ptr)
        output = c_int64()
        _lib.opensolid_Length_floorDiv_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return output.value

    def __mod__(self, rhs: Length) -> Length:
        """Return ``self % rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._length_ptr, rhs._length_ptr)
        output = c_void_p()
        _lib.opensolid_Length_mod_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    def __rmul__(self, lhs: float) -> Length:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._length_ptr)
        output = c_void_p()
        _lib.opensolid_Length_mul_Float_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        return "Length.meters(" + str(self.in_meters()) + ")"


def _length_zero() -> Length:
    output = c_void_p()
    _lib.opensolid_Length_zero(c_void_p(), ctypes.byref(output))
    return Length._new(output)


Length.zero = _length_zero()


class Area:
    """An area in square meters, square inches etc.

    Represented internally as a value in square meters.
    """

    _area_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Area:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Area)
        obj._area_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._area_ptr)

    zero: Area = None  # type: ignore[assignment]
    """The zero value."""

    @staticmethod
    def interpolate(start: Area, end: Area, parameter_value: float) -> Area:
        """Interpolate from one value to another, based on a parameter that ranges from 0 to 1."""
        inputs = _Tuple3_c_void_p_c_void_p_c_double(
            start._area_ptr, end._area_ptr, parameter_value
        )
        output = c_void_p()
        _lib.opensolid_Area_interpolate_Area_Area_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    @staticmethod
    def steps(start: Area, end: Area, n: int) -> list[Area]:
        """Interpolate between two values by subdividing into the given number of steps.

        The result is an empty list if the given number of steps is zero (or negative).
        Otherwise, the number of values in the resulting list will be equal to one plus the number of steps.
        For example, for one step the returned values will just be the given start and end values;
        for two steps the returned values will be the start value, the midpoint and then the end value.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._area_ptr, end._area_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Area_steps_Area_Area_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Area._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def leading(start: Area, end: Area, n: int) -> list[Area]:
        """Interpolate between two values like 'steps', but skip the first value."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._area_ptr, end._area_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Area_leading_Area_Area_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Area._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def trailing(start: Area, end: Area, n: int) -> list[Area]:
        """Interpolate between two values like 'steps', but skip the last value."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._area_ptr, end._area_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Area_trailing_Area_Area_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Area._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def in_between(start: Area, end: Area, n: int) -> list[Area]:
        """Interpolate between two values like 'steps', but skip the first and last values."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._area_ptr, end._area_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Area_inBetween_Area_Area_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Area._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def midpoints(start: Area, end: Area, n: int) -> list[Area]:
        """Subdivide a given range into the given number of steps, and return the midpoint of each step.

        This can be useful if you want to sample a curve or other function at the midpoint of several intervals.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._area_ptr, end._area_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Area_midpoints_Area_Area_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Area._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def square_meters(value: float) -> Area:
        """Construct an area from a number of square meters."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Area_squareMeters_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    @staticmethod
    def square_inches(value: float) -> Area:
        """Construct an area from a number of square inches."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Area_squareInches_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    def in_square_meters(self) -> float:
        """Convert an area to a number of square meters."""
        inputs = self._area_ptr
        output = c_double()
        _lib.opensolid_Area_inSquareMeters(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_square_inches(self) -> float:
        """Convert an area to a number of square inches."""
        inputs = self._area_ptr
        output = c_double()
        _lib.opensolid_Area_inSquareInches(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def is_zero(self) -> bool:
        """Check if an area is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(_area_tolerance()._area_ptr, self._area_ptr)
        output = c_int64()
        _lib.opensolid_Area_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __eq__(self, other: object) -> bool:
        """Return ``self == other``.

        Note that this is an *exact* comparison; for a tolerant comparison
        (one which will return true if two values are *almost* equal)
        you'll likely want to use an ``is_zero()`` method instead.
        """
        if not isinstance(other, Area):
            return False
        inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, other._area_ptr)
        output = c_int64()
        _lib.opensolid_Area_eq(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __hash__(self) -> int:
        """Return a hash code for ``self``."""
        inputs = self._area_ptr
        output = c_int64()
        _lib.opensolid_Area_hash(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def _compare(self, other: Area) -> int:
        inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, other._area_ptr)
        output = c_int64()
        _lib.opensolid_Area_compare(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def __lt__(self, other: Area) -> bool:
        """Return ``self < other``."""
        return self._compare(other) < 0

    def __le__(self, other: Area) -> bool:
        """Return ``self <= other``."""
        return self._compare(other) <= 0

    def __ge__(self, other: Area) -> bool:
        """Return ``self >= other``."""
        return self._compare(other) >= 0

    def __gt__(self, other: Area) -> bool:
        """Return ``self > other``."""
        return self._compare(other) > 0

    def __neg__(self) -> Area:
        """Return ``-self``."""
        inputs = self._area_ptr
        output = c_void_p()
        _lib.opensolid_Area_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Area._new(output)

    def __abs__(self) -> Area:
        """Return ``abs(self)``."""
        inputs = self._area_ptr
        output = c_void_p()
        _lib.opensolid_Area_abs(ctypes.byref(inputs), ctypes.byref(output))
        return Area._new(output)

    @overload
    def __add__(self, rhs: Area) -> Area:
        pass

    @overload
    def __add__(self, rhs: AreaBounds) -> AreaBounds:
        pass

    @overload
    def __add__(self, rhs: AreaCurve) -> AreaCurve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_Area_add_Area_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._areabounds_ptr)
                output = c_void_p()
                _lib.opensolid_Area_add_Area_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case AreaCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._areacurve_ptr)
                output = c_void_p()
                _lib.opensolid_Area_add_Area_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: Area) -> Area:
        pass

    @overload
    def __sub__(self, rhs: AreaBounds) -> AreaBounds:
        pass

    @overload
    def __sub__(self, rhs: AreaCurve) -> AreaCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_Area_sub_Area_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._areabounds_ptr)
                output = c_void_p()
                _lib.opensolid_Area_sub_Area_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case AreaCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._areacurve_ptr)
                output = c_void_p()
                _lib.opensolid_Area_sub_Area_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> Area:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: Direction2d) -> AreaVector2d:
        pass

    @overload
    def __mul__(self, rhs: Vector2d) -> AreaVector2d:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._area_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Area_mul_Area_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Area_mul_Area_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_Area_mul_Area_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Direction2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._direction2d_ptr)
                output = c_void_p()
                _lib.opensolid_Area_mul_Area_Direction2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector2d._new(output)
            case Vector2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._vector2d_ptr)
                output = c_void_p()
                _lib.opensolid_Area_mul_Area_Vector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector2d._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Area:
        pass

    @overload
    def __truediv__(self, rhs: Area) -> float:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Length:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> AreaBounds:
        pass

    @overload
    def __truediv__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    @overload
    def __truediv__(self, rhs: AreaBounds) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> AreaCurve:
        pass

    @overload
    def __truediv__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    @overload
    def __truediv__(self, rhs: AreaCurve) -> Curve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._area_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Area_div_Area_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._area_ptr)
                output = c_double()
                _lib.opensolid_Area_div_Area_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return output.value
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Area_div_Area_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Area_div_Area_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._area_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Area_div_Area_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._areabounds_ptr)
                output = c_void_p()
                _lib.opensolid_Area_div_Area_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._area_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_Area_div_Area_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    AreaCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case LengthCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _length_tolerance()._length_ptr,
                    self._area_ptr,
                    rhs._lengthcurve_ptr,
                )
                output = _Result_c_void_p()
                _lib.opensolid_Area_div_Area_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    LengthCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case AreaCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _length_tolerance()._length_ptr, self._area_ptr, rhs._areacurve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_Area_div_Area_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __floordiv__(self, rhs: Area) -> int:
        """Return ``self // rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._area_ptr)
        output = c_int64()
        _lib.opensolid_Area_floorDiv_Area_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return output.value

    def __mod__(self, rhs: Area) -> Area:
        """Return ``self % rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._area_ptr, rhs._area_ptr)
        output = c_void_p()
        _lib.opensolid_Area_mod_Area_Area(ctypes.byref(inputs), ctypes.byref(output))
        return Area._new(output)

    def __rmul__(self, lhs: float) -> Area:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._area_ptr)
        output = c_void_p()
        _lib.opensolid_Area_mul_Float_Area(ctypes.byref(inputs), ctypes.byref(output))
        return Area._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        return "Area.square_meters(" + str(self.in_square_meters()) + ")"


def _area_zero() -> Area:
    output = c_void_p()
    _lib.opensolid_Area_zero(c_void_p(), ctypes.byref(output))
    return Area._new(output)


Area.zero = _area_zero()


class Angle:
    """An angle in degrees, radians, turns etc.

    Represented internally as a value in radians.
    """

    _angle_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Angle:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Angle)
        obj._angle_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._angle_ptr)

    zero: Angle = None  # type: ignore[assignment]
    """The zero value."""

    golden_angle: Angle = None  # type: ignore[assignment]
    """The [golden angle](https://en.wikipedia.org/wiki/Golden_angle)."""

    radian: Angle = None  # type: ignore[assignment]
    """One radian."""

    full_turn: Angle = None  # type: ignore[assignment]
    """One full turn, or 360 degrees."""

    half_turn: Angle = None  # type: ignore[assignment]
    """One half turn, or 180 degrees."""

    quarter_turn: Angle = None  # type: ignore[assignment]
    """One quarter turn, or 90 degrees."""

    pi: Angle = None  # type: ignore[assignment]
    """π radians, or 180 degrees."""

    two_pi: Angle = None  # type: ignore[assignment]
    """2π radians, or 360 degrees."""

    @staticmethod
    def interpolate(start: Angle, end: Angle, parameter_value: float) -> Angle:
        """Interpolate from one value to another, based on a parameter that ranges from 0 to 1."""
        inputs = _Tuple3_c_void_p_c_void_p_c_double(
            start._angle_ptr, end._angle_ptr, parameter_value
        )
        output = c_void_p()
        _lib.opensolid_Angle_interpolate_Angle_Angle_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    @staticmethod
    def steps(start: Angle, end: Angle, n: int) -> list[Angle]:
        """Interpolate between two values by subdividing into the given number of steps.

        The result is an empty list if the given number of steps is zero (or negative).
        Otherwise, the number of values in the resulting list will be equal to one plus the number of steps.
        For example, for one step the returned values will just be the given start and end values;
        for two steps the returned values will be the start value, the midpoint and then the end value.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._angle_ptr, end._angle_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Angle_steps_Angle_Angle_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Angle._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def leading(start: Angle, end: Angle, n: int) -> list[Angle]:
        """Interpolate between two values like 'steps', but skip the first value."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._angle_ptr, end._angle_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Angle_leading_Angle_Angle_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Angle._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def trailing(start: Angle, end: Angle, n: int) -> list[Angle]:
        """Interpolate between two values like 'steps', but skip the last value."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._angle_ptr, end._angle_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Angle_trailing_Angle_Angle_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Angle._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def in_between(start: Angle, end: Angle, n: int) -> list[Angle]:
        """Interpolate between two values like 'steps', but skip the first and last values."""
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._angle_ptr, end._angle_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Angle_inBetween_Angle_Angle_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Angle._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def midpoints(start: Angle, end: Angle, n: int) -> list[Angle]:
        """Subdivide a given range into the given number of steps, and return the midpoint of each step.

        This can be useful if you want to sample a curve or other function at the midpoint of several intervals.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_int64(start._angle_ptr, end._angle_ptr, n)
        output = _List_c_void_p()
        _lib.opensolid_Angle_midpoints_Angle_Angle_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Angle._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @staticmethod
    def radians(value: float) -> Angle:
        """Construct an angle from a number of radians."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Angle_radians_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @staticmethod
    def degrees(value: float) -> Angle:
        """Construct an angle from a number of degrees."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Angle_degrees_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @staticmethod
    def turns(value: float) -> Angle:
        """Construct an angle from a number of turns.

        One turn is equal to 360 degrees.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Angle_turns_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @staticmethod
    def acos(value: float) -> Angle:
        """Compute the inverse cosine of a value."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Angle_acos_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @staticmethod
    def asin(value: float) -> Angle:
        """Compute the inverse sine of a value."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Angle_asin_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @staticmethod
    def atan(value: float) -> Angle:
        """Compute the inverse tangent of a value."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Angle_atan_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def in_radians(self) -> float:
        """Convert an angle to a number of radians."""
        inputs = self._angle_ptr
        output = c_double()
        _lib.opensolid_Angle_inRadians(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_degrees(self) -> float:
        """Convert an angle to a number of degrees."""
        inputs = self._angle_ptr
        output = c_double()
        _lib.opensolid_Angle_inDegrees(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def in_turns(self) -> float:
        """Convert an angle to a number of turns.

        One turn is equal to 360 degrees.
        """
        inputs = self._angle_ptr
        output = c_double()
        _lib.opensolid_Angle_inTurns(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def is_zero(self) -> bool:
        """Check if an angle is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _angle_tolerance()._angle_ptr, self._angle_ptr
        )
        output = c_int64()
        _lib.opensolid_Angle_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def sin(self) -> float:
        """Compute the sine of an angle."""
        inputs = self._angle_ptr
        output = c_double()
        _lib.opensolid_Angle_sin(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def cos(self) -> float:
        """Compute the cosine of an angle."""
        inputs = self._angle_ptr
        output = c_double()
        _lib.opensolid_Angle_cos(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def tan(self) -> float:
        """Compute the tangent of an angle."""
        inputs = self._angle_ptr
        output = c_double()
        _lib.opensolid_Angle_tan(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def __eq__(self, other: object) -> bool:
        """Return ``self == other``.

        Note that this is an *exact* comparison; for a tolerant comparison
        (one which will return true if two values are *almost* equal)
        you'll likely want to use an ``is_zero()`` method instead.
        """
        if not isinstance(other, Angle):
            return False
        inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, other._angle_ptr)
        output = c_int64()
        _lib.opensolid_Angle_eq(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __hash__(self) -> int:
        """Return a hash code for ``self``."""
        inputs = self._angle_ptr
        output = c_int64()
        _lib.opensolid_Angle_hash(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def _compare(self, other: Angle) -> int:
        inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, other._angle_ptr)
        output = c_int64()
        _lib.opensolid_Angle_compare(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def __lt__(self, other: Angle) -> bool:
        """Return ``self < other``."""
        return self._compare(other) < 0

    def __le__(self, other: Angle) -> bool:
        """Return ``self <= other``."""
        return self._compare(other) <= 0

    def __ge__(self, other: Angle) -> bool:
        """Return ``self >= other``."""
        return self._compare(other) >= 0

    def __gt__(self, other: Angle) -> bool:
        """Return ``self > other``."""
        return self._compare(other) > 0

    def __neg__(self) -> Angle:
        """Return ``-self``."""
        inputs = self._angle_ptr
        output = c_void_p()
        _lib.opensolid_Angle_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def __abs__(self) -> Angle:
        """Return ``abs(self)``."""
        inputs = self._angle_ptr
        output = c_void_p()
        _lib.opensolid_Angle_abs(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @overload
    def __add__(self, rhs: Angle) -> Angle:
        pass

    @overload
    def __add__(self, rhs: AngleBounds) -> AngleBounds:
        pass

    @overload
    def __add__(self, rhs: AngleCurve) -> AngleCurve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_add_Angle_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Angle._new(output)
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._angle_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Angle_add_Angle_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case AngleCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._anglecurve_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_add_Angle_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: Angle) -> Angle:
        pass

    @overload
    def __sub__(self, rhs: AngleBounds) -> AngleBounds:
        pass

    @overload
    def __sub__(self, rhs: AngleCurve) -> AngleCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_sub_Angle_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Angle._new(output)
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._angle_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Angle_sub_Angle_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case AngleCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._anglecurve_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_sub_Angle_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> Angle:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> AngleBounds:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> AngleCurve:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._angle_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Angle_mul_Angle_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Angle._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_mul_Angle_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_mul_Angle_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Angle:
        pass

    @overload
    def __truediv__(self, rhs: Angle) -> float:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> AngleBounds:
        pass

    @overload
    def __truediv__(self, rhs: AngleBounds) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> AngleCurve:
        pass

    @overload
    def __truediv__(self, rhs: AngleCurve) -> Curve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._angle_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Angle_div_Angle_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Angle._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._angle_ptr)
                output = c_double()
                _lib.opensolid_Angle_div_Angle_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return output.value
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Angle_div_Angle_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._angle_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Angle_div_Angle_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._angle_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_Angle_div_Angle_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    AngleCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case AngleCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _angle_tolerance()._angle_ptr, self._angle_ptr, rhs._anglecurve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_Angle_div_Angle_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __floordiv__(self, rhs: Angle) -> int:
        """Return ``self // rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._angle_ptr)
        output = c_int64()
        _lib.opensolid_Angle_floorDiv_Angle_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return output.value

    def __mod__(self, rhs: Angle) -> Angle:
        """Return ``self % rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._angle_ptr, rhs._angle_ptr)
        output = c_void_p()
        _lib.opensolid_Angle_mod_Angle_Angle(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def __rmul__(self, lhs: float) -> Angle:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._angle_ptr)
        output = c_void_p()
        _lib.opensolid_Angle_mul_Float_Angle(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        return "Angle.radians(" + str(self.in_radians()) + ")"


def _angle_zero() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_zero(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.zero = _angle_zero()


def _angle_golden_angle() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_goldenAngle(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.golden_angle = _angle_golden_angle()


def _angle_radian() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_radian(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.radian = _angle_radian()


def _angle_full_turn() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_fullTurn(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.full_turn = _angle_full_turn()


def _angle_half_turn() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_halfTurn(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.half_turn = _angle_half_turn()


def _angle_quarter_turn() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_quarterTurn(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.quarter_turn = _angle_quarter_turn()


def _angle_pi() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_pi(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.pi = _angle_pi()


def _angle_two_pi() -> Angle:
    output = c_void_p()
    _lib.opensolid_Angle_twoPi(c_void_p(), ctypes.byref(output))
    return Angle._new(output)


Angle.two_pi = _angle_two_pi()


class Bounds:
    """A range of unitless values, with a lower bound and upper bound."""

    _bounds_ptr: c_void_p

    def __init__(self, first_value: float, second_value: float) -> None:
        """Construct a bounding range from two given values (endpoints).

        The order of the two arguments does not matter;
        the minimum of the two will be used as the lower bound
        and the maximum will be used as the upper bound.

        If either argument is NaN, then the result will be open/infinite
        (with endpoints negative infinity and positive infinity).
        """
        inputs = _Tuple2_c_double_c_double(first_value, second_value)
        self._bounds_ptr = c_void_p()
        _lib.opensolid_Bounds_constructor_Float_Float(
            ctypes.byref(inputs), ctypes.byref(self._bounds_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Bounds:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Bounds)
        obj._bounds_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._bounds_ptr)

    unit_interval: Bounds = None  # type: ignore[assignment]
    """The bounding range with endoints [0,1]."""

    @staticmethod
    def constant(value: float) -> Bounds:
        """Construct a zero-width bounding range containing a single value."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Bounds_constant_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Bounds._new(output)

    @staticmethod
    def zero_to(value: float) -> Bounds:
        """Create a bounding range with zero as one of its endpoints and the given value as the other."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Bounds_zeroTo_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Bounds._new(output)

    @staticmethod
    def symmetric(*, width: float) -> Bounds:
        """Create a bounding range symmetric about zero, with the given width.

        The lower bound of the range will be -w/2 and the upper bound will be w/2.
        """
        inputs = c_double(width)
        output = c_void_p()
        _lib.opensolid_Bounds_symmetric_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    @staticmethod
    def hull(values: list[float]) -> Bounds:
        """Build a bounding range containing all values in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_double,
                (c_double * len(values))(*[c_double(item) for item in values]),
            )
            if values
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Bounds_hull_NonEmptyFloat(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    @staticmethod
    def aggregate(bounds: list[Bounds]) -> Bounds:
        """Build a bounding range containing all ranges in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._bounds_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Bounds_aggregate_NonEmptyBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    @cached_property
    def endpoints(self) -> tuple[float, float]:
        """Get the lower and upper bounds of a range."""
        inputs = self._bounds_ptr
        output = _Tuple2_c_double_c_double()
        _lib.opensolid_Bounds_endpoints(ctypes.byref(inputs), ctypes.byref(output))
        return (output.field0, output.field1)

    @cached_property
    def lower(self) -> float:
        """Get the lower bound of a range."""
        inputs = self._bounds_ptr
        output = c_double()
        _lib.opensolid_Bounds_lower(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def upper(self) -> float:
        """Get the upper bound of a range."""
        inputs = self._bounds_ptr
        output = c_double()
        _lib.opensolid_Bounds_upper(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def intersection(self, other: Bounds) -> Bounds | None:
        """Attempt to find the intersection of two bounding ranges."""
        inputs = _Tuple2_c_void_p_c_void_p(other._bounds_ptr, self._bounds_ptr)
        output = _Maybe_c_void_p()
        _lib.opensolid_Bounds_intersection_Bounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(c_void_p(output.field1)) if output.field0 == 0 else None

    def includes(self, value: float) -> bool:
        """Check if a given value is included in a bounding range.

        Note that this does *not* use a tolerance, so use with care -
        for example, a value *just* outside the range (due to numerical roundoff)
        will be reported as not included.
        """
        inputs = _Tuple2_c_double_c_void_p(value, self._bounds_ptr)
        output = c_int64()
        _lib.opensolid_Bounds_includes_Float(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def contains(self, other: Bounds) -> bool:
        """Check if one bounding range contains another.

        Note that this does *not* use a tolerance, so use with care -
        for example, a range that extends *just* outside another range (due to numerical
        roundoff) will be reported as not contained by that range.
        """
        inputs = _Tuple2_c_void_p_c_void_p(other._bounds_ptr, self._bounds_ptr)
        output = c_int64()
        _lib.opensolid_Bounds_contains_Bounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def __neg__(self) -> Bounds:
        """Return ``-self``."""
        inputs = self._bounds_ptr
        output = c_void_p()
        _lib.opensolid_Bounds_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Bounds._new(output)

    def __abs__(self) -> Bounds:
        """Return ``abs(self)``."""
        inputs = self._bounds_ptr
        output = c_void_p()
        _lib.opensolid_Bounds_abs(ctypes.byref(inputs), ctypes.byref(output))
        return Bounds._new(output)

    @overload
    def __add__(self, rhs: float) -> Bounds:
        pass

    @overload
    def __add__(self, rhs: Bounds) -> Bounds:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._bounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Bounds_add_Bounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_add_Bounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: float) -> Bounds:
        pass

    @overload
    def __sub__(self, rhs: Bounds) -> Bounds:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._bounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Bounds_sub_Bounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_sub_Bounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> Bounds:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> Bounds:
        pass

    @overload
    def __mul__(self, rhs: Length) -> LengthBounds:
        pass

    @overload
    def __mul__(self, rhs: Area) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: Angle) -> AngleBounds:
        pass

    @overload
    def __mul__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    @overload
    def __mul__(self, rhs: AreaBounds) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: AngleBounds) -> AngleBounds:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._bounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._bounds_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._bounds_ptr, rhs._areabounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._bounds_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_Bounds_mul_Bounds_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> Bounds:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._bounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Bounds_div_Bounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(self._bounds_ptr, rhs._bounds_ptr)
                output = c_void_p()
                _lib.opensolid_Bounds_div_Bounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case _:
                return NotImplemented

    def __radd__(self, lhs: float) -> Bounds:
        """Return ``lhs <> self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._bounds_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds_add_Float_Bounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    def __rsub__(self, lhs: float) -> Bounds:
        """Return ``lhs - self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._bounds_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds_sub_Float_Bounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    def __rmul__(self, lhs: float) -> Bounds:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._bounds_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds_mul_Float_Bounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    def __rtruediv__(self, lhs: float) -> Bounds:
        """Return ``lhs / self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._bounds_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds_div_Float_Bounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        low, high = self.endpoints
        return "Bounds(" + str(low) + "," + str(high) + ")"


def _bounds_unit_interval() -> Bounds:
    output = c_void_p()
    _lib.opensolid_Bounds_unitInterval(c_void_p(), ctypes.byref(output))
    return Bounds._new(output)


Bounds.unit_interval = _bounds_unit_interval()


class LengthBounds:
    """A range of length values, with a lower bound and upper bound."""

    _lengthbounds_ptr: c_void_p

    def __init__(self, first_value: Length, second_value: Length) -> None:
        """Construct a bounding range from two given values (endpoints).

        The order of the two arguments does not matter;
        the minimum of the two will be used as the lower bound
        and the maximum will be used as the upper bound.

        If either argument is NaN, then the result will be open/infinite
        (with endpoints negative infinity and positive infinity).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            first_value._length_ptr, second_value._length_ptr
        )
        self._lengthbounds_ptr = c_void_p()
        _lib.opensolid_LengthBounds_constructor_Length_Length(
            ctypes.byref(inputs), ctypes.byref(self._lengthbounds_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> LengthBounds:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(LengthBounds)
        obj._lengthbounds_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._lengthbounds_ptr)

    @staticmethod
    def constant(value: Length) -> LengthBounds:
        """Construct a zero-width bounding range containing a single value."""
        inputs = value._length_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_constant_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthBounds._new(output)

    @staticmethod
    def zero_to(value: Length) -> LengthBounds:
        """Create a bounding range with zero as one of its endpoints and the given value as the other."""
        inputs = value._length_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_zeroTo_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthBounds._new(output)

    @staticmethod
    def symmetric(*, width: Length) -> LengthBounds:
        """Create a bounding range symmetric about zero, with the given width.

        The lower bound of the range will be -w/2 and the upper bound will be w/2.
        """
        inputs = width._length_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_symmetric_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthBounds._new(output)

    @staticmethod
    def hull(values: list[Length]) -> LengthBounds:
        """Build a bounding range containing all values in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(values))(*[item._length_ptr for item in values]),
            )
            if values
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_LengthBounds_hull_NonEmptyLength(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthBounds._new(output)

    @staticmethod
    def aggregate(bounds: list[LengthBounds]) -> LengthBounds:
        """Build a bounding range containing all ranges in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._lengthbounds_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_LengthBounds_aggregate_NonEmptyLengthBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthBounds._new(output)

    @cached_property
    def endpoints(self) -> tuple[Length, Length]:
        """Get the lower and upper bounds of a range."""
        inputs = self._lengthbounds_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_LengthBounds_endpoints(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
        )

    @cached_property
    def lower(self) -> Length:
        """Get the lower bound of a range."""
        inputs = self._lengthbounds_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_lower(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @cached_property
    def upper(self) -> Length:
        """Get the upper bound of a range."""
        inputs = self._lengthbounds_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_upper(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    def intersection(self, other: LengthBounds) -> LengthBounds | None:
        """Attempt to find the intersection of two bounding ranges."""
        inputs = _Tuple2_c_void_p_c_void_p(
            other._lengthbounds_ptr, self._lengthbounds_ptr
        )
        output = _Maybe_c_void_p()
        _lib.opensolid_LengthBounds_intersection_LengthBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            LengthBounds._new(c_void_p(output.field1)) if output.field0 == 0 else None
        )

    def includes(self, value: Length) -> bool:
        """Check if a given value is included in a bounding range.

        Note that this does *not* use a tolerance, so use with care -
        for example, a value *just* outside the range (due to numerical roundoff)
        will be reported as not included.
        """
        inputs = _Tuple2_c_void_p_c_void_p(value._length_ptr, self._lengthbounds_ptr)
        output = c_int64()
        _lib.opensolid_LengthBounds_includes_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def contains(self, other: LengthBounds) -> bool:
        """Check if one bounding range contains another.

        Note that this does *not* use a tolerance, so use with care -
        for example, a range that extends *just* outside another range (due to numerical
        roundoff) will be reported as not contained by that range.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            other._lengthbounds_ptr, self._lengthbounds_ptr
        )
        output = c_int64()
        _lib.opensolid_LengthBounds_contains_LengthBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def __neg__(self) -> LengthBounds:
        """Return ``-self``."""
        inputs = self._lengthbounds_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_neg(ctypes.byref(inputs), ctypes.byref(output))
        return LengthBounds._new(output)

    def __abs__(self) -> LengthBounds:
        """Return ``abs(self)``."""
        inputs = self._lengthbounds_ptr
        output = c_void_p()
        _lib.opensolid_LengthBounds_abs(ctypes.byref(inputs), ctypes.byref(output))
        return LengthBounds._new(output)

    @overload
    def __add__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    @overload
    def __add__(self, rhs: Length) -> LengthBounds:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_add_LengthBounds_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_add_LengthBounds_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    @overload
    def __sub__(self, rhs: Length) -> LengthBounds:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_sub_LengthBounds_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_sub_LengthBounds_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> LengthBounds:
        pass

    @overload
    def __mul__(self, rhs: LengthBounds) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: Length) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> LengthBounds:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._lengthbounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_LengthBounds_mul_LengthBounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_mul_LengthBounds_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_mul_LengthBounds_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._bounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_mul_LengthBounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> LengthBounds:
        pass

    @overload
    def __truediv__(self, rhs: LengthBounds) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> LengthBounds:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._lengthbounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_LengthBounds_div_LengthBounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_div_LengthBounds_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_div_LengthBounds_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthbounds_ptr, rhs._bounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthBounds_div_LengthBounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> LengthBounds:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._lengthbounds_ptr)
        output = c_void_p()
        _lib.opensolid_LengthBounds_mul_Float_LengthBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthBounds._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        low, high = self.endpoints
        return "LengthBounds(" + repr(low) + "," + repr(high) + ")"


class AreaBounds:
    """A range of area values, with a lower bound and upper bound."""

    _areabounds_ptr: c_void_p

    def __init__(self, first_value: Area, second_value: Area) -> None:
        """Construct a bounding range from two given values (endpoints).

        The order of the two arguments does not matter;
        the minimum of the two will be used as the lower bound
        and the maximum will be used as the upper bound.

        If either argument is NaN, then the result will be open/infinite
        (with endpoints negative infinity and positive infinity).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            first_value._area_ptr, second_value._area_ptr
        )
        self._areabounds_ptr = c_void_p()
        _lib.opensolid_AreaBounds_constructor_Area_Area(
            ctypes.byref(inputs), ctypes.byref(self._areabounds_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> AreaBounds:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(AreaBounds)
        obj._areabounds_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._areabounds_ptr)

    @staticmethod
    def constant(value: Area) -> AreaBounds:
        """Construct a zero-width bounding range containing a single value."""
        inputs = value._area_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_constant_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(output)

    @staticmethod
    def zero_to(value: Area) -> AreaBounds:
        """Create a bounding range with zero as one of its endpoints and the given value as the other."""
        inputs = value._area_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_zeroTo_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(output)

    @staticmethod
    def symmetric(*, width: Area) -> AreaBounds:
        """Create a bounding range symmetric about zero, with the given width.

        The lower bound of the range will be -w/2 and the upper bound will be w/2.
        """
        inputs = width._area_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_symmetric_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(output)

    @staticmethod
    def hull(values: list[Area]) -> AreaBounds:
        """Build a bounding range containing all values in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(values))(*[item._area_ptr for item in values]),
            )
            if values
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_AreaBounds_hull_NonEmptyArea(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(output)

    @staticmethod
    def aggregate(bounds: list[AreaBounds]) -> AreaBounds:
        """Build a bounding range containing all ranges in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._areabounds_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_AreaBounds_aggregate_NonEmptyAreaBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(output)

    @cached_property
    def endpoints(self) -> tuple[Area, Area]:
        """Get the lower and upper bounds of a range."""
        inputs = self._areabounds_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_AreaBounds_endpoints(ctypes.byref(inputs), ctypes.byref(output))
        return (Area._new(c_void_p(output.field0)), Area._new(c_void_p(output.field1)))

    @cached_property
    def lower(self) -> Area:
        """Get the lower bound of a range."""
        inputs = self._areabounds_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_lower(ctypes.byref(inputs), ctypes.byref(output))
        return Area._new(output)

    @cached_property
    def upper(self) -> Area:
        """Get the upper bound of a range."""
        inputs = self._areabounds_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_upper(ctypes.byref(inputs), ctypes.byref(output))
        return Area._new(output)

    def intersection(self, other: AreaBounds) -> AreaBounds | None:
        """Attempt to find the intersection of two bounding ranges."""
        inputs = _Tuple2_c_void_p_c_void_p(other._areabounds_ptr, self._areabounds_ptr)
        output = _Maybe_c_void_p()
        _lib.opensolid_AreaBounds_intersection_AreaBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(c_void_p(output.field1)) if output.field0 == 0 else None

    def includes(self, value: Area) -> bool:
        """Check if a given value is included in a bounding range.

        Note that this does *not* use a tolerance, so use with care -
        for example, a value *just* outside the range (due to numerical roundoff)
        will be reported as not included.
        """
        inputs = _Tuple2_c_void_p_c_void_p(value._area_ptr, self._areabounds_ptr)
        output = c_int64()
        _lib.opensolid_AreaBounds_includes_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def contains(self, other: AreaBounds) -> bool:
        """Check if one bounding range contains another.

        Note that this does *not* use a tolerance, so use with care -
        for example, a range that extends *just* outside another range (due to numerical
        roundoff) will be reported as not contained by that range.
        """
        inputs = _Tuple2_c_void_p_c_void_p(other._areabounds_ptr, self._areabounds_ptr)
        output = c_int64()
        _lib.opensolid_AreaBounds_contains_AreaBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def __neg__(self) -> AreaBounds:
        """Return ``-self``."""
        inputs = self._areabounds_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_neg(ctypes.byref(inputs), ctypes.byref(output))
        return AreaBounds._new(output)

    def __abs__(self) -> AreaBounds:
        """Return ``abs(self)``."""
        inputs = self._areabounds_ptr
        output = c_void_p()
        _lib.opensolid_AreaBounds_abs(ctypes.byref(inputs), ctypes.byref(output))
        return AreaBounds._new(output)

    @overload
    def __add__(self, rhs: AreaBounds) -> AreaBounds:
        pass

    @overload
    def __add__(self, rhs: Area) -> AreaBounds:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._areabounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_add_AreaBounds_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._areabounds_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_AreaBounds_add_AreaBounds_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: AreaBounds) -> AreaBounds:
        pass

    @overload
    def __sub__(self, rhs: Area) -> AreaBounds:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._areabounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_sub_AreaBounds_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._areabounds_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_AreaBounds_sub_AreaBounds_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> AreaBounds:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> AreaBounds:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._areabounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AreaBounds_mul_AreaBounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._bounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_mul_AreaBounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> AreaBounds:
        pass

    @overload
    def __truediv__(self, rhs: AreaBounds) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> LengthBounds:
        pass

    @overload
    def __truediv__(self, rhs: Area) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> AreaBounds:
        pass

    @overload
    def __truediv__(self, rhs: LengthBounds) -> LengthBounds:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._areabounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AreaBounds_div_AreaBounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case AreaBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._areabounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_div_AreaBounds_AreaBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_div_AreaBounds_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._areabounds_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_AreaBounds_div_AreaBounds_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._bounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_div_AreaBounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaBounds._new(output)
            case LengthBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areabounds_ptr, rhs._lengthbounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaBounds_div_AreaBounds_LengthBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthBounds._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> AreaBounds:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._areabounds_ptr)
        output = c_void_p()
        _lib.opensolid_AreaBounds_mul_Float_AreaBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaBounds._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        low, high = self.endpoints
        return "AreaBounds(" + repr(low) + "," + repr(high) + ")"


class AngleBounds:
    """A range of angle values, with a lower bound and upper bound."""

    _anglebounds_ptr: c_void_p

    def __init__(self, first_value: Angle, second_value: Angle) -> None:
        """Construct a bounding range from two given values (endpoints).

        The order of the two arguments does not matter;
        the minimum of the two will be used as the lower bound
        and the maximum will be used as the upper bound.

        If either argument is NaN, then the result will be open/infinite
        (with endpoints negative infinity and positive infinity).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            first_value._angle_ptr, second_value._angle_ptr
        )
        self._anglebounds_ptr = c_void_p()
        _lib.opensolid_AngleBounds_constructor_Angle_Angle(
            ctypes.byref(inputs), ctypes.byref(self._anglebounds_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> AngleBounds:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(AngleBounds)
        obj._anglebounds_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._anglebounds_ptr)

    @staticmethod
    def constant(value: Angle) -> AngleBounds:
        """Construct a zero-width bounding range containing a single value."""
        inputs = value._angle_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_constant_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(output)

    @staticmethod
    def zero_to(value: Angle) -> AngleBounds:
        """Create a bounding range with zero as one of its endpoints and the given value as the other."""
        inputs = value._angle_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_zeroTo_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(output)

    @staticmethod
    def symmetric(*, width: Angle) -> AngleBounds:
        """Create a bounding range symmetric about zero, with the given width.

        The lower bound of the range will be -w/2 and the upper bound will be w/2.
        """
        inputs = width._angle_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_symmetric_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(output)

    @staticmethod
    def hull(values: list[Angle]) -> AngleBounds:
        """Build a bounding range containing all values in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(values))(*[item._angle_ptr for item in values]),
            )
            if values
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_AngleBounds_hull_NonEmptyAngle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(output)

    @staticmethod
    def aggregate(bounds: list[AngleBounds]) -> AngleBounds:
        """Build a bounding range containing all ranges in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._anglebounds_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_AngleBounds_aggregate_NonEmptyAngleBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(output)

    @cached_property
    def endpoints(self) -> tuple[Angle, Angle]:
        """Get the lower and upper bounds of a range."""
        inputs = self._anglebounds_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_AngleBounds_endpoints(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Angle._new(c_void_p(output.field0)),
            Angle._new(c_void_p(output.field1)),
        )

    @cached_property
    def lower(self) -> Angle:
        """Get the lower bound of a range."""
        inputs = self._anglebounds_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_lower(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    @cached_property
    def upper(self) -> Angle:
        """Get the upper bound of a range."""
        inputs = self._anglebounds_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_upper(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def intersection(self, other: AngleBounds) -> AngleBounds | None:
        """Attempt to find the intersection of two bounding ranges."""
        inputs = _Tuple2_c_void_p_c_void_p(
            other._anglebounds_ptr, self._anglebounds_ptr
        )
        output = _Maybe_c_void_p()
        _lib.opensolid_AngleBounds_intersection_AngleBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(c_void_p(output.field1)) if output.field0 == 0 else None

    def includes(self, value: Angle) -> bool:
        """Check if a given value is included in a bounding range.

        Note that this does *not* use a tolerance, so use with care -
        for example, a value *just* outside the range (due to numerical roundoff)
        will be reported as not included.
        """
        inputs = _Tuple2_c_void_p_c_void_p(value._angle_ptr, self._anglebounds_ptr)
        output = c_int64()
        _lib.opensolid_AngleBounds_includes_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def contains(self, other: AngleBounds) -> bool:
        """Check if one bounding range contains another.

        Note that this does *not* use a tolerance, so use with care -
        for example, a range that extends *just* outside another range (due to numerical
        roundoff) will be reported as not contained by that range.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            other._anglebounds_ptr, self._anglebounds_ptr
        )
        output = c_int64()
        _lib.opensolid_AngleBounds_contains_AngleBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return bool(output.value)

    def __neg__(self) -> AngleBounds:
        """Return ``-self``."""
        inputs = self._anglebounds_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_neg(ctypes.byref(inputs), ctypes.byref(output))
        return AngleBounds._new(output)

    def __abs__(self) -> AngleBounds:
        """Return ``abs(self)``."""
        inputs = self._anglebounds_ptr
        output = c_void_p()
        _lib.opensolid_AngleBounds_abs(ctypes.byref(inputs), ctypes.byref(output))
        return AngleBounds._new(output)

    @overload
    def __add__(self, rhs: AngleBounds) -> AngleBounds:
        pass

    @overload
    def __add__(self, rhs: Angle) -> AngleBounds:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_add_AngleBounds_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._angle_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_add_AngleBounds_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: AngleBounds) -> AngleBounds:
        pass

    @overload
    def __sub__(self, rhs: Angle) -> AngleBounds:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_sub_AngleBounds_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._angle_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_sub_AngleBounds_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> AngleBounds:
        pass

    @overload
    def __mul__(self, rhs: Bounds) -> AngleBounds:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._anglebounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AngleBounds_mul_AngleBounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._bounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_mul_AngleBounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> AngleBounds:
        pass

    @overload
    def __truediv__(self, rhs: AngleBounds) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Angle) -> Bounds:
        pass

    @overload
    def __truediv__(self, rhs: Bounds) -> AngleBounds:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._anglebounds_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AngleBounds_div_AngleBounds_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case AngleBounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._anglebounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_div_AngleBounds_AngleBounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._angle_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_div_AngleBounds_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Bounds._new(output)
            case Bounds():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglebounds_ptr, rhs._bounds_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleBounds_div_AngleBounds_Bounds(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleBounds._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> AngleBounds:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._anglebounds_ptr)
        output = c_void_p()
        _lib.opensolid_AngleBounds_mul_Float_AngleBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleBounds._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        low, high = self.endpoints
        return "AngleBounds(" + repr(low) + "," + repr(high) + ")"


class Color:
    """An RGB color value."""

    _color_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Color:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Color)
        obj._color_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._color_ptr)

    red: Color = None  # type: ignore[assignment]
    """Scarlet Red from the Tango icon theme."""

    dark_red: Color = None  # type: ignore[assignment]
    """Dark Scarlet Red from the Tango icon theme."""

    light_orange: Color = None  # type: ignore[assignment]
    """Light Orange from the Tango icon theme."""

    orange: Color = None  # type: ignore[assignment]
    """Orange from the Tango icon theme."""

    dark_orange: Color = None  # type: ignore[assignment]
    """Dark Orange from the Tango icon theme."""

    light_yellow: Color = None  # type: ignore[assignment]
    """Light Butter from the Tango icon theme."""

    yellow: Color = None  # type: ignore[assignment]
    """Butter from the Tango icon theme."""

    dark_yellow: Color = None  # type: ignore[assignment]
    """Dark Butter from the Tango icon theme."""

    light_green: Color = None  # type: ignore[assignment]
    """Light Chameleon from the Tango icon theme."""

    green: Color = None  # type: ignore[assignment]
    """Chameleon from the Tango icon theme."""

    dark_green: Color = None  # type: ignore[assignment]
    """Dark Chameleon from the Tango icon theme."""

    light_blue: Color = None  # type: ignore[assignment]
    """Light Sky Blue from the Tango icon theme."""

    blue: Color = None  # type: ignore[assignment]
    """Sky Blue from the Tango icon theme."""

    dark_blue: Color = None  # type: ignore[assignment]
    """Dark Sky Blue from the Tango icon theme."""

    light_purple: Color = None  # type: ignore[assignment]
    """Light Plum from the Tango icon theme."""

    purple: Color = None  # type: ignore[assignment]
    """Plum from the Tango icon theme."""

    dark_purple: Color = None  # type: ignore[assignment]
    """Dark Plum from the Tango icon theme."""

    light_brown: Color = None  # type: ignore[assignment]
    """Light Chocolate from the Tango icon theme."""

    brown: Color = None  # type: ignore[assignment]
    """Chocolate from the Tango icon theme."""

    dark_brown: Color = None  # type: ignore[assignment]
    """Dark Chocolate from the Tango icon theme."""

    black: Color = None  # type: ignore[assignment]
    """Black."""

    white: Color = None  # type: ignore[assignment]
    """White."""

    light_grey: Color = None  # type: ignore[assignment]
    """Aluminium 1/6 from the Tango icon theme."""

    grey: Color = None  # type: ignore[assignment]
    """Aluminium 2/6 from the Tango icon theme."""

    dark_grey: Color = None  # type: ignore[assignment]
    """Aluminium 3/6 from the Tango icon theme."""

    light_gray: Color = None  # type: ignore[assignment]
    """Aluminium 1/6 from the Tango icon theme."""

    gray: Color = None  # type: ignore[assignment]
    """Aluminium 2/6 from the Tango icon theme."""

    dark_gray: Color = None  # type: ignore[assignment]
    """Aluminium 3/6 from the Tango icon theme."""

    light_charcoal: Color = None  # type: ignore[assignment]
    """Aluminium 4/6 from the Tango icon theme."""

    charcoal: Color = None  # type: ignore[assignment]
    """Aluminium 5/6 from the Tango icon theme."""

    dark_charcoal: Color = None  # type: ignore[assignment]
    """Aluminium 6/6 from the Tango icon theme."""

    @staticmethod
    def rgb_float(red: float, green: float, blue: float) -> Color:
        """Construct a color from its RGB components, in the range [0,1]."""
        inputs = _Tuple3_c_double_c_double_c_double(red, green, blue)
        output = c_void_p()
        _lib.opensolid_Color_rgbFloat_Float_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Color._new(output)

    @staticmethod
    def rgb_int(red: int, green: int, blue: int) -> Color:
        """Construct a color from its RGB components, in the range [0,255]."""
        inputs = _Tuple3_c_int64_c_int64_c_int64(red, green, blue)
        output = c_void_p()
        _lib.opensolid_Color_rgbInt_Int_Int_Int(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Color._new(output)

    @staticmethod
    def hsl(hue: Angle, saturation: float, lightness: float) -> Color:
        """Construct a color from its hue, saturation and lightness values."""
        inputs = _Tuple3_c_void_p_c_double_c_double(
            hue._angle_ptr, saturation, lightness
        )
        output = c_void_p()
        _lib.opensolid_Color_hsl_Angle_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Color._new(output)

    @staticmethod
    def from_hex(hex_string: str) -> Color:
        """Construct a color from a hex string such as '#f3f3f3' or 'f3f3f3'."""
        inputs = _str_to_text(hex_string)
        output = c_void_p()
        _lib.opensolid_Color_fromHex_Text(ctypes.byref(inputs), ctypes.byref(output))
        return Color._new(output)

    @cached_property
    def rgb_float_components(self) -> tuple[float, float, float]:
        """Get the RGB components of a color as values in the range [0,1]."""
        inputs = self._color_ptr
        output = _Tuple3_c_double_c_double_c_double()
        _lib.opensolid_Color_rgbFloatComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (output.field0, output.field1, output.field2)

    @cached_property
    def rgb_int_components(self) -> tuple[int, int, int]:
        """Get the RGB components of a color as values in the range [0,255]."""
        inputs = self._color_ptr
        output = _Tuple3_c_int64_c_int64_c_int64()
        _lib.opensolid_Color_rgbIntComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (output.field0, output.field1, output.field2)

    def to_hex(self) -> str:
        """Convert a color to a hex string such as '#f3f3f3'."""
        inputs = self._color_ptr
        output = _Text()
        _lib.opensolid_Color_toHex(ctypes.byref(inputs), ctypes.byref(output))
        return _text_to_str(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        r, g, b = self.rgb_int_components
        return "Color.rgb_int(" + str(r) + "," + str(g) + "," + str(b) + ")"


def _color_red() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_red(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.red = _color_red()


def _color_dark_red() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkRed(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_red = _color_dark_red()


def _color_light_orange() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightOrange(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_orange = _color_light_orange()


def _color_orange() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_orange(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.orange = _color_orange()


def _color_dark_orange() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkOrange(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_orange = _color_dark_orange()


def _color_light_yellow() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightYellow(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_yellow = _color_light_yellow()


def _color_yellow() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_yellow(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.yellow = _color_yellow()


def _color_dark_yellow() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkYellow(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_yellow = _color_dark_yellow()


def _color_light_green() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightGreen(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_green = _color_light_green()


def _color_green() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_green(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.green = _color_green()


def _color_dark_green() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkGreen(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_green = _color_dark_green()


def _color_light_blue() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightBlue(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_blue = _color_light_blue()


def _color_blue() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_blue(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.blue = _color_blue()


def _color_dark_blue() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkBlue(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_blue = _color_dark_blue()


def _color_light_purple() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightPurple(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_purple = _color_light_purple()


def _color_purple() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_purple(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.purple = _color_purple()


def _color_dark_purple() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkPurple(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_purple = _color_dark_purple()


def _color_light_brown() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightBrown(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_brown = _color_light_brown()


def _color_brown() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_brown(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.brown = _color_brown()


def _color_dark_brown() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkBrown(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_brown = _color_dark_brown()


def _color_black() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_black(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.black = _color_black()


def _color_white() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_white(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.white = _color_white()


def _color_light_grey() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightGrey(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_grey = _color_light_grey()


def _color_grey() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_grey(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.grey = _color_grey()


def _color_dark_grey() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkGrey(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_grey = _color_dark_grey()


def _color_light_gray() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightGray(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_gray = _color_light_gray()


def _color_gray() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_gray(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.gray = _color_gray()


def _color_dark_gray() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkGray(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_gray = _color_dark_gray()


def _color_light_charcoal() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_lightCharcoal(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.light_charcoal = _color_light_charcoal()


def _color_charcoal() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_charcoal(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.charcoal = _color_charcoal()


def _color_dark_charcoal() -> Color:
    output = c_void_p()
    _lib.opensolid_Color_darkCharcoal(c_void_p(), ctypes.byref(output))
    return Color._new(output)


Color.dark_charcoal = _color_dark_charcoal()


class Vector2d:
    """A unitless vector in 2D."""

    _vector2d_ptr: c_void_p

    def __init__(self, x_component: float, y_component: float) -> None:
        """Construct a vector from its X and Y components."""
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        self._vector2d_ptr = c_void_p()
        _lib.opensolid_Vector2d_constructor_Float_Float(
            ctypes.byref(inputs), ctypes.byref(self._vector2d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Vector2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Vector2d)
        obj._vector2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._vector2d_ptr)

    zero: Vector2d = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def unit(direction: Direction2d) -> Vector2d:
        """Construct a unit vector in the given direction."""
        inputs = direction._direction2d_ptr
        output = c_void_p()
        _lib.opensolid_Vector2d_unit_Direction2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    @staticmethod
    def y(y_component: float) -> Vector2d:
        """Construct a vector from just a Y component.

        The X component will be set to zero.
        """
        inputs = c_double(y_component)
        output = c_void_p()
        _lib.opensolid_Vector2d_y_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Vector2d._new(output)

    @staticmethod
    def x(x_component: float) -> Vector2d:
        """Construct a vector from just an X component.

        The Y component will be set to zero.
        """
        inputs = c_double(x_component)
        output = c_void_p()
        _lib.opensolid_Vector2d_x_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Vector2d._new(output)

    @staticmethod
    def polar(magnitude: float, angle: Angle) -> Vector2d:
        """Construct a vector from its magnitude (length) and angle."""
        inputs = _Tuple2_c_double_c_void_p(magnitude, angle._angle_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_polar_Float_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    @cached_property
    def components(self) -> tuple[float, float]:
        """Get the X and Y components of a vector as a tuple."""
        inputs = self._vector2d_ptr
        output = _Tuple2_c_double_c_double()
        _lib.opensolid_Vector2d_components(ctypes.byref(inputs), ctypes.byref(output))
        return (output.field0, output.field1)

    @cached_property
    def x_component(self) -> float:
        """Get the X component of a vector."""
        inputs = self._vector2d_ptr
        output = c_double()
        _lib.opensolid_Vector2d_xComponent(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def y_component(self) -> float:
        """Get the Y component of a vector."""
        inputs = self._vector2d_ptr
        output = c_double()
        _lib.opensolid_Vector2d_yComponent(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def angle(self) -> Angle:
        """Get the angle of a vector.

        The angle is measured counterclockwise from the positive X axis, so:

          * A vector in the positive X direction has an angle of zero.
          * A vector in the positive Y direction has an angle of 90 degrees.
          * A vector in the negative Y direction has an angle of -90 degrees.
          * It is not defined whether a vector exactly in the negative X direction has
            an angle of -180 or +180 degrees. (Currently it is reported as having an
            angle of +180 degrees, but this should not be relied upon.)

        The returned angle will be between -180 and +180 degrees.
        """
        inputs = self._vector2d_ptr
        output = c_void_p()
        _lib.opensolid_Vector2d_angle(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def direction(self) -> Direction2d:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._vector2d_ptr)
        output = _Result_c_void_p()
        _lib.opensolid_Vector2d_direction(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Direction2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def normalize(self) -> Vector2d:
        """Normalize a vector.

        If the original vector is exactly zero, then the result will be zero as well.
        Otherwise, the result will be a unit vector.
        """
        inputs = self._vector2d_ptr
        output = c_void_p()
        _lib.opensolid_Vector2d_normalize(ctypes.byref(inputs), ctypes.byref(output))
        return Vector2d._new(output)

    def angle_to(self, other: Vector2d) -> Angle:
        """Measure the signed angle from one vector to another.

        The angle will be measured counterclockwise from the first vector to the
        second, and will always be between -180 and +180 degrees.
        """
        inputs = _Tuple2_c_void_p_c_void_p(other._vector2d_ptr, self._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_angleTo_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    def is_zero(self) -> bool:
        """Check if a vector is zero, within the current tolerance."""
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._vector2d_ptr)
        output = c_int64()
        _lib.opensolid_Vector2d_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def place_on(self, plane: Plane3d) -> Vector3d:
        """Convert a 2D vector to 3D vector by placing it on a plane.

        Given a 2D vector defined within a plane's coordinate system,
        this returns the corresponding 3D vector.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_placeOn_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def rotate_left(self) -> Vector2d:
        """Rotate a vector left (counterclockwise) by 90 degrees."""
        inputs = self._vector2d_ptr
        output = c_void_p()
        _lib.opensolid_Vector2d_rotateLeft(ctypes.byref(inputs), ctypes.byref(output))
        return Vector2d._new(output)

    def rotate_right(self) -> Vector2d:
        """Rotate a vector right (clockwise) by 90 degrees."""
        inputs = self._vector2d_ptr
        output = c_void_p()
        _lib.opensolid_Vector2d_rotateRight(ctypes.byref(inputs), ctypes.byref(output))
        return Vector2d._new(output)

    def rotate_by(self, angle: Angle) -> Vector2d:
        """Rotate a vector by a given angle.

        A positive angle corresponds to a counterclockwise rotation.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_rotateBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def mirror_in(self, direction: Direction2d) -> Vector2d:
        """Mirror a vector in/along a given direction.

        For example, mirroring in the X direction
        will negate the vector's X component and leave its Y component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction2d_ptr, self._vector2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Vector2d_mirrorIn_Direction2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Vector2d:
        """Mirror a vector across a given axis.

        The origin point of the axis is not used, only its direction, since vectors have no position.
        For example, mirroring a vector across *any* axis parallel to the X axis
        will negate the vector's Y component while leaving its X component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def __neg__(self) -> Vector2d:
        """Return ``-self``."""
        inputs = self._vector2d_ptr
        output = c_void_p()
        _lib.opensolid_Vector2d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Vector2d._new(output)

    def __add__(self, rhs: Vector2d) -> Vector2d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._vector2d_ptr, rhs._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_add_Vector2d_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def __sub__(self, rhs: Vector2d) -> Vector2d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._vector2d_ptr, rhs._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_sub_Vector2d_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    @overload
    def __mul__(self, rhs: float) -> Vector2d:
        pass

    @overload
    def __mul__(self, rhs: Length) -> Displacement2d:
        pass

    @overload
    def __mul__(self, rhs: Area) -> AreaVector2d:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._vector2d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Vector2d_mul_Vector2d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector2d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._vector2d_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Vector2d_mul_Vector2d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._vector2d_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_Vector2d_mul_Vector2d_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector2d._new(output)
            case _:
                return NotImplemented

    def __truediv__(self, rhs: float) -> Vector2d:
        """Return ``self / rhs``."""
        inputs = _Tuple2_c_void_p_c_double(self._vector2d_ptr, rhs)
        output = c_void_p()
        _lib.opensolid_Vector2d_div_Vector2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    @overload
    def dot(self, rhs: Vector2d) -> float:
        pass

    @overload
    def dot(self, rhs: Displacement2d) -> Length:
        pass

    @overload
    def dot(self, rhs: AreaVector2d) -> Area:
        pass

    def dot(self, rhs):
        """Compute the dot product of two vector-like values."""
        match rhs:
            case Vector2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector2d_ptr, rhs._vector2d_ptr
                )
                output = c_double()
                _lib.opensolid_Vector2d_dot_Vector2d_Vector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return output.value
            case Displacement2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector2d_ptr, rhs._displacement2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector2d_dot_Vector2d_Displacement2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case AreaVector2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector2d_ptr, rhs._areavector2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector2d_dot_Vector2d_AreaVector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case _:
                return NotImplemented

    @overload
    def cross(self, rhs: Vector2d) -> float:
        pass

    @overload
    def cross(self, rhs: Displacement2d) -> Length:
        pass

    @overload
    def cross(self, rhs: AreaVector2d) -> Area:
        pass

    def cross(self, rhs):
        """Compute the cross product of two vector-like values."""
        match rhs:
            case Vector2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector2d_ptr, rhs._vector2d_ptr
                )
                output = c_double()
                _lib.opensolid_Vector2d_cross_Vector2d_Vector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return output.value
            case Displacement2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector2d_ptr, rhs._displacement2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector2d_cross_Vector2d_Displacement2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case AreaVector2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector2d_ptr, rhs._areavector2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector2d_cross_Vector2d_AreaVector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> Vector2d:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector2d_mul_Float_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        x, y = self.components
        return "Vector2d(" + str(x) + "," + str(y) + ")"


def _vector2d_zero() -> Vector2d:
    output = c_void_p()
    _lib.opensolid_Vector2d_zero(c_void_p(), ctypes.byref(output))
    return Vector2d._new(output)


Vector2d.zero = _vector2d_zero()


class Displacement2d:
    """A displacement vector in 2D."""

    _displacement2d_ptr: c_void_p

    def __init__(self, x_component: Length, y_component: Length) -> None:
        """Construct a vector from its X and Y components."""
        inputs = _Tuple2_c_void_p_c_void_p(
            x_component._length_ptr, y_component._length_ptr
        )
        self._displacement2d_ptr = c_void_p()
        _lib.opensolid_Displacement2d_constructor_Length_Length(
            ctypes.byref(inputs), ctypes.byref(self._displacement2d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Displacement2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Displacement2d)
        obj._displacement2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._displacement2d_ptr)

    zero: Displacement2d = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def x(x_component: Length) -> Displacement2d:
        """Construct a vector from just an X component.

        The Y component will be set to zero.
        """
        inputs = x_component._length_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_x_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def y(y_component: Length) -> Displacement2d:
        """Construct a vector from just a Y component.

        The X component will be set to zero.
        """
        inputs = y_component._length_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_y_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def polar(magnitude: Length, angle: Angle) -> Displacement2d:
        """Construct a vector from its magnitude (length) and angle."""
        inputs = _Tuple2_c_void_p_c_void_p(magnitude._length_ptr, angle._angle_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement2d_polar_Length_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def meters(x_component: float, y_component: float) -> Displacement2d:
        """Construct a vector from its X and Y components given in meters."""
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_Displacement2d_meters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def centimeters(x_component: float, y_component: float) -> Displacement2d:
        """Construct a vector from its X and Y components given in centimeters."""
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_Displacement2d_centimeters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def cm(x_component: float, y_component: float) -> Displacement2d:
        """Construct a vector from its X and Y components given in centimeters.

        Short form alias for 'centimeters'.
        """
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_Displacement2d_cm_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def millimeters(x_component: float, y_component: float) -> Displacement2d:
        """Construct a vector from its X and Y components given in millimeters."""
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_Displacement2d_millimeters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def mm(x_component: float, y_component: float) -> Displacement2d:
        """Construct a vector from its X and Y components given in millimeters.

        Short form alias for 'millimeters'.
        """
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_Displacement2d_mm_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @staticmethod
    def inches(x_component: float, y_component: float) -> Displacement2d:
        """Construct a vector from its X and Y components given in inches."""
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_Displacement2d_inches_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @cached_property
    def components(self) -> tuple[Length, Length]:
        """Get the X and Y components of a vector as a tuple."""
        inputs = self._displacement2d_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_Displacement2d_components(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
        )

    @cached_property
    def x_component(self) -> Length:
        """Get the X component of a vector."""
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_xComponent(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @cached_property
    def y_component(self) -> Length:
        """Get the Y component of a vector."""
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_yComponent(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @cached_property
    def angle(self) -> Angle:
        """Get the angle of a vector.

        The angle is measured counterclockwise from the positive X axis, so:

          * A vector in the positive X direction has an angle of zero.
          * A vector in the positive Y direction has an angle of 90 degrees.
          * A vector in the negative Y direction has an angle of -90 degrees.
          * It is not defined whether a vector exactly in the negative X direction has
            an angle of -180 or +180 degrees. (Currently it is reported as having an
            angle of +180 degrees, but this should not be relied upon.)

        The returned angle will be between -180 and +180 degrees.
        """
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_angle(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def direction(self) -> Direction2d:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._displacement2d_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_Displacement2d_direction(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Direction2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def normalize(self) -> Vector2d:
        """Normalize a vector.

        If the original vector is exactly zero, then the result will be zero as well.
        Otherwise, the result will be a unit vector.
        """
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_normalize(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def angle_to(self, other: Displacement2d) -> Angle:
        """Measure the signed angle from one vector to another.

        The angle will be measured counterclockwise from the first vector to the
        second, and will always be between -180 and +180 degrees.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            other._displacement2d_ptr, self._displacement2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement2d_angleTo_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    def is_zero(self) -> bool:
        """Check if a displacement is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._displacement2d_ptr
        )
        output = c_int64()
        _lib.opensolid_Displacement2d_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def place_on(self, plane: Plane3d) -> Displacement3d:
        """Convert a 2D vector to 3D vector by placing it on a plane.

        Given a 2D vector defined within a plane's coordinate system,
        this returns the corresponding 3D vector.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement2d_placeOn_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def rotate_left(self) -> Displacement2d:
        """Rotate a vector left (counterclockwise) by 90 degrees."""
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_rotateLeft(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def rotate_right(self) -> Displacement2d:
        """Rotate a vector right (clockwise) by 90 degrees."""
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_rotateRight(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def rotate_by(self, angle: Angle) -> Displacement2d:
        """Rotate a vector by a given angle.

        A positive angle corresponds to a counterclockwise rotation.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement2d_rotateBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def mirror_in(self, direction: Direction2d) -> Displacement2d:
        """Mirror a vector in/along a given direction.

        For example, mirroring in the X direction
        will negate the vector's X component and leave its Y component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction2d_ptr, self._displacement2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement2d_mirrorIn_Direction2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Displacement2d:
        """Mirror a vector across a given axis.

        The origin point of the axis is not used, only its direction, since vectors have no position.
        For example, mirroring a vector across *any* axis parallel to the X axis
        will negate the vector's Y component while leaving its X component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def __neg__(self) -> Displacement2d:
        """Return ``-self``."""
        inputs = self._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement2d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Displacement2d._new(output)

    def __add__(self, rhs: Displacement2d) -> Displacement2d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._displacement2d_ptr, rhs._displacement2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement2d_add_Displacement2d_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def __sub__(self, rhs: Displacement2d) -> Displacement2d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._displacement2d_ptr, rhs._displacement2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement2d_sub_Displacement2d_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    @overload
    def __mul__(self, rhs: float) -> Displacement2d:
        pass

    @overload
    def __mul__(self, rhs: Length) -> AreaVector2d:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._displacement2d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Displacement2d_mul_Displacement2d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement2d_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement2d_mul_Displacement2d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector2d._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Displacement2d:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Vector2d:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._displacement2d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Displacement2d_div_Displacement2d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement2d_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement2d_div_Displacement2d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector2d._new(output)
            case _:
                return NotImplemented

    @overload
    def dot(self, rhs: Displacement2d) -> Area:
        pass

    @overload
    def dot(self, rhs: Vector2d) -> Length:
        pass

    def dot(self, rhs):
        """Compute the dot product of two vector-like values."""
        match rhs:
            case Displacement2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement2d_ptr, rhs._displacement2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement2d_dot_Displacement2d_Displacement2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case Vector2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement2d_ptr, rhs._vector2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement2d_dot_Displacement2d_Vector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case _:
                return NotImplemented

    @overload
    def cross(self, rhs: Displacement2d) -> Area:
        pass

    @overload
    def cross(self, rhs: Vector2d) -> Length:
        pass

    def cross(self, rhs):
        """Compute the cross product of two vector-like values."""
        match rhs:
            case Displacement2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement2d_ptr, rhs._displacement2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement2d_cross_Displacement2d_Displacement2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case Vector2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement2d_ptr, rhs._vector2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement2d_cross_Displacement2d_Vector2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> Displacement2d:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement2d_mul_Float_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        x, y = self.components
        return "Displacement2d(" + repr(x) + "," + repr(y) + ")"


def _displacement2d_zero() -> Displacement2d:
    output = c_void_p()
    _lib.opensolid_Displacement2d_zero(c_void_p(), ctypes.byref(output))
    return Displacement2d._new(output)


Displacement2d.zero = _displacement2d_zero()


class AreaVector2d:
    """A vector in 2D with units of area."""

    _areavector2d_ptr: c_void_p

    def __init__(self, x_component: Area, y_component: Area) -> None:
        """Construct a vector from its X and Y components."""
        inputs = _Tuple2_c_void_p_c_void_p(x_component._area_ptr, y_component._area_ptr)
        self._areavector2d_ptr = c_void_p()
        _lib.opensolid_AreaVector2d_constructor_Area_Area(
            ctypes.byref(inputs), ctypes.byref(self._areavector2d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> AreaVector2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(AreaVector2d)
        obj._areavector2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._areavector2d_ptr)

    zero: AreaVector2d = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def x(x_component: Area) -> AreaVector2d:
        """Construct a vector from just an X component.

        The Y component will be set to zero.
        """
        inputs = x_component._area_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_x_Area(ctypes.byref(inputs), ctypes.byref(output))
        return AreaVector2d._new(output)

    @staticmethod
    def y(y_component: Area) -> AreaVector2d:
        """Construct a vector from just a Y component.

        The X component will be set to zero.
        """
        inputs = y_component._area_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_y_Area(ctypes.byref(inputs), ctypes.byref(output))
        return AreaVector2d._new(output)

    @staticmethod
    def polar(magnitude: Area, angle: Angle) -> AreaVector2d:
        """Construct a vector from its magnitude (length) and angle."""
        inputs = _Tuple2_c_void_p_c_void_p(magnitude._area_ptr, angle._angle_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_polar_Area_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    @staticmethod
    def square_meters(x_component: float, y_component: float) -> AreaVector2d:
        """Construct a vector from its X and Y components given in square meters."""
        inputs = _Tuple2_c_double_c_double(x_component, y_component)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_squareMeters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    @cached_property
    def components(self) -> tuple[Area, Area]:
        """Get the X and Y components of a vector as a tuple."""
        inputs = self._areavector2d_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_AreaVector2d_components(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (Area._new(c_void_p(output.field0)), Area._new(c_void_p(output.field1)))

    @cached_property
    def x_component(self) -> Area:
        """Get the X component of a vector."""
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_xComponent(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    @cached_property
    def y_component(self) -> Area:
        """Get the Y component of a vector."""
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_yComponent(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    @cached_property
    def angle(self) -> Angle:
        """Get the angle of a vector.

        The angle is measured counterclockwise from the positive X axis, so:

          * A vector in the positive X direction has an angle of zero.
          * A vector in the positive Y direction has an angle of 90 degrees.
          * A vector in the negative Y direction has an angle of -90 degrees.
          * It is not defined whether a vector exactly in the negative X direction has
            an angle of -180 or +180 degrees. (Currently it is reported as having an
            angle of +180 degrees, but this should not be relied upon.)

        The returned angle will be between -180 and +180 degrees.
        """
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_angle(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def direction(self) -> Direction2d:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _area_tolerance()._area_ptr, self._areavector2d_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_AreaVector2d_direction(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Direction2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def normalize(self) -> Vector2d:
        """Normalize a vector.

        If the original vector is exactly zero, then the result will be zero as well.
        Otherwise, the result will be a unit vector.
        """
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_normalize(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)

    def angle_to(self, other: AreaVector2d) -> Angle:
        """Measure the signed angle from one vector to another.

        The angle will be measured counterclockwise from the first vector to the
        second, and will always be between -180 and +180 degrees.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            other._areavector2d_ptr, self._areavector2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector2d_angleTo_AreaVector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    def is_zero(self) -> bool:
        """Check if an area vector is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _area_tolerance()._area_ptr, self._areavector2d_ptr
        )
        output = c_int64()
        _lib.opensolid_AreaVector2d_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def place_on(self, plane: Plane3d) -> AreaVector3d:
        """Convert a 2D vector to 3D vector by placing it on a plane.

        Given a 2D vector defined within a plane's coordinate system,
        this returns the corresponding 3D vector.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._areavector2d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_placeOn_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def rotate_left(self) -> AreaVector2d:
        """Rotate a vector left (counterclockwise) by 90 degrees."""
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_rotateLeft(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def rotate_right(self) -> AreaVector2d:
        """Rotate a vector right (clockwise) by 90 degrees."""
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_rotateRight(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def rotate_by(self, angle: Angle) -> AreaVector2d:
        """Rotate a vector by a given angle.

        A positive angle corresponds to a counterclockwise rotation.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._areavector2d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_rotateBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def mirror_in(self, direction: Direction2d) -> AreaVector2d:
        """Mirror a vector in/along a given direction.

        For example, mirroring in the X direction
        will negate the vector's X component and leave its Y component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction2d_ptr, self._areavector2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector2d_mirrorIn_Direction2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def mirror_across(self, axis: Axis2d) -> AreaVector2d:
        """Mirror a vector across a given axis.

        The origin point of the axis is not used, only its direction, since vectors have no position.
        For example, mirroring a vector across *any* axis parallel to the X axis
        will negate the vector's Y component while leaving its X component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._areavector2d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def __neg__(self) -> AreaVector2d:
        """Return ``-self``."""
        inputs = self._areavector2d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector2d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return AreaVector2d._new(output)

    def __add__(self, rhs: AreaVector2d) -> AreaVector2d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._areavector2d_ptr, rhs._areavector2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector2d_add_AreaVector2d_AreaVector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def __sub__(self, rhs: AreaVector2d) -> AreaVector2d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._areavector2d_ptr, rhs._areavector2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector2d_sub_AreaVector2d_AreaVector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def __mul__(self, rhs: float) -> AreaVector2d:
        """Return ``self * rhs``."""
        inputs = _Tuple2_c_void_p_c_double(self._areavector2d_ptr, rhs)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_mul_AreaVector2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    @overload
    def __truediv__(self, rhs: float) -> AreaVector2d:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Displacement2d:
        pass

    @overload
    def __truediv__(self, rhs: Area) -> Vector2d:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._areavector2d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AreaVector2d_div_AreaVector2d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector2d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areavector2d_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaVector2d_div_AreaVector2d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areavector2d_ptr, rhs._area_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaVector2d_div_AreaVector2d_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector2d._new(output)
            case _:
                return NotImplemented

    def dot(self, rhs: Vector2d) -> Area:
        """Compute the dot product of two vector-like values."""
        inputs = _Tuple2_c_void_p_c_void_p(self._areavector2d_ptr, rhs._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_dot_AreaVector2d_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    def cross(self, rhs: Vector2d) -> Area:
        """Compute the cross product of two vector-like values."""
        inputs = _Tuple2_c_void_p_c_void_p(self._areavector2d_ptr, rhs._vector2d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_cross_AreaVector2d_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    def __rmul__(self, lhs: float) -> AreaVector2d:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._areavector2d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector2d_mul_Float_AreaVector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector2d._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        x, y = self.components
        return "AreaVector2d(" + repr(x) + "," + repr(y) + ")"


def _areavector2d_zero() -> AreaVector2d:
    output = c_void_p()
    _lib.opensolid_AreaVector2d_zero(c_void_p(), ctypes.byref(output))
    return AreaVector2d._new(output)


AreaVector2d.zero = _areavector2d_zero()


class UvVector:
    """A vector in UV parameter space."""

    _uvvector_ptr: c_void_p

    def __init__(self, u_component: float, v_component: float) -> None:
        """Construct a vector from its U and V components."""
        inputs = _Tuple2_c_double_c_double(u_component, v_component)
        self._uvvector_ptr = c_void_p()
        _lib.opensolid_UvVector_constructor_Float_Float(
            ctypes.byref(inputs), ctypes.byref(self._uvvector_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> UvVector:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvVector)
        obj._uvvector_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvvector_ptr)

    zero: UvVector = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def unit(direction: UvDirection) -> UvVector:
        """Construct a unit vector in the given direction."""
        inputs = direction._uvdirection_ptr
        output = c_void_p()
        _lib.opensolid_UvVector_unit_UvDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    @staticmethod
    def polar(magnitude: float, angle: Angle) -> UvVector:
        """Construct a vector from its magnitude (length) and angle."""
        inputs = _Tuple2_c_double_c_void_p(magnitude, angle._angle_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_polar_Float_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    @cached_property
    def components(self) -> tuple[float, float]:
        """Get the X and Y components of a vector as a tuple."""
        inputs = self._uvvector_ptr
        output = _Tuple2_c_double_c_double()
        _lib.opensolid_UvVector_components(ctypes.byref(inputs), ctypes.byref(output))
        return (output.field0, output.field1)

    @cached_property
    def u_component(self) -> float:
        """Get the U component of a vector."""
        inputs = self._uvvector_ptr
        output = c_double()
        _lib.opensolid_UvVector_uComponent(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def v_component(self) -> float:
        """Get the V component of a vector."""
        inputs = self._uvvector_ptr
        output = c_double()
        _lib.opensolid_UvVector_vComponent(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def angle(self) -> Angle:
        """Get the angle of a vector.

        The angle is measured counterclockwise from the positive X axis, so:

          * A vector in the positive X direction has an angle of zero.
          * A vector in the positive Y direction has an angle of 90 degrees.
          * A vector in the negative Y direction has an angle of -90 degrees.
          * It is not defined whether a vector exactly in the negative X direction has
            an angle of -180 or +180 degrees. (Currently it is reported as having an
            angle of +180 degrees, but this should not be relied upon.)

        The returned angle will be between -180 and +180 degrees.
        """
        inputs = self._uvvector_ptr
        output = c_void_p()
        _lib.opensolid_UvVector_angle(ctypes.byref(inputs), ctypes.byref(output))
        return Angle._new(output)

    def direction(self) -> UvDirection:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._uvvector_ptr)
        output = _Result_c_void_p()
        _lib.opensolid_UvVector_direction(ctypes.byref(inputs), ctypes.byref(output))
        return (
            UvDirection._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def normalize(self) -> UvVector:
        """Normalize a vector.

        If the original vector is exactly zero, then the result will be zero as well.
        Otherwise, the result will be a unit vector.
        """
        inputs = self._uvvector_ptr
        output = c_void_p()
        _lib.opensolid_UvVector_normalize(ctypes.byref(inputs), ctypes.byref(output))
        return UvVector._new(output)

    def angle_to(self, other: UvVector) -> Angle:
        """Measure the signed angle from one vector to another.

        The angle will be measured counterclockwise from the first vector to the
        second, and will always be between -180 and +180 degrees.
        """
        inputs = _Tuple2_c_void_p_c_void_p(other._uvvector_ptr, self._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_angleTo_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    def is_zero(self) -> bool:
        """Check if a vector is zero, within the current tolerance."""
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._uvvector_ptr)
        output = c_int64()
        _lib.opensolid_UvVector_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def rotate_left(self) -> UvVector:
        """Rotate a vector left (counterclockwise) by 90 degrees."""
        inputs = self._uvvector_ptr
        output = c_void_p()
        _lib.opensolid_UvVector_rotateLeft(ctypes.byref(inputs), ctypes.byref(output))
        return UvVector._new(output)

    def rotate_right(self) -> UvVector:
        """Rotate a vector right (clockwise) by 90 degrees."""
        inputs = self._uvvector_ptr
        output = c_void_p()
        _lib.opensolid_UvVector_rotateRight(ctypes.byref(inputs), ctypes.byref(output))
        return UvVector._new(output)

    def rotate_by(self, angle: Angle) -> UvVector:
        """Rotate a vector by a given angle.

        A positive angle corresponds to a counterclockwise rotation.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_rotateBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def mirror_in(self, direction: UvDirection) -> UvVector:
        """Mirror a vector in/along a given direction.

        For example, mirroring in the X direction
        will negate the vector's X component and leave its Y component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._uvdirection_ptr, self._uvvector_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvVector_mirrorIn_UvDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def mirror_across(self, axis: UvAxis) -> UvVector:
        """Mirror a vector across a given axis.

        The origin point of the axis is not used, only its direction, since vectors have no position.
        For example, mirroring a vector across *any* axis parallel to the X axis
        will negate the vector's Y component while leaving its X component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(axis._uvaxis_ptr, self._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_mirrorAcross_UvAxis(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def __neg__(self) -> UvVector:
        """Return ``-self``."""
        inputs = self._uvvector_ptr
        output = c_void_p()
        _lib.opensolid_UvVector_neg(ctypes.byref(inputs), ctypes.byref(output))
        return UvVector._new(output)

    def __add__(self, rhs: UvVector) -> UvVector:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvvector_ptr, rhs._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_add_UvVector_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def __sub__(self, rhs: UvVector) -> UvVector:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvvector_ptr, rhs._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_sub_UvVector_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def __mul__(self, rhs: float) -> UvVector:
        """Return ``self * rhs``."""
        inputs = _Tuple2_c_void_p_c_double(self._uvvector_ptr, rhs)
        output = c_void_p()
        _lib.opensolid_UvVector_mul_UvVector_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def __truediv__(self, rhs: float) -> UvVector:
        """Return ``self / rhs``."""
        inputs = _Tuple2_c_void_p_c_double(self._uvvector_ptr, rhs)
        output = c_void_p()
        _lib.opensolid_UvVector_div_UvVector_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)

    def dot(self, rhs: UvVector) -> float:
        """Compute the dot product of two vector-like values."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvvector_ptr, rhs._uvvector_ptr)
        output = c_double()
        _lib.opensolid_UvVector_dot_UvVector_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return output.value

    def cross(self, rhs: UvVector) -> float:
        """Compute the cross product of two vector-like values."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvvector_ptr, rhs._uvvector_ptr)
        output = c_double()
        _lib.opensolid_UvVector_cross_UvVector_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return output.value

    def __rmul__(self, lhs: float) -> UvVector:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvVector_mul_Float_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)


def _uvvector_zero() -> UvVector:
    output = c_void_p()
    _lib.opensolid_UvVector_zero(c_void_p(), ctypes.byref(output))
    return UvVector._new(output)


UvVector.zero = _uvvector_zero()


class Direction2d(Vector2d):
    """A direction in 2D.

    This is effectively a type-safe unit vector.
    """

    _direction2d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Direction2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Direction2d)
        obj._direction2d_ptr = ptr
        obj._vector2d_ptr = c_void_p()
        _lib.opensolid_Direction2d_upcast(
            ctypes.byref(obj._direction2d_ptr), ctypes.byref(obj._vector2d_ptr)
        )
        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._direction2d_ptr)
        super().__del__()

    x: Direction2d = None  # type: ignore[assignment]
    """The X direction."""

    y: Direction2d = None  # type: ignore[assignment]
    """The Y direction."""

    @staticmethod
    def from_angle(angle: Angle) -> Direction2d:
        """Construct a direction from an angle.

        The angle is measured counterclockwise from the positive X direction, so:

          * An angle of zero corresponds to the positive X direction
          * An angle of 90 degrees corresponds to the positive Y direction
          * An angle of 180 degrees (or -180 degrees) corresponds to the negative X direction
        """
        inputs = angle._angle_ptr
        output = c_void_p()
        _lib.opensolid_Direction2d_fromAngle_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    @staticmethod
    def degrees(value: float) -> Direction2d:
        """Construct a direction from an angle given in degrees.

        See 'fromAngle' for details.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Direction2d_degrees_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    @staticmethod
    def radians(value: float) -> Direction2d:
        """Construct a direction from an angle given in radians.

        See 'fromAngle' for details.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Direction2d_radians_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    def rotate_left(self) -> Direction2d:
        """Rotate a direction left (counterclockwise) by 90 degrees."""
        inputs = self._direction2d_ptr
        output = c_void_p()
        _lib.opensolid_Direction2d_rotateLeft(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    def rotate_right(self) -> Direction2d:
        """Rotate a direction right (clockwise) by 90 degrees."""
        inputs = self._direction2d_ptr
        output = c_void_p()
        _lib.opensolid_Direction2d_rotateRight(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    def rotate_by(self, angle: Angle) -> Direction2d:
        """Rotate a direction by a given angle.

        A positive angle corresponds to a counterclockwise rotation.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._direction2d_ptr)
        output = c_void_p()
        _lib.opensolid_Direction2d_rotateBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    def mirror_in(self, direction: Direction2d) -> Direction2d:
        """Mirror a direction in/along a given other direction.

        For example, mirroring in the X direction
        will negate the original direction's X component and leave its Y component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction2d_ptr, self._direction2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Direction2d_mirrorIn_Direction2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Direction2d:
        """Mirror a direction across a given axis.

        The origin point of the axis is not used, only its direction, since directions have no position.
        For example, mirroring a direction across *any* axis parallel to the X axis
        will negate the direction's Y component while leaving its X component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._direction2d_ptr)
        output = c_void_p()
        _lib.opensolid_Direction2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction2d._new(output)

    def place_on(self, plane: Plane3d) -> Direction3d:
        """Convert a 2D direction to 3D direction by placing it on a plane.

        Given a 2D direction defined within a plane's coordinate system,
        this returns the corresponding 3D direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._direction2d_ptr)
        output = c_void_p()
        _lib.opensolid_Direction2d_placeOn_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def __neg__(self) -> Direction2d:
        """Return ``-self``."""
        inputs = self._direction2d_ptr
        output = c_void_p()
        _lib.opensolid_Direction2d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Direction2d._new(output)


def _direction2d_x() -> Direction2d:
    output = c_void_p()
    _lib.opensolid_Direction2d_x(c_void_p(), ctypes.byref(output))
    return Direction2d._new(output)


Direction2d.x = _direction2d_x()


def _direction2d_y() -> Direction2d:
    output = c_void_p()
    _lib.opensolid_Direction2d_y(c_void_p(), ctypes.byref(output))
    return Direction2d._new(output)


Direction2d.y = _direction2d_y()


class UvDirection(UvVector):
    """A direction in UV parameter space."""

    _uvdirection_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> UvDirection:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvDirection)
        obj._uvdirection_ptr = ptr
        obj._uvvector_ptr = c_void_p()
        _lib.opensolid_UvDirection_upcast(
            ctypes.byref(obj._uvdirection_ptr), ctypes.byref(obj._uvvector_ptr)
        )
        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvdirection_ptr)
        super().__del__()

    u: UvDirection = None  # type: ignore[assignment]
    """The U direction."""

    v: UvDirection = None  # type: ignore[assignment]
    """The V direction."""

    @staticmethod
    def from_angle(angle: Angle) -> UvDirection:
        """Construct a direction from an angle.

        The angle is measured counterclockwise from the positive X direction, so:

          * An angle of zero corresponds to the positive X direction
          * An angle of 90 degrees corresponds to the positive Y direction
          * An angle of 180 degrees (or -180 degrees) corresponds to the negative X direction
        """
        inputs = angle._angle_ptr
        output = c_void_p()
        _lib.opensolid_UvDirection_fromAngle_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    @staticmethod
    def degrees(value: float) -> UvDirection:
        """Construct a direction from an angle given in degrees.

        See 'fromAngle' for details.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_UvDirection_degrees_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    @staticmethod
    def radians(value: float) -> UvDirection:
        """Construct a direction from an angle given in radians.

        See 'fromAngle' for details.
        """
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_UvDirection_radians_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    def rotate_left(self) -> UvDirection:
        """Rotate a direction left (counterclockwise) by 90 degrees."""
        inputs = self._uvdirection_ptr
        output = c_void_p()
        _lib.opensolid_UvDirection_rotateLeft(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    def rotate_right(self) -> UvDirection:
        """Rotate a direction right (clockwise) by 90 degrees."""
        inputs = self._uvdirection_ptr
        output = c_void_p()
        _lib.opensolid_UvDirection_rotateRight(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    def rotate_by(self, angle: Angle) -> UvDirection:
        """Rotate a direction by a given angle.

        A positive angle corresponds to a counterclockwise rotation.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._uvdirection_ptr)
        output = c_void_p()
        _lib.opensolid_UvDirection_rotateBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    def mirror_in(self, direction: UvDirection) -> UvDirection:
        """Mirror a direction in/along a given other direction.

        For example, mirroring in the X direction
        will negate the original direction's X component and leave its Y component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._uvdirection_ptr, self._uvdirection_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvDirection_mirrorIn_UvDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    def mirror_across(self, axis: UvAxis) -> UvDirection:
        """Mirror a direction across a given axis.

        The origin point of the axis is not used, only its direction, since directions have no position.
        For example, mirroring a direction across *any* axis parallel to the X axis
        will negate the direction's Y component while leaving its X component unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(axis._uvaxis_ptr, self._uvdirection_ptr)
        output = c_void_p()
        _lib.opensolid_UvDirection_mirrorAcross_UvAxis(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvDirection._new(output)

    def __neg__(self) -> UvDirection:
        """Return ``-self``."""
        inputs = self._uvdirection_ptr
        output = c_void_p()
        _lib.opensolid_UvDirection_neg(ctypes.byref(inputs), ctypes.byref(output))
        return UvDirection._new(output)


def _uvdirection_u() -> UvDirection:
    output = c_void_p()
    _lib.opensolid_UvDirection_u(c_void_p(), ctypes.byref(output))
    return UvDirection._new(output)


UvDirection.u = _uvdirection_u()


def _uvdirection_v() -> UvDirection:
    output = c_void_p()
    _lib.opensolid_UvDirection_v(c_void_p(), ctypes.byref(output))
    return UvDirection._new(output)


UvDirection.v = _uvdirection_v()


class Point2d:
    """A point in 2D, defined by its X and Y coordinates."""

    _point2d_ptr: c_void_p

    def __init__(self, x_coordinate: Length, y_coordinate: Length) -> None:
        """Construct a point from its X and Y coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(
            x_coordinate._length_ptr, y_coordinate._length_ptr
        )
        self._point2d_ptr = c_void_p()
        _lib.opensolid_Point2d_constructor_Length_Length(
            ctypes.byref(inputs), ctypes.byref(self._point2d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Point2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Point2d)
        obj._point2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._point2d_ptr)

    origin: Point2d = None  # type: ignore[assignment]
    """The point with coordinates (0,0)."""

    @staticmethod
    def x(x_coordinate: Length) -> Point2d:
        """Construct a point along the X axis, with the given X coordinate."""
        inputs = x_coordinate._length_ptr
        output = c_void_p()
        _lib.opensolid_Point2d_x_Length(ctypes.byref(inputs), ctypes.byref(output))
        return Point2d._new(output)

    @staticmethod
    def y(y_coordinate: Length) -> Point2d:
        """Construct a point along the Y axis, with the given Y coordinate."""
        inputs = y_coordinate._length_ptr
        output = c_void_p()
        _lib.opensolid_Point2d_y_Length(ctypes.byref(inputs), ctypes.byref(output))
        return Point2d._new(output)

    @staticmethod
    def polar(radius: Length, angle: Angle) -> Point2d:
        """Construct a point from polar coordinates (radius and angle).

        The angle is measured counterclockwise from the positive X axis.
        """
        inputs = _Tuple2_c_void_p_c_void_p(radius._length_ptr, angle._angle_ptr)
        output = c_void_p()
        _lib.opensolid_Point2d_polar_Length_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @staticmethod
    def meters(x_coordinate: float, y_coordinate: float) -> Point2d:
        """Construct a point from its X and Y coordinates given in meters."""
        inputs = _Tuple2_c_double_c_double(x_coordinate, y_coordinate)
        output = c_void_p()
        _lib.opensolid_Point2d_meters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @staticmethod
    def centimeters(x_coordinate: float, y_coordinate: float) -> Point2d:
        """Construct a point from its X and Y coordinates given in centimeters."""
        inputs = _Tuple2_c_double_c_double(x_coordinate, y_coordinate)
        output = c_void_p()
        _lib.opensolid_Point2d_centimeters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @staticmethod
    def cm(x_coordinate: float, y_coordinate: float) -> Point2d:
        """Construct a point from its X and Y coordinates given in centimeters.

        Short form alias for 'centimeters'.
        """
        inputs = _Tuple2_c_double_c_double(x_coordinate, y_coordinate)
        output = c_void_p()
        _lib.opensolid_Point2d_cm_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @staticmethod
    def millimeters(x_coordinate: float, y_coordinate: float) -> Point2d:
        """Construct a point from its X and Y coordinates given in millimeters."""
        inputs = _Tuple2_c_double_c_double(x_coordinate, y_coordinate)
        output = c_void_p()
        _lib.opensolid_Point2d_millimeters_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @staticmethod
    def mm(x_coordinate: float, y_coordinate: float) -> Point2d:
        """Construct a point from its X and Y coordinates given in millimeters.

        Short form alias for 'millimeters'.
        """
        inputs = _Tuple2_c_double_c_double(x_coordinate, y_coordinate)
        output = c_void_p()
        _lib.opensolid_Point2d_mm_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @staticmethod
    def inches(x_coordinate: float, y_coordinate: float) -> Point2d:
        """Construct a point from its X and Y coordinates given in inches."""
        inputs = _Tuple2_c_double_c_double(x_coordinate, y_coordinate)
        output = c_void_p()
        _lib.opensolid_Point2d_inches_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @cached_property
    def coordinates(self) -> tuple[Length, Length]:
        """Get the X and Y coordinates of a point."""
        inputs = self._point2d_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_Point2d_coordinates(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
        )

    @cached_property
    def x_coordinate(self) -> Length:
        """Get the X coordinate of a point."""
        inputs = self._point2d_ptr
        output = c_void_p()
        _lib.opensolid_Point2d_xCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @cached_property
    def y_coordinate(self) -> Length:
        """Get the Y coordinate of a point."""
        inputs = self._point2d_ptr
        output = c_void_p()
        _lib.opensolid_Point2d_yCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    def distance_to(self, other: Point2d) -> Length:
        """Compute the distance from one point to another."""
        inputs = _Tuple2_c_void_p_c_void_p(other._point2d_ptr, self._point2d_ptr)
        output = c_void_p()
        _lib.opensolid_Point2d_distanceTo_Point2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    def midpoint(self, other: Point2d) -> Point2d:
        """Find the midpoint between two points."""
        inputs = _Tuple2_c_void_p_c_void_p(other._point2d_ptr, self._point2d_ptr)
        output = c_void_p()
        _lib.opensolid_Point2d_midpoint_Point2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def place_on(self, plane: Plane3d) -> Point3d:
        """Convert a 2D point to 3D point by placing it on a plane.

        Given a 2D point defined within a plane's coordinate system,
        this returns the corresponding 3D point.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._point2d_ptr)
        output = c_void_p()
        _lib.opensolid_Point2d_placeOn_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def scale_along(self, axis: Axis2d, scale: float) -> Point2d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis2d_ptr, scale, self._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point2d_scaleAlong_Axis2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def scale_about(self, point: Point2d, scale: float) -> Point2d:
        """Scale uniformly about the given point by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            point._point2d_ptr, scale, self._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point2d_scaleAbout_Point2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Point2d:
        """Mirror across the given axis."""
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._point2d_ptr)
        output = c_void_p()
        _lib.opensolid_Point2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def translate_by(self, displacement: Displacement2d) -> Point2d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement2d_ptr, self._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point2d_translateBy_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def translate_in(self, direction: Direction2d, distance: Length) -> Point2d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction2d_ptr, distance._length_ptr, self._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point2d_translateIn_Direction2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def translate_along(self, axis: Axis2d, distance: Length) -> Point2d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis2d_ptr, distance._length_ptr, self._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point2d_translateAlong_Axis2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def rotate_around(self, point: Point2d, angle: Angle) -> Point2d:
        """Rotate around the given point by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            point._point2d_ptr, angle._angle_ptr, self._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point2d_rotateAround_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    @overload
    def __sub__(self, rhs: Point2d) -> Displacement2d:
        pass

    @overload
    def __sub__(self, rhs: Displacement2d) -> Point2d:
        pass

    @overload
    def __sub__(self, rhs: Curve2d) -> DisplacementCurve2d:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case Point2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._point2d_ptr, rhs._point2d_ptr)
                output = c_void_p()
                _lib.opensolid_Point2d_sub_Point2d_Point2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement2d._new(output)
            case Displacement2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._point2d_ptr, rhs._displacement2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Point2d_sub_Point2d_Displacement2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Point2d._new(output)
            case Curve2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._point2d_ptr, rhs._curve2d_ptr)
                output = c_void_p()
                _lib.opensolid_Point2d_sub_Point2d_Curve2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return DisplacementCurve2d._new(output)
            case _:
                return NotImplemented

    def __add__(self, rhs: Displacement2d) -> Point2d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._point2d_ptr, rhs._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Point2d_add_Point2d_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        x, y = self.coordinates
        return "Point2d(" + repr(x) + "," + repr(y) + ")"


def _point2d_origin() -> Point2d:
    output = c_void_p()
    _lib.opensolid_Point2d_origin(c_void_p(), ctypes.byref(output))
    return Point2d._new(output)


Point2d.origin = _point2d_origin()


class UvPoint:
    """A point in UV parameter space."""

    _uvpoint_ptr: c_void_p

    def __init__(self, u_coordinate: float, v_coordinate: float) -> None:
        """Construct a point from its U and V coordinates."""
        inputs = _Tuple2_c_double_c_double(u_coordinate, v_coordinate)
        self._uvpoint_ptr = c_void_p()
        _lib.opensolid_UvPoint_constructor_Float_Float(
            ctypes.byref(inputs), ctypes.byref(self._uvpoint_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> UvPoint:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvPoint)
        obj._uvpoint_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvpoint_ptr)

    origin: UvPoint = None  # type: ignore[assignment]
    """The point with coordinates (0,0)."""

    @cached_property
    def coordinates(self) -> tuple[float, float]:
        """Get the U and V coordinates of a point."""
        inputs = self._uvpoint_ptr
        output = _Tuple2_c_double_c_double()
        _lib.opensolid_UvPoint_coordinates(ctypes.byref(inputs), ctypes.byref(output))
        return (output.field0, output.field1)

    @cached_property
    def u_coordinate(self) -> float:
        """Get the U coordinate of a point."""
        inputs = self._uvpoint_ptr
        output = c_double()
        _lib.opensolid_UvPoint_uCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def v_coordinate(self) -> float:
        """Get the V coordinate of a point."""
        inputs = self._uvpoint_ptr
        output = c_double()
        _lib.opensolid_UvPoint_vCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def distance_to(self, other: UvPoint) -> float:
        """Compute the distance from one point to another."""
        inputs = _Tuple2_c_void_p_c_void_p(other._uvpoint_ptr, self._uvpoint_ptr)
        output = c_double()
        _lib.opensolid_UvPoint_distanceTo_UvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return output.value

    def midpoint(self, other: UvPoint) -> UvPoint:
        """Find the midpoint between two points."""
        inputs = _Tuple2_c_void_p_c_void_p(other._uvpoint_ptr, self._uvpoint_ptr)
        output = c_void_p()
        _lib.opensolid_UvPoint_midpoint_UvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvPoint._new(output)

    @overload
    def __sub__(self, rhs: UvPoint) -> UvVector:
        pass

    @overload
    def __sub__(self, rhs: UvVector) -> UvPoint:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case UvPoint():
                inputs = _Tuple2_c_void_p_c_void_p(self._uvpoint_ptr, rhs._uvpoint_ptr)
                output = c_void_p()
                _lib.opensolid_UvPoint_sub_UvPoint_UvPoint(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return UvVector._new(output)
            case UvVector():
                inputs = _Tuple2_c_void_p_c_void_p(self._uvpoint_ptr, rhs._uvvector_ptr)
                output = c_void_p()
                _lib.opensolid_UvPoint_sub_UvPoint_UvVector(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return UvPoint._new(output)
            case _:
                return NotImplemented

    def __add__(self, rhs: UvVector) -> UvPoint:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvpoint_ptr, rhs._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvPoint_add_UvPoint_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvPoint._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        x, y = self.coordinates
        return "UvPoint(" + str(x) + "," + str(y) + ")"


def _uvpoint_origin() -> UvPoint:
    output = c_void_p()
    _lib.opensolid_UvPoint_origin(c_void_p(), ctypes.byref(output))
    return UvPoint._new(output)


UvPoint.origin = _uvpoint_origin()


class Bounds2d:
    """A bounding box in 2D."""

    _bounds2d_ptr: c_void_p

    def __init__(self, x_coordinate: LengthBounds, y_coordinate: LengthBounds) -> None:
        """Construct a bounding box from its X and Y coordinate bounds."""
        inputs = _Tuple2_c_void_p_c_void_p(
            x_coordinate._lengthbounds_ptr, y_coordinate._lengthbounds_ptr
        )
        self._bounds2d_ptr = c_void_p()
        _lib.opensolid_Bounds2d_constructor_LengthBounds_LengthBounds(
            ctypes.byref(inputs), ctypes.byref(self._bounds2d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Bounds2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Bounds2d)
        obj._bounds2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._bounds2d_ptr)

    @staticmethod
    def constant(point: Point2d) -> Bounds2d:
        """Construct a zero-size bounding box containing a single point."""
        inputs = point._point2d_ptr
        output = c_void_p()
        _lib.opensolid_Bounds2d_constant_Point2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    @staticmethod
    def from_corners(first_point: Point2d, second_point: Point2d) -> Bounds2d:
        """Construct a bounding box from two corner points."""
        inputs = _Tuple2_c_void_p_c_void_p(
            first_point._point2d_ptr, second_point._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_fromCorners_Point2d_Point2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    @staticmethod
    def hull(points: list[Point2d]) -> Bounds2d:
        """Construct a bounding box containing all vertices in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(points))(*[item._point2d_ptr for item in points]),
            )
            if points
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_hull_NonEmptyPoint2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    @staticmethod
    def aggregate(bounds: list[Bounds2d]) -> Bounds2d:
        """Construct a bounding box containing all bounding boxes in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._bounds2d_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_aggregate_NonEmptyBounds2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    @cached_property
    def coordinates(self) -> tuple[LengthBounds, LengthBounds]:
        """Get the X and Y coordinate bounds of a bounding box."""
        inputs = self._bounds2d_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_Bounds2d_coordinates(ctypes.byref(inputs), ctypes.byref(output))
        return (
            LengthBounds._new(c_void_p(output.field0)),
            LengthBounds._new(c_void_p(output.field1)),
        )

    @cached_property
    def x_coordinate(self) -> LengthBounds:
        """Get the X coordinate bounds of a bounding box."""
        inputs = self._bounds2d_ptr
        output = c_void_p()
        _lib.opensolid_Bounds2d_xCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return LengthBounds._new(output)

    @cached_property
    def y_coordinate(self) -> LengthBounds:
        """Get the Y coordinate bounds of a bounding box."""
        inputs = self._bounds2d_ptr
        output = c_void_p()
        _lib.opensolid_Bounds2d_yCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return LengthBounds._new(output)

    def scale_along(self, axis: Axis2d, scale: float) -> Bounds2d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis2d_ptr, scale, self._bounds2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_scaleAlong_Axis2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def scale_about(self, point: Point2d, scale: float) -> Bounds2d:
        """Scale uniformly about the given point by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            point._point2d_ptr, scale, self._bounds2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_scaleAbout_Point2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Bounds2d:
        """Mirror across the given axis."""
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._bounds2d_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def translate_by(self, displacement: Displacement2d) -> Bounds2d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement2d_ptr, self._bounds2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_translateBy_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def translate_in(self, direction: Direction2d, distance: Length) -> Bounds2d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction2d_ptr, distance._length_ptr, self._bounds2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_translateIn_Direction2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def translate_along(self, axis: Axis2d, distance: Length) -> Bounds2d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis2d_ptr, distance._length_ptr, self._bounds2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_translateAlong_Axis2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def rotate_around(self, point: Point2d, angle: Angle) -> Bounds2d:
        """Rotate around the given point by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            point._point2d_ptr, angle._angle_ptr, self._bounds2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds2d_rotateAround_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def __add__(self, rhs: Displacement2d) -> Bounds2d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._bounds2d_ptr, rhs._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds2d_add_Bounds2d_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def __sub__(self, rhs: Displacement2d) -> Bounds2d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._bounds2d_ptr, rhs._displacement2d_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds2d_sub_Bounds2d_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds2d._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        x, y = self.coordinates
        return "Bounds2d(" + repr(x) + "," + repr(y) + ")"


class UvBounds:
    """A bounding box in UV parameter space."""

    _uvbounds_ptr: c_void_p

    def __init__(self, u_coordinate: Bounds, v_coordinate: Bounds) -> None:
        """Construct a bounding box from its U and V coordinate bounds."""
        inputs = _Tuple2_c_void_p_c_void_p(
            u_coordinate._bounds_ptr, v_coordinate._bounds_ptr
        )
        self._uvbounds_ptr = c_void_p()
        _lib.opensolid_UvBounds_constructor_Bounds_Bounds(
            ctypes.byref(inputs), ctypes.byref(self._uvbounds_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> UvBounds:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvBounds)
        obj._uvbounds_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvbounds_ptr)

    @staticmethod
    def constant(point: UvPoint) -> UvBounds:
        """Construct a zero-size bounding box containing a single point."""
        inputs = point._uvpoint_ptr
        output = c_void_p()
        _lib.opensolid_UvBounds_constant_UvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvBounds._new(output)

    @staticmethod
    def from_corners(first_point: UvPoint, second_point: UvPoint) -> UvBounds:
        """Construct a bounding box from two corner points."""
        inputs = _Tuple2_c_void_p_c_void_p(
            first_point._uvpoint_ptr, second_point._uvpoint_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvBounds_fromCorners_UvPoint_UvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvBounds._new(output)

    @staticmethod
    def hull(points: list[UvPoint]) -> UvBounds:
        """Construct a bounding box containing all vertices in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(points))(*[item._uvpoint_ptr for item in points]),
            )
            if points
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_UvBounds_hull_NonEmptyUvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvBounds._new(output)

    @staticmethod
    def aggregate(bounds: list[UvBounds]) -> UvBounds:
        """Construct a bounding box containing all bounding boxes in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._uvbounds_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_UvBounds_aggregate_NonEmptyUvBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvBounds._new(output)

    @cached_property
    def coordinates(self) -> tuple[Bounds, Bounds]:
        """Get the X and Y coordinate bounds of a bounding box."""
        inputs = self._uvbounds_ptr
        output = _Tuple2_c_void_p_c_void_p()
        _lib.opensolid_UvBounds_coordinates(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Bounds._new(c_void_p(output.field0)),
            Bounds._new(c_void_p(output.field1)),
        )

    @cached_property
    def u_coordinate(self) -> Bounds:
        """Get the U coordinate bounds of a bounding box."""
        inputs = self._uvbounds_ptr
        output = c_void_p()
        _lib.opensolid_UvBounds_uCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return Bounds._new(output)

    @cached_property
    def v_coordinate(self) -> Bounds:
        """Get the V coordinate bounds of a bounding box."""
        inputs = self._uvbounds_ptr
        output = c_void_p()
        _lib.opensolid_UvBounds_vCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return Bounds._new(output)

    def __add__(self, rhs: UvVector) -> UvBounds:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvbounds_ptr, rhs._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvBounds_add_UvBounds_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvBounds._new(output)

    def __sub__(self, rhs: UvVector) -> UvBounds:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvbounds_ptr, rhs._uvvector_ptr)
        output = c_void_p()
        _lib.opensolid_UvBounds_sub_UvBounds_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvBounds._new(output)

    def __repr__(self) -> str:
        """Return a human-readable representation of this value."""
        u, v = self.coordinates
        return "UvBounds(" + repr(u) + "," + repr(v) + ")"


class Curve:
    """A parametric curve definining a unitless value in terms of a parameter value."""

    _curve_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Curve:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Curve)
        obj._curve_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._curve_ptr)

    zero: Curve = None  # type: ignore[assignment]
    """A curve equal to zero everywhere."""

    t: Curve = None  # type: ignore[assignment]
    """A curve parameter.

    In other words, a curve whose value is equal to its input parameter.
    When defining parametric curves, you will typically start with 'Curve.t'
    and then use arithmetic operators etc. to build up more complex curves.
    """

    @staticmethod
    def constant(value: float) -> Curve:
        """Create a curve with the given constant value."""
        inputs = c_double(value)
        output = c_void_p()
        _lib.opensolid_Curve_constant_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    @staticmethod
    def line(start: float, end: float) -> Curve:
        """Create a curve that linearly interpolates from the first value to the second."""
        inputs = _Tuple2_c_double_c_double(start, end)
        output = c_void_p()
        _lib.opensolid_Curve_line_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve._new(output)

    def squared(self) -> Curve:
        """Compute the square of a curve."""
        inputs = self._curve_ptr
        output = c_void_p()
        _lib.opensolid_Curve_squared(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def sqrt(self) -> Curve:
        """Compute the square root of a curve."""
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._curve_ptr)
        output = c_void_p()
        _lib.opensolid_Curve_sqrt(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def evaluate(self, parameter_value: float) -> float:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._curve_ptr)
        output = c_double()
        _lib.opensolid_Curve_evaluate_Float(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    def zeros(self) -> list[Curve.Zero]:
        """Find all points at which the given curve is zero.

        This includes not only points where the curve *crosses* zero,
        but also where it is *tangent* to zero.
        For example, y=x-3 crosses zero at x=3,
        while y=(x-3)^2 is tangent to zero at x=3.

        We define y=x-3 as having a zero of order 0 at x=3,
        since only the "derivative of order zero" (the curve itself)
        is zero at that point.
        Similarly, y=(x-3)^2 has a zero of order 1 at x=3,
        since the first derivative (but not the second derivative)
        is zero at that point.

        Currently, this function up to third-order zeros
        (e.g. y=x^4 has a third-order zero at x=0,
        since everything up to the third derivative is zero at x=0).

        The current tolerance is used to determine
        whether a given point should be considered a zero,
        and of what order.
        For example, the curve y=x^2-0.0001 is *exactly* zero at x=0.01 and x=-0.01.
        However, note that the curve is also very close to zero at x=0,
        and at that point the first derivative is *also* zero.
        In many cases, it is reasonable to assume that
        the 0.0001 is an artifact of numerical roundoff,
        and the curve actually has a single zero of order 1 at x=0.
        The current tolerance is used to choose which case to report.
        In this example, a tolerance of 0.000001
        would mean that we consider 0.0001 a meaningful value (not just roundoff),
        so we would end up reporting two order-0 zeros at x=0.01 and x=-0.01.
        On the other hand, a tolerance of 0.01 would mean that
        we consider 0.0001 as just roundoff error,
        so we would end up reporting a single order-1 zero at x=0
        (the point at which the *first derivative* is zero).
        """
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._curve_ptr)
        output = _Result_List_c_void_p()
        _lib.opensolid_Curve_zeros(ctypes.byref(inputs), ctypes.byref(output))
        return (
            [
                Curve.Zero._new(c_void_p(item))
                for item in [
                    output.field2.field1[index] for index in range(output.field2.field0)
                ]
            ]
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if a curve is zero everywhere, within the current tolerance."""
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._curve_ptr)
        output = c_int64()
        _lib.opensolid_Curve_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __neg__(self) -> Curve:
        """Return ``-self``."""
        inputs = self._curve_ptr
        output = c_void_p()
        _lib.opensolid_Curve_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    @overload
    def __add__(self, rhs: float) -> Curve:
        pass

    @overload
    def __add__(self, rhs: Curve) -> Curve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._curve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Curve_add_Curve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_add_Curve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: float) -> Curve:
        pass

    @overload
    def __sub__(self, rhs: Curve) -> Curve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._curve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Curve_sub_Curve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_sub_Curve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> Curve:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> Curve:
        pass

    @overload
    def __mul__(self, rhs: Length) -> LengthCurve:
        pass

    @overload
    def __mul__(self, rhs: Area) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: Angle) -> AngleCurve:
        pass

    @overload
    def __mul__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    @overload
    def __mul__(self, rhs: AreaCurve) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: AngleCurve) -> AngleCurve:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._curve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._curve_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case AreaCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._areacurve_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case AngleCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve_ptr, rhs._anglecurve_ptr)
                output = c_void_p()
                _lib.opensolid_Curve_mul_Curve_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> Curve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._curve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Curve_div_Curve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._curve_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_Curve_div_Curve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __radd__(self, lhs: float) -> Curve:
        """Return ``lhs <> self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._curve_ptr)
        output = c_void_p()
        _lib.opensolid_Curve_add_Float_Curve(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def __rsub__(self, lhs: float) -> Curve:
        """Return ``lhs - self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._curve_ptr)
        output = c_void_p()
        _lib.opensolid_Curve_sub_Float_Curve(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def __rmul__(self, lhs: float) -> Curve:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._curve_ptr)
        output = c_void_p()
        _lib.opensolid_Curve_mul_Float_Curve(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def __rtruediv__(self, lhs: float) -> Curve:
        """Return ``lhs / self``."""
        inputs = _Tuple3_c_double_c_double_c_void_p(
            _float_tolerance(), lhs, self._curve_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_Curve_div_Float_Curve(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Curve._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    class Zero:
        """A point where a given curve is equal to zero."""

        _zero_ptr: c_void_p

        @staticmethod
        def _new(ptr: c_void_p) -> Curve.Zero:
            """Construct directly from an underlying C pointer."""
            obj = object.__new__(Curve.Zero)
            obj._zero_ptr = ptr

            return obj

        def __del__(self) -> None:
            """Free the underlying Haskell value."""
            _lib.opensolid_release(self._zero_ptr)

        @cached_property
        def location(self) -> float:
            """The parameter value at which the curve is zero."""
            inputs = self._zero_ptr
            output = c_double()
            _lib.opensolid_CurveZero_location(
                ctypes.byref(inputs), ctypes.byref(output)
            )
            return output.value

        @cached_property
        def order(self) -> int:
            """The order of the solution: 0 for crossing, 1 for tangent, etc."""
            inputs = self._zero_ptr
            output = c_int64()
            _lib.opensolid_CurveZero_order(ctypes.byref(inputs), ctypes.byref(output))
            return output.value

        @cached_property
        def sign(self) -> int:
            """The sign of the solution: the sign of the curve to the right of the solution."""
            inputs = self._zero_ptr
            output = c_int64()
            _lib.opensolid_CurveZero_sign(ctypes.byref(inputs), ctypes.byref(output))
            return output.value


def _curve_zero() -> Curve:
    output = c_void_p()
    _lib.opensolid_Curve_zero(c_void_p(), ctypes.byref(output))
    return Curve._new(output)


Curve.zero = _curve_zero()


def _curve_t() -> Curve:
    output = c_void_p()
    _lib.opensolid_Curve_t(c_void_p(), ctypes.byref(output))
    return Curve._new(output)


Curve.t = _curve_t()


class LengthCurve:
    """A parametric curve definining a length in terms of a parameter value."""

    _lengthcurve_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> LengthCurve:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(LengthCurve)
        obj._lengthcurve_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._lengthcurve_ptr)

    zero: LengthCurve = None  # type: ignore[assignment]
    """A curve equal to zero everywhere."""

    @staticmethod
    def constant(value: Length) -> LengthCurve:
        """Create a curve with the given constant value."""
        inputs = value._length_ptr
        output = c_void_p()
        _lib.opensolid_LengthCurve_constant_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthCurve._new(output)

    @staticmethod
    def line(start: Length, end: Length) -> LengthCurve:
        """Create a curve that linearly interpolates from the first value to the second."""
        inputs = _Tuple2_c_void_p_c_void_p(start._length_ptr, end._length_ptr)
        output = c_void_p()
        _lib.opensolid_LengthCurve_line_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthCurve._new(output)

    def squared(self) -> AreaCurve:
        """Compute the square of a curve."""
        inputs = self._lengthcurve_ptr
        output = c_void_p()
        _lib.opensolid_LengthCurve_squared(ctypes.byref(inputs), ctypes.byref(output))
        return AreaCurve._new(output)

    def evaluate(self, parameter_value: float) -> Length:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._lengthcurve_ptr)
        output = c_void_p()
        _lib.opensolid_LengthCurve_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    def zeros(self) -> list[Curve.Zero]:
        """Find all points at which the given curve is zero.

        This includes not only points where the curve *crosses* zero,
        but also where it is *tangent* to zero.
        For example, y=x-3 crosses zero at x=3,
        while y=(x-3)^2 is tangent to zero at x=3.

        We define y=x-3 as having a zero of order 0 at x=3,
        since only the "derivative of order zero" (the curve itself)
        is zero at that point.
        Similarly, y=(x-3)^2 has a zero of order 1 at x=3,
        since the first derivative (but not the second derivative)
        is zero at that point.

        Currently, this function up to third-order zeros
        (e.g. y=x^4 has a third-order zero at x=0,
        since everything up to the third derivative is zero at x=0).

        The current tolerance is used to determine
        whether a given point should be considered a zero,
        and of what order.
        For example, the curve y=x^2-0.0001 is *exactly* zero at x=0.01 and x=-0.01.
        However, note that the curve is also very close to zero at x=0,
        and at that point the first derivative is *also* zero.
        In many cases, it is reasonable to assume that
        the 0.0001 is an artifact of numerical roundoff,
        and the curve actually has a single zero of order 1 at x=0.
        The current tolerance is used to choose which case to report.
        In this example, a tolerance of 0.000001
        would mean that we consider 0.0001 a meaningful value (not just roundoff),
        so we would end up reporting two order-0 zeros at x=0.01 and x=-0.01.
        On the other hand, a tolerance of 0.01 would mean that
        we consider 0.0001 as just roundoff error,
        so we would end up reporting a single order-1 zero at x=0
        (the point at which the *first derivative* is zero).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._lengthcurve_ptr
        )
        output = _Result_List_c_void_p()
        _lib.opensolid_LengthCurve_zeros(ctypes.byref(inputs), ctypes.byref(output))
        return (
            [
                Curve.Zero._new(c_void_p(item))
                for item in [
                    output.field2.field1[index] for index in range(output.field2.field0)
                ]
            ]
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if a curve is zero everywhere, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._lengthcurve_ptr
        )
        output = c_int64()
        _lib.opensolid_LengthCurve_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __neg__(self) -> LengthCurve:
        """Return ``-self``."""
        inputs = self._lengthcurve_ptr
        output = c_void_p()
        _lib.opensolid_LengthCurve_neg(ctypes.byref(inputs), ctypes.byref(output))
        return LengthCurve._new(output)

    @overload
    def __add__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    @overload
    def __add__(self, rhs: Length) -> LengthCurve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_add_LengthCurve_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_add_LengthCurve_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    @overload
    def __sub__(self, rhs: Length) -> LengthCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_sub_LengthCurve_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_sub_LengthCurve_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> LengthCurve:
        pass

    @overload
    def __mul__(self, rhs: LengthCurve) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: Length) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> LengthCurve:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._lengthcurve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_LengthCurve_mul_LengthCurve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case LengthCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._lengthcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_mul_LengthCurve_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_mul_LengthCurve_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._curve_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_mul_LengthCurve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> LengthCurve:
        pass

    @overload
    def __truediv__(self, rhs: LengthCurve) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> LengthCurve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._lengthcurve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_LengthCurve_div_LengthCurve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case LengthCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _length_tolerance()._length_ptr,
                    self._lengthcurve_ptr,
                    rhs._lengthcurve_ptr,
                )
                output = _Result_c_void_p()
                _lib.opensolid_LengthCurve_div_LengthCurve_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._lengthcurve_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_LengthCurve_div_LengthCurve_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._lengthcurve_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_LengthCurve_div_LengthCurve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    LengthCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> LengthCurve:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._lengthcurve_ptr)
        output = c_void_p()
        _lib.opensolid_LengthCurve_mul_Float_LengthCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return LengthCurve._new(output)


def _lengthcurve_zero() -> LengthCurve:
    output = c_void_p()
    _lib.opensolid_LengthCurve_zero(c_void_p(), ctypes.byref(output))
    return LengthCurve._new(output)


LengthCurve.zero = _lengthcurve_zero()


class AreaCurve:
    """A parametric curve definining an area in terms of a parameter value."""

    _areacurve_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> AreaCurve:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(AreaCurve)
        obj._areacurve_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._areacurve_ptr)

    zero: AreaCurve = None  # type: ignore[assignment]
    """A curve equal to zero everywhere."""

    @staticmethod
    def constant(value: Area) -> AreaCurve:
        """Create a curve with the given constant value."""
        inputs = value._area_ptr
        output = c_void_p()
        _lib.opensolid_AreaCurve_constant_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaCurve._new(output)

    @staticmethod
    def line(start: Area, end: Area) -> AreaCurve:
        """Create a curve that linearly interpolates from the first value to the second."""
        inputs = _Tuple2_c_void_p_c_void_p(start._area_ptr, end._area_ptr)
        output = c_void_p()
        _lib.opensolid_AreaCurve_line_Area_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaCurve._new(output)

    def sqrt(self) -> LengthCurve:
        """Compute the square root of a curve."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._areacurve_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaCurve_sqrt(ctypes.byref(inputs), ctypes.byref(output))
        return LengthCurve._new(output)

    def evaluate(self, parameter_value: float) -> Area:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._areacurve_ptr)
        output = c_void_p()
        _lib.opensolid_AreaCurve_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    def zeros(self) -> list[Curve.Zero]:
        """Find all points at which the given curve is zero.

        This includes not only points where the curve *crosses* zero,
        but also where it is *tangent* to zero.
        For example, y=x-3 crosses zero at x=3,
        while y=(x-3)^2 is tangent to zero at x=3.

        We define y=x-3 as having a zero of order 0 at x=3,
        since only the "derivative of order zero" (the curve itself)
        is zero at that point.
        Similarly, y=(x-3)^2 has a zero of order 1 at x=3,
        since the first derivative (but not the second derivative)
        is zero at that point.

        Currently, this function up to third-order zeros
        (e.g. y=x^4 has a third-order zero at x=0,
        since everything up to the third derivative is zero at x=0).

        The current tolerance is used to determine
        whether a given point should be considered a zero,
        and of what order.
        For example, the curve y=x^2-0.0001 is *exactly* zero at x=0.01 and x=-0.01.
        However, note that the curve is also very close to zero at x=0,
        and at that point the first derivative is *also* zero.
        In many cases, it is reasonable to assume that
        the 0.0001 is an artifact of numerical roundoff,
        and the curve actually has a single zero of order 1 at x=0.
        The current tolerance is used to choose which case to report.
        In this example, a tolerance of 0.000001
        would mean that we consider 0.0001 a meaningful value (not just roundoff),
        so we would end up reporting two order-0 zeros at x=0.01 and x=-0.01.
        On the other hand, a tolerance of 0.01 would mean that
        we consider 0.0001 as just roundoff error,
        so we would end up reporting a single order-1 zero at x=0
        (the point at which the *first derivative* is zero).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _area_tolerance()._area_ptr, self._areacurve_ptr
        )
        output = _Result_List_c_void_p()
        _lib.opensolid_AreaCurve_zeros(ctypes.byref(inputs), ctypes.byref(output))
        return (
            [
                Curve.Zero._new(c_void_p(item))
                for item in [
                    output.field2.field1[index] for index in range(output.field2.field0)
                ]
            ]
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if a curve is zero everywhere, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _area_tolerance()._area_ptr, self._areacurve_ptr
        )
        output = c_int64()
        _lib.opensolid_AreaCurve_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __neg__(self) -> AreaCurve:
        """Return ``-self``."""
        inputs = self._areacurve_ptr
        output = c_void_p()
        _lib.opensolid_AreaCurve_neg(ctypes.byref(inputs), ctypes.byref(output))
        return AreaCurve._new(output)

    @overload
    def __add__(self, rhs: AreaCurve) -> AreaCurve:
        pass

    @overload
    def __add__(self, rhs: Area) -> AreaCurve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case AreaCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areacurve_ptr, rhs._areacurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaCurve_add_AreaCurve_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._areacurve_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_AreaCurve_add_AreaCurve_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: AreaCurve) -> AreaCurve:
        pass

    @overload
    def __sub__(self, rhs: Area) -> AreaCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case AreaCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areacurve_ptr, rhs._areacurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaCurve_sub_AreaCurve_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._areacurve_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_AreaCurve_sub_AreaCurve_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> AreaCurve:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> AreaCurve:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._areacurve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AreaCurve_mul_AreaCurve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._areacurve_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_AreaCurve_mul_AreaCurve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> AreaCurve:
        pass

    @overload
    def __truediv__(self, rhs: AreaCurve) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> LengthCurve:
        pass

    @overload
    def __truediv__(self, rhs: Area) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> AreaCurve:
        pass

    @overload
    def __truediv__(self, rhs: LengthCurve) -> LengthCurve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._areacurve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AreaCurve_div_AreaCurve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaCurve._new(output)
            case AreaCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _length_tolerance()._length_ptr,
                    self._areacurve_ptr,
                    rhs._areacurve_ptr,
                )
                output = _Result_c_void_p()
                _lib.opensolid_AreaCurve_div_AreaCurve_AreaCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._areacurve_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_AreaCurve_div_AreaCurve_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return LengthCurve._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._areacurve_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_AreaCurve_div_AreaCurve_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._areacurve_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_AreaCurve_div_AreaCurve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    AreaCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case LengthCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _length_tolerance()._length_ptr,
                    self._areacurve_ptr,
                    rhs._lengthcurve_ptr,
                )
                output = _Result_c_void_p()
                _lib.opensolid_AreaCurve_div_AreaCurve_LengthCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    LengthCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> AreaCurve:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._areacurve_ptr)
        output = c_void_p()
        _lib.opensolid_AreaCurve_mul_Float_AreaCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaCurve._new(output)


def _areacurve_zero() -> AreaCurve:
    output = c_void_p()
    _lib.opensolid_AreaCurve_zero(c_void_p(), ctypes.byref(output))
    return AreaCurve._new(output)


AreaCurve.zero = _areacurve_zero()


class AngleCurve:
    """A parametric curve definining an angle in terms of a parameter value."""

    _anglecurve_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> AngleCurve:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(AngleCurve)
        obj._anglecurve_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._anglecurve_ptr)

    zero: AngleCurve = None  # type: ignore[assignment]
    """A curve equal to zero everywhere."""

    @staticmethod
    def constant(value: Angle) -> AngleCurve:
        """Create a curve with the given constant value."""
        inputs = value._angle_ptr
        output = c_void_p()
        _lib.opensolid_AngleCurve_constant_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleCurve._new(output)

    @staticmethod
    def line(start: Angle, end: Angle) -> AngleCurve:
        """Create a curve that linearly interpolates from the first value to the second."""
        inputs = _Tuple2_c_void_p_c_void_p(start._angle_ptr, end._angle_ptr)
        output = c_void_p()
        _lib.opensolid_AngleCurve_line_Angle_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleCurve._new(output)

    def sin(self) -> Curve:
        """Compute the sine of a curve."""
        inputs = self._anglecurve_ptr
        output = c_void_p()
        _lib.opensolid_AngleCurve_sin(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def cos(self) -> Curve:
        """Compute the cosine of a curve."""
        inputs = self._anglecurve_ptr
        output = c_void_p()
        _lib.opensolid_AngleCurve_cos(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def evaluate(self, parameter_value: float) -> Angle:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._anglecurve_ptr)
        output = c_void_p()
        _lib.opensolid_AngleCurve_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    def zeros(self) -> list[Curve.Zero]:
        """Find all points at which the given curve is zero.

        This includes not only points where the curve *crosses* zero,
        but also where it is *tangent* to zero.
        For example, y=x-3 crosses zero at x=3,
        while y=(x-3)^2 is tangent to zero at x=3.

        We define y=x-3 as having a zero of order 0 at x=3,
        since only the "derivative of order zero" (the curve itself)
        is zero at that point.
        Similarly, y=(x-3)^2 has a zero of order 1 at x=3,
        since the first derivative (but not the second derivative)
        is zero at that point.

        Currently, this function up to third-order zeros
        (e.g. y=x^4 has a third-order zero at x=0,
        since everything up to the third derivative is zero at x=0).

        The current tolerance is used to determine
        whether a given point should be considered a zero,
        and of what order.
        For example, the curve y=x^2-0.0001 is *exactly* zero at x=0.01 and x=-0.01.
        However, note that the curve is also very close to zero at x=0,
        and at that point the first derivative is *also* zero.
        In many cases, it is reasonable to assume that
        the 0.0001 is an artifact of numerical roundoff,
        and the curve actually has a single zero of order 1 at x=0.
        The current tolerance is used to choose which case to report.
        In this example, a tolerance of 0.000001
        would mean that we consider 0.0001 a meaningful value (not just roundoff),
        so we would end up reporting two order-0 zeros at x=0.01 and x=-0.01.
        On the other hand, a tolerance of 0.01 would mean that
        we consider 0.0001 as just roundoff error,
        so we would end up reporting a single order-1 zero at x=0
        (the point at which the *first derivative* is zero).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _angle_tolerance()._angle_ptr, self._anglecurve_ptr
        )
        output = _Result_List_c_void_p()
        _lib.opensolid_AngleCurve_zeros(ctypes.byref(inputs), ctypes.byref(output))
        return (
            [
                Curve.Zero._new(c_void_p(item))
                for item in [
                    output.field2.field1[index] for index in range(output.field2.field0)
                ]
            ]
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if a curve is zero everywhere, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _angle_tolerance()._angle_ptr, self._anglecurve_ptr
        )
        output = c_int64()
        _lib.opensolid_AngleCurve_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def __neg__(self) -> AngleCurve:
        """Return ``-self``."""
        inputs = self._anglecurve_ptr
        output = c_void_p()
        _lib.opensolid_AngleCurve_neg(ctypes.byref(inputs), ctypes.byref(output))
        return AngleCurve._new(output)

    @overload
    def __add__(self, rhs: AngleCurve) -> AngleCurve:
        pass

    @overload
    def __add__(self, rhs: Angle) -> AngleCurve:
        pass

    def __add__(self, rhs):
        """Return ``self <> rhs``."""
        match rhs:
            case AngleCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglecurve_ptr, rhs._anglecurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleCurve_add_AngleCurve_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._anglecurve_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_AngleCurve_add_AngleCurve_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __sub__(self, rhs: AngleCurve) -> AngleCurve:
        pass

    @overload
    def __sub__(self, rhs: Angle) -> AngleCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case AngleCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._anglecurve_ptr, rhs._anglecurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_AngleCurve_sub_AngleCurve_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._anglecurve_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_AngleCurve_sub_AngleCurve_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __mul__(self, rhs: float) -> AngleCurve:
        pass

    @overload
    def __mul__(self, rhs: Curve) -> AngleCurve:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._anglecurve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AngleCurve_mul_AngleCurve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case Curve():
                inputs = _Tuple2_c_void_p_c_void_p(self._anglecurve_ptr, rhs._curve_ptr)
                output = c_void_p()
                _lib.opensolid_AngleCurve_mul_AngleCurve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> AngleCurve:
        pass

    @overload
    def __truediv__(self, rhs: AngleCurve) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Angle) -> Curve:
        pass

    @overload
    def __truediv__(self, rhs: Curve) -> AngleCurve:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._anglecurve_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AngleCurve_div_AngleCurve_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AngleCurve._new(output)
            case AngleCurve():
                inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
                    _angle_tolerance()._angle_ptr,
                    self._anglecurve_ptr,
                    rhs._anglecurve_ptr,
                )
                output = _Result_c_void_p()
                _lib.opensolid_AngleCurve_div_AngleCurve_AngleCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    Curve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case Angle():
                inputs = _Tuple2_c_void_p_c_void_p(self._anglecurve_ptr, rhs._angle_ptr)
                output = c_void_p()
                _lib.opensolid_AngleCurve_div_AngleCurve_Angle(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve._new(output)
            case Curve():
                inputs = _Tuple3_c_double_c_void_p_c_void_p(
                    _float_tolerance(), self._anglecurve_ptr, rhs._curve_ptr
                )
                output = _Result_c_void_p()
                _lib.opensolid_AngleCurve_div_AngleCurve_Curve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return (
                    AngleCurve._new(c_void_p(output.field2))
                    if output.field0 == 0
                    else _error(_text_to_str(output.field1))
                )
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> AngleCurve:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._anglecurve_ptr)
        output = c_void_p()
        _lib.opensolid_AngleCurve_mul_Float_AngleCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AngleCurve._new(output)


def _anglecurve_zero() -> AngleCurve:
    output = c_void_p()
    _lib.opensolid_AngleCurve_zero(c_void_p(), ctypes.byref(output))
    return AngleCurve._new(output)


AngleCurve.zero = _anglecurve_zero()


class Drawing2d:
    """A 2D drawing composed of shapes with attributes such as colour and stroke width."""

    _drawing2d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Drawing2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Drawing2d)
        obj._drawing2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._drawing2d_ptr)

    black_stroke: Drawing2d.Attribute = None  # type: ignore[assignment]
    """Black stroke for curves and borders."""

    no_fill: Drawing2d.Attribute = None  # type: ignore[assignment]
    """Set shapes to have no fill."""

    @staticmethod
    def group(drawings: list[Drawing2d]) -> Drawing2d:
        """Group several drawings into a single drawing."""
        inputs = _list_argument(
            _List_c_void_p,
            (c_void_p * len(drawings))(*[item._drawing2d_ptr for item in drawings]),
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_group_ListDrawing2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def group_with(
        attributes: list[Drawing2d.Attribute], drawings: list[Drawing2d]
    ) -> Drawing2d:
        """Group several drawings into a single drawing, applying the given attributes to the group."""
        inputs = _Tuple2_List_c_void_p_List_c_void_p(
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(drawings))(*[item._drawing2d_ptr for item in drawings]),
            ),
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_groupWith_ListDrawing2dAttribute_ListDrawing2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def polygon(vertices: list[Point2d]) -> Drawing2d:
        """Create a polygon with the given vertices."""
        inputs = _list_argument(
            _List_c_void_p,
            (c_void_p * len(vertices))(*[item._point2d_ptr for item in vertices]),
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_polygon_ListPoint2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def polygon_with(
        attributes: list[Drawing2d.Attribute], vertices: list[Point2d]
    ) -> Drawing2d:
        """Create a polygon with the given attributes and vertices."""
        inputs = _Tuple2_List_c_void_p_List_c_void_p(
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(vertices))(*[item._point2d_ptr for item in vertices]),
            ),
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_polygonWith_ListDrawing2dAttribute_ListPoint2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def circle(*, center_point: Point2d, diameter: Length) -> Drawing2d:
        """Create a circle with the given center point and diameter."""
        inputs = _Tuple2_c_void_p_c_void_p(
            center_point._point2d_ptr, diameter._length_ptr
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_circle_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def circle_with(
        attributes: list[Drawing2d.Attribute],
        *,
        center_point: Point2d,
        diameter: Length,
    ) -> Drawing2d:
        """Create a circle with the given attributes, center point and diameter."""
        inputs = _Tuple3_List_c_void_p_c_void_p_c_void_p(
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            center_point._point2d_ptr,
            diameter._length_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_circleWith_ListDrawing2dAttribute_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def curve(resolution: Resolution, curve: Curve2d) -> Drawing2d:
        """Draw a curve with the given resolution."""
        inputs = _Tuple2_c_void_p_c_void_p(
            resolution._resolution_ptr, curve._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_curve_Resolution_Curve2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def curve_with(
        attributes: list[Drawing2d.Attribute], resolution: Resolution, curve: Curve2d
    ) -> Drawing2d:
        """Draw a curve with the given attributes and resolution."""
        inputs = _Tuple3_List_c_void_p_c_void_p_c_void_p(
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            resolution._resolution_ptr,
            curve._curve2d_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Drawing2d_curveWith_ListDrawing2dAttribute_Resolution_Curve2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d._new(output)

    @staticmethod
    def stroke_color(color: Color) -> Drawing2d.Attribute:
        """Set the stroke color for curves and borders."""
        inputs = color._color_ptr
        output = c_void_p()
        _lib.opensolid_Drawing2d_strokeColor_Color(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d.Attribute._new(output)

    @staticmethod
    def fill_color(color: Color) -> Drawing2d.Attribute:
        """Set the fill color for shapes."""
        inputs = color._color_ptr
        output = c_void_p()
        _lib.opensolid_Drawing2d_fillColor_Color(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Drawing2d.Attribute._new(output)

    def to_svg(self, view_box: Bounds2d) -> str:
        """Render a drawing to SVG.

        The given bounding box defines the overall size of the drawing;
        anything outside of this will be cropped.
        """
        inputs = _Tuple2_c_void_p_c_void_p(view_box._bounds2d_ptr, self._drawing2d_ptr)
        output = _Text()
        _lib.opensolid_Drawing2d_toSVG_Bounds2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return _text_to_str(output)

    def write_svg(self, path: str, view_box: Bounds2d) -> None:
        """Render SVG to a file.

        The given bounding box defines the overall size of the drawing;
        anything outside of this will be cropped.
        """
        inputs = _Tuple3_Text_c_void_p_c_void_p(
            _str_to_text(path), view_box._bounds2d_ptr, self._drawing2d_ptr
        )
        output = _Result_c_int64()
        _lib.opensolid_Drawing2d_writeSVG_Text_Bounds2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return None if output.field0 == 0 else _error(_text_to_str(output.field1))

    class Attribute:
        """A drawing attribute such as fill color or stroke width."""

        _attribute_ptr: c_void_p

        @staticmethod
        def _new(ptr: c_void_p) -> Drawing2d.Attribute:
            """Construct directly from an underlying C pointer."""
            obj = object.__new__(Drawing2d.Attribute)
            obj._attribute_ptr = ptr

            return obj

        def __del__(self) -> None:
            """Free the underlying Haskell value."""
            _lib.opensolid_release(self._attribute_ptr)


def _drawing2d_black_stroke() -> Drawing2d.Attribute:
    output = c_void_p()
    _lib.opensolid_Drawing2d_blackStroke(c_void_p(), ctypes.byref(output))
    return Drawing2d.Attribute._new(output)


Drawing2d.black_stroke = _drawing2d_black_stroke()


def _drawing2d_no_fill() -> Drawing2d.Attribute:
    output = c_void_p()
    _lib.opensolid_Drawing2d_noFill(c_void_p(), ctypes.byref(output))
    return Drawing2d.Attribute._new(output)


Drawing2d.no_fill = _drawing2d_no_fill()


class Axis2d:
    """An axis in 2D, defined by an origin point and direction."""

    _axis2d_ptr: c_void_p

    def __init__(self, origin_point: Point2d, direction: Direction2d) -> None:
        """Construct an axis from its origin point and direction."""
        inputs = _Tuple2_c_void_p_c_void_p(
            origin_point._point2d_ptr, direction._direction2d_ptr
        )
        self._axis2d_ptr = c_void_p()
        _lib.opensolid_Axis2d_constructor_Point2d_Direction2d(
            ctypes.byref(inputs), ctypes.byref(self._axis2d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Axis2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Axis2d)
        obj._axis2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._axis2d_ptr)

    x: Axis2d = None  # type: ignore[assignment]
    """The X axis."""

    y: Axis2d = None  # type: ignore[assignment]
    """The Y axis."""

    @cached_property
    def origin_point(self) -> Point2d:
        """Get the origin point of an axis."""
        inputs = self._axis2d_ptr
        output = c_void_p()
        _lib.opensolid_Axis2d_originPoint(ctypes.byref(inputs), ctypes.byref(output))
        return Point2d._new(output)

    @cached_property
    def direction(self) -> Direction2d:
        """Get the direction of an axis."""
        inputs = self._axis2d_ptr
        output = c_void_p()
        _lib.opensolid_Axis2d_direction(ctypes.byref(inputs), ctypes.byref(output))
        return Direction2d._new(output)

    def place_on(self, plane: Plane3d) -> Axis3d:
        """Convert a 2D axis to 3D axis by placing it on a plane.

        Given a 2D axis defined within a plane's coordinate system,
        this returns the corresponding 3D axis.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._axis2d_ptr)
        output = c_void_p()
        _lib.opensolid_Axis2d_placeOn_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def mirror_across(self, axis: Axis2d) -> Axis2d:
        """Mirror across the given axis."""
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._axis2d_ptr)
        output = c_void_p()
        _lib.opensolid_Axis2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis2d._new(output)

    def translate_by(self, displacement: Displacement2d) -> Axis2d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement2d_ptr, self._axis2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis2d_translateBy_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis2d._new(output)

    def translate_in(self, direction: Direction2d, distance: Length) -> Axis2d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction2d_ptr, distance._length_ptr, self._axis2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis2d_translateIn_Direction2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis2d._new(output)

    def translate_along(self, axis: Axis2d, distance: Length) -> Axis2d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis2d_ptr, distance._length_ptr, self._axis2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis2d_translateAlong_Axis2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis2d._new(output)

    def rotate_around(self, point: Point2d, angle: Angle) -> Axis2d:
        """Rotate around the given point by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            point._point2d_ptr, angle._angle_ptr, self._axis2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis2d_rotateAround_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis2d._new(output)


def _axis2d_x() -> Axis2d:
    output = c_void_p()
    _lib.opensolid_Axis2d_x(c_void_p(), ctypes.byref(output))
    return Axis2d._new(output)


Axis2d.x = _axis2d_x()


def _axis2d_y() -> Axis2d:
    output = c_void_p()
    _lib.opensolid_Axis2d_y(c_void_p(), ctypes.byref(output))
    return Axis2d._new(output)


Axis2d.y = _axis2d_y()


class UvAxis:
    """An axis in 2D, defined by an origin point and direction."""

    _uvaxis_ptr: c_void_p

    def __init__(self, origin_point: UvPoint, direction: UvDirection) -> None:
        """Construct an axis from its origin point and direction."""
        inputs = _Tuple2_c_void_p_c_void_p(
            origin_point._uvpoint_ptr, direction._uvdirection_ptr
        )
        self._uvaxis_ptr = c_void_p()
        _lib.opensolid_UvAxis_constructor_UvPoint_UvDirection(
            ctypes.byref(inputs), ctypes.byref(self._uvaxis_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> UvAxis:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvAxis)
        obj._uvaxis_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvaxis_ptr)

    u: UvAxis = None  # type: ignore[assignment]
    """The U axis."""

    v: UvAxis = None  # type: ignore[assignment]
    """The V axis."""

    @cached_property
    def origin_point(self) -> UvPoint:
        """Get the origin point of an axis."""
        inputs = self._uvaxis_ptr
        output = c_void_p()
        _lib.opensolid_UvAxis_originPoint(ctypes.byref(inputs), ctypes.byref(output))
        return UvPoint._new(output)

    @cached_property
    def direction(self) -> UvDirection:
        """Get the direction of an axis."""
        inputs = self._uvaxis_ptr
        output = c_void_p()
        _lib.opensolid_UvAxis_direction(ctypes.byref(inputs), ctypes.byref(output))
        return UvDirection._new(output)


def _uvaxis_u() -> UvAxis:
    output = c_void_p()
    _lib.opensolid_UvAxis_u(c_void_p(), ctypes.byref(output))
    return UvAxis._new(output)


UvAxis.u = _uvaxis_u()


def _uvaxis_v() -> UvAxis:
    output = c_void_p()
    _lib.opensolid_UvAxis_v(c_void_p(), ctypes.byref(output))
    return UvAxis._new(output)


UvAxis.v = _uvaxis_v()


class Convention3d:
    """A coordinate convention in 3D space.

    This defines which of X, Y and Z mean 'forward' or 'upward' or 'rightward'.
    """

    _convention3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Convention3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Convention3d)
        obj._convention3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._convention3d_ptr)

    y_up: Convention3d = None  # type: ignore[assignment]
    """A convention where positive X is leftward, positive Y is upward, and positive Z is forward.

    This is the convention used by (among other things) the glTF file format.
    """

    z_up: Convention3d = None  # type: ignore[assignment]
    """A convention where positive X is rightward, positive Y is forward and positive Z is upward.

    This is the convention used by (among other things) the Blender animation package.
    """


def _convention3d_y_up() -> Convention3d:
    output = c_void_p()
    _lib.opensolid_Convention3d_yUp(c_void_p(), ctypes.byref(output))
    return Convention3d._new(output)


Convention3d.y_up = _convention3d_y_up()


def _convention3d_z_up() -> Convention3d:
    output = c_void_p()
    _lib.opensolid_Convention3d_zUp(c_void_p(), ctypes.byref(output))
    return Convention3d._new(output)


Convention3d.z_up = _convention3d_z_up()


class Vector3d:
    """A unitless vector in 3D."""

    _vector3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Vector3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Vector3d)
        obj._vector3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._vector3d_ptr)

    zero: Vector3d = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def unit(direction: Direction3d) -> Vector3d:
        """Construct a unit vector in the given direction."""
        inputs = direction._direction3d_ptr
        output = c_void_p()
        _lib.opensolid_Vector3d_unit_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    @staticmethod
    def xyz(
        convention: Convention3d, components: tuple[float, float, float]
    ) -> Vector3d:
        """Construct a vector from its XYZ components, given the coordinate convention to use."""
        inputs = _Tuple2_c_void_p_Tuple3_c_double_c_double_c_double(
            convention._convention3d_ptr,
            _Tuple3_c_double_c_double_c_double(
                components[0], components[1], components[2]
            ),
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_xyz_Convention3d_Tuple3FloatFloatFloat(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    @staticmethod
    def z_up(x_component: float, y_component: float, z_component: float) -> Vector3d:
        """Construct a vector from its XYZ components, using a Z-up convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = _Tuple3_c_double_c_double_c_double(
            x_component, y_component, z_component
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_zUp_Float_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    @staticmethod
    def y_up(x_component: float, y_component: float, z_component: float) -> Vector3d:
        """Construct a vector from its XYZ components, using a Y-up convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = _Tuple3_c_double_c_double_c_double(
            x_component, y_component, z_component
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_yUp_Float_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def components(self, convention: Convention3d) -> tuple[float, float, float]:
        """Get the XYZ components of a vector, given an XYZ coordinate convention to use."""
        inputs = _Tuple2_c_void_p_c_void_p(
            convention._convention3d_ptr, self._vector3d_ptr
        )
        output = _Tuple3_c_double_c_double_c_double()
        _lib.opensolid_Vector3d_components_Convention3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (output.field0, output.field1, output.field2)

    def z_up_components(self) -> tuple[float, float, float]:
        """Get the XYZ components of a vector using a Z-up coordinate convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = self._vector3d_ptr
        output = _Tuple3_c_double_c_double_c_double()
        _lib.opensolid_Vector3d_zUpComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (output.field0, output.field1, output.field2)

    def y_up_components(self) -> tuple[float, float, float]:
        """Get the XYZ components of a vector using a Y-up coordinate convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = self._vector3d_ptr
        output = _Tuple3_c_double_c_double_c_double()
        _lib.opensolid_Vector3d_yUpComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (output.field0, output.field1, output.field2)

    def direction(self) -> Direction3d:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._vector3d_ptr)
        output = _Result_c_void_p()
        _lib.opensolid_Vector3d_direction(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Direction3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if a vector is zero, within the current tolerance."""
        inputs = _Tuple2_c_double_c_void_p(_float_tolerance(), self._vector3d_ptr)
        output = c_int64()
        _lib.opensolid_Vector3d_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def rotate_in(self, direction: Direction3d, angle: Angle) -> Vector3d:
        """Rotate a vector in a given direction.

        This is equivalent to rotating around an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, angle._angle_ptr, self._vector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_rotateIn_Direction3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Vector3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._vector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def mirror_in(self, direction: Direction3d) -> Vector3d:
        """Mirror in a particular direction.

        This is equivalent to mirroring across a plane with the given normal direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction3d_ptr, self._vector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_mirrorIn_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def mirror_across(self, plane: Plane3d) -> Vector3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def scale_in(self, direction: Direction3d, scale: float) -> Vector3d:
        """Scale (stretch) in the given direction by the given scaling factor.

        This is equivalent to scaling along an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            direction._direction3d_ptr, scale, self._vector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_scaleIn_Direction3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def scale_along(self, axis: Axis3d, scale: float) -> Vector3d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis3d_ptr, scale, self._vector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Vector3d_scaleAlong_Axis3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def place_in(self, frame: Frame3d) -> Vector3d:
        """Convert a vectr defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def relative_to(self, frame: Frame3d) -> Vector3d:
        """Convert a vector defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def __neg__(self) -> Vector3d:
        """Return ``-self``."""
        inputs = self._vector3d_ptr
        output = c_void_p()
        _lib.opensolid_Vector3d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Vector3d._new(output)

    def __add__(self, rhs: Vector3d) -> Vector3d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._vector3d_ptr, rhs._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector3d_add_Vector3d_Vector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    def __sub__(self, rhs: Vector3d) -> Vector3d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._vector3d_ptr, rhs._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector3d_sub_Vector3d_Vector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    @overload
    def __mul__(self, rhs: float) -> Vector3d:
        pass

    @overload
    def __mul__(self, rhs: Length) -> Displacement3d:
        pass

    @overload
    def __mul__(self, rhs: Area) -> AreaVector3d:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._vector3d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Vector3d_mul_Vector3d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector3d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(self._vector3d_ptr, rhs._length_ptr)
                output = c_void_p()
                _lib.opensolid_Vector3d_mul_Vector3d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(self._vector3d_ptr, rhs._area_ptr)
                output = c_void_p()
                _lib.opensolid_Vector3d_mul_Vector3d_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector3d._new(output)
            case _:
                return NotImplemented

    def __truediv__(self, rhs: float) -> Vector3d:
        """Return ``self / rhs``."""
        inputs = _Tuple2_c_void_p_c_double(self._vector3d_ptr, rhs)
        output = c_void_p()
        _lib.opensolid_Vector3d_div_Vector3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)

    @overload
    def dot(self, rhs: Vector3d) -> float:
        pass

    @overload
    def dot(self, rhs: Displacement3d) -> Length:
        pass

    @overload
    def dot(self, rhs: AreaVector3d) -> Area:
        pass

    def dot(self, rhs):
        """Compute the dot product of two vector-like values."""
        match rhs:
            case Vector3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector3d_ptr, rhs._vector3d_ptr
                )
                output = c_double()
                _lib.opensolid_Vector3d_dot_Vector3d_Vector3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return output.value
            case Displacement3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector3d_ptr, rhs._displacement3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector3d_dot_Vector3d_Displacement3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case AreaVector3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector3d_ptr, rhs._areavector3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector3d_dot_Vector3d_AreaVector3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case _:
                return NotImplemented

    @overload
    def cross(self, rhs: Vector3d) -> Vector3d:
        pass

    @overload
    def cross(self, rhs: Displacement3d) -> Displacement3d:
        pass

    @overload
    def cross(self, rhs: AreaVector3d) -> AreaVector3d:
        pass

    def cross(self, rhs):
        """Compute the cross product of two vector-like values."""
        match rhs:
            case Vector3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector3d_ptr, rhs._vector3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector3d_cross_Vector3d_Vector3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector3d._new(output)
            case Displacement3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector3d_ptr, rhs._displacement3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector3d_cross_Vector3d_Displacement3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case AreaVector3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._vector3d_ptr, rhs._areavector3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Vector3d_cross_Vector3d_AreaVector3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector3d._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> Vector3d:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_Vector3d_mul_Float_Vector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector3d._new(output)


def _vector3d_zero() -> Vector3d:
    output = c_void_p()
    _lib.opensolid_Vector3d_zero(c_void_p(), ctypes.byref(output))
    return Vector3d._new(output)


Vector3d.zero = _vector3d_zero()


class Displacement3d:
    """A displacement vector in 3D."""

    _displacement3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Displacement3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Displacement3d)
        obj._displacement3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._displacement3d_ptr)

    zero: Displacement3d = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def xyz(
        convention: Convention3d, components: tuple[Length, Length, Length]
    ) -> Displacement3d:
        """Construct a vector from its XYZ components, given the coordinate convention to use."""
        inputs = _Tuple2_c_void_p_Tuple3_c_void_p_c_void_p_c_void_p(
            convention._convention3d_ptr,
            _Tuple3_c_void_p_c_void_p_c_void_p(
                components[0]._length_ptr,
                components[1]._length_ptr,
                components[2]._length_ptr,
            ),
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_xyz_Convention3d_Tuple3LengthLengthLength(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    @staticmethod
    def z_up(
        x_component: Length, y_component: Length, z_component: Length
    ) -> Displacement3d:
        """Construct a vector from its XYZ components, using a Z-up convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            x_component._length_ptr, y_component._length_ptr, z_component._length_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_zUp_Length_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    @staticmethod
    def y_up(
        x_component: Length, y_component: Length, z_component: Length
    ) -> Displacement3d:
        """Construct a vector from its XYZ components, using a Y-up convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            x_component._length_ptr, y_component._length_ptr, z_component._length_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_yUp_Length_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def components(self, convention: Convention3d) -> tuple[Length, Length, Length]:
        """Get the XYZ components of a vector, given an XYZ coordinate convention to use."""
        inputs = _Tuple2_c_void_p_c_void_p(
            convention._convention3d_ptr, self._displacement3d_ptr
        )
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Displacement3d_components_Convention3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
            Length._new(c_void_p(output.field2)),
        )

    def z_up_components(self) -> tuple[Length, Length, Length]:
        """Get the XYZ components of a vector using a Z-up coordinate convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = self._displacement3d_ptr
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Displacement3d_zUpComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
            Length._new(c_void_p(output.field2)),
        )

    def y_up_components(self) -> tuple[Length, Length, Length]:
        """Get the XYZ components of a vector using a Y-up coordinate convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = self._displacement3d_ptr
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Displacement3d_yUpComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
            Length._new(c_void_p(output.field2)),
        )

    def direction(self) -> Direction3d:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._displacement3d_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_Displacement3d_direction(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Direction3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if a displacement is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._displacement3d_ptr
        )
        output = c_int64()
        _lib.opensolid_Displacement3d_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def rotate_in(self, direction: Direction3d, angle: Angle) -> Displacement3d:
        """Rotate a vector in a given direction.

        This is equivalent to rotating around an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, angle._angle_ptr, self._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_rotateIn_Direction3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Displacement3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def mirror_in(self, direction: Direction3d) -> Displacement3d:
        """Mirror in a particular direction.

        This is equivalent to mirroring across a plane with the given normal direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction3d_ptr, self._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_mirrorIn_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def mirror_across(self, plane: Plane3d) -> Displacement3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def scale_in(self, direction: Direction3d, scale: float) -> Displacement3d:
        """Scale (stretch) in the given direction by the given scaling factor.

        This is equivalent to scaling along an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            direction._direction3d_ptr, scale, self._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_scaleIn_Direction3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def scale_along(self, axis: Axis3d, scale: float) -> Displacement3d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis3d_ptr, scale, self._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_scaleAlong_Axis3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def place_in(self, frame: Frame3d) -> Displacement3d:
        """Convert a vectr defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def relative_to(self, frame: Frame3d) -> Displacement3d:
        """Convert a vector defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def __neg__(self) -> Displacement3d:
        """Return ``-self``."""
        inputs = self._displacement3d_ptr
        output = c_void_p()
        _lib.opensolid_Displacement3d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Displacement3d._new(output)

    def __add__(self, rhs: Displacement3d) -> Displacement3d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._displacement3d_ptr, rhs._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_add_Displacement3d_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    def __sub__(self, rhs: Displacement3d) -> Displacement3d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._displacement3d_ptr, rhs._displacement3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Displacement3d_sub_Displacement3d_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)

    @overload
    def __mul__(self, rhs: float) -> Displacement3d:
        pass

    @overload
    def __mul__(self, rhs: Length) -> AreaVector3d:
        pass

    def __mul__(self, rhs):
        """Return ``self * rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._displacement3d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Displacement3d_mul_Displacement3d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement3d_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement3d_mul_Displacement3d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector3d._new(output)
            case _:
                return NotImplemented

    @overload
    def __truediv__(self, rhs: float) -> Displacement3d:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Vector3d:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._displacement3d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_Displacement3d_div_Displacement3d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement3d_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement3d_div_Displacement3d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector3d._new(output)
            case _:
                return NotImplemented

    @overload
    def dot(self, rhs: Displacement3d) -> Area:
        pass

    @overload
    def dot(self, rhs: Vector3d) -> Length:
        pass

    def dot(self, rhs):
        """Compute the dot product of two vector-like values."""
        match rhs:
            case Displacement3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement3d_ptr, rhs._displacement3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement3d_dot_Displacement3d_Displacement3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Area._new(output)
            case Vector3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement3d_ptr, rhs._vector3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement3d_dot_Displacement3d_Vector3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Length._new(output)
            case _:
                return NotImplemented

    @overload
    def cross(self, rhs: Displacement3d) -> AreaVector3d:
        pass

    @overload
    def cross(self, rhs: Vector3d) -> Displacement3d:
        pass

    def cross(self, rhs):
        """Compute the cross product of two vector-like values."""
        match rhs:
            case Displacement3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement3d_ptr, rhs._displacement3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement3d_cross_Displacement3d_Displacement3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector3d._new(output)
            case Vector3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._displacement3d_ptr, rhs._vector3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Displacement3d_cross_Displacement3d_Vector3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case _:
                return NotImplemented

    def __rmul__(self, lhs: float) -> Displacement3d:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Displacement3d_mul_Float_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement3d._new(output)


def _displacement3d_zero() -> Displacement3d:
    output = c_void_p()
    _lib.opensolid_Displacement3d_zero(c_void_p(), ctypes.byref(output))
    return Displacement3d._new(output)


Displacement3d.zero = _displacement3d_zero()


class AreaVector3d:
    """A vector in 3D with units of area."""

    _areavector3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> AreaVector3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(AreaVector3d)
        obj._areavector3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._areavector3d_ptr)

    zero: AreaVector3d = None  # type: ignore[assignment]
    """The zero vector."""

    @staticmethod
    def xyz(
        convention: Convention3d, components: tuple[Area, Area, Area]
    ) -> AreaVector3d:
        """Construct a vector from its XYZ components, given the coordinate convention to use."""
        inputs = _Tuple2_c_void_p_Tuple3_c_void_p_c_void_p_c_void_p(
            convention._convention3d_ptr,
            _Tuple3_c_void_p_c_void_p_c_void_p(
                components[0]._area_ptr,
                components[1]._area_ptr,
                components[2]._area_ptr,
            ),
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_xyz_Convention3d_Tuple3AreaAreaArea(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    @staticmethod
    def z_up(x_component: Area, y_component: Area, z_component: Area) -> AreaVector3d:
        """Construct a vector from its XYZ components, using a Z-up convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            x_component._area_ptr, y_component._area_ptr, z_component._area_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_zUp_Area_Area_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    @staticmethod
    def y_up(x_component: Area, y_component: Area, z_component: Area) -> AreaVector3d:
        """Construct a vector from its XYZ components, using a Y-up convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            x_component._area_ptr, y_component._area_ptr, z_component._area_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_yUp_Area_Area_Area(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def components(self, convention: Convention3d) -> tuple[Area, Area, Area]:
        """Get the XYZ components of a vector, given an XYZ coordinate convention to use."""
        inputs = _Tuple2_c_void_p_c_void_p(
            convention._convention3d_ptr, self._areavector3d_ptr
        )
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_AreaVector3d_components_Convention3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Area._new(c_void_p(output.field0)),
            Area._new(c_void_p(output.field1)),
            Area._new(c_void_p(output.field2)),
        )

    def z_up_components(self) -> tuple[Area, Area, Area]:
        """Get the XYZ components of a vector using a Z-up coordinate convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = self._areavector3d_ptr
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_AreaVector3d_zUpComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Area._new(c_void_p(output.field0)),
            Area._new(c_void_p(output.field1)),
            Area._new(c_void_p(output.field2)),
        )

    def y_up_components(self) -> tuple[Area, Area, Area]:
        """Get the XYZ components of a vector using a Y-up coordinate convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = self._areavector3d_ptr
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_AreaVector3d_yUpComponents(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Area._new(c_void_p(output.field0)),
            Area._new(c_void_p(output.field1)),
            Area._new(c_void_p(output.field2)),
        )

    def direction(self) -> Direction3d:
        """Attempt to get the direction of a vector.

        The current tolerance will be used to check if the vector is zero
        (and therefore does not have a direction).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _area_tolerance()._area_ptr, self._areavector3d_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_AreaVector3d_direction(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Direction3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def is_zero(self) -> bool:
        """Check if an area vector is zero, within the current tolerance."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _area_tolerance()._area_ptr, self._areavector3d_ptr
        )
        output = c_int64()
        _lib.opensolid_AreaVector3d_isZero(ctypes.byref(inputs), ctypes.byref(output))
        return bool(output.value)

    def rotate_in(self, direction: Direction3d, angle: Angle) -> AreaVector3d:
        """Rotate a vector in a given direction.

        This is equivalent to rotating around an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, angle._angle_ptr, self._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_rotateIn_Direction3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> AreaVector3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def mirror_in(self, direction: Direction3d) -> AreaVector3d:
        """Mirror in a particular direction.

        This is equivalent to mirroring across a plane with the given normal direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction3d_ptr, self._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_mirrorIn_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def mirror_across(self, plane: Plane3d) -> AreaVector3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._areavector3d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def scale_in(self, direction: Direction3d, scale: float) -> AreaVector3d:
        """Scale (stretch) in the given direction by the given scaling factor.

        This is equivalent to scaling along an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            direction._direction3d_ptr, scale, self._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_scaleIn_Direction3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def scale_along(self, axis: Axis3d, scale: float) -> AreaVector3d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis3d_ptr, scale, self._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_scaleAlong_Axis3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def place_in(self, frame: Frame3d) -> AreaVector3d:
        """Convert a vectr defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._areavector3d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def relative_to(self, frame: Frame3d) -> AreaVector3d:
        """Convert a vector defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._areavector3d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def __neg__(self) -> AreaVector3d:
        """Return ``-self``."""
        inputs = self._areavector3d_ptr
        output = c_void_p()
        _lib.opensolid_AreaVector3d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return AreaVector3d._new(output)

    def __add__(self, rhs: AreaVector3d) -> AreaVector3d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._areavector3d_ptr, rhs._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_add_AreaVector3d_AreaVector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def __sub__(self, rhs: AreaVector3d) -> AreaVector3d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._areavector3d_ptr, rhs._areavector3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_AreaVector3d_sub_AreaVector3d_AreaVector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def __mul__(self, rhs: float) -> AreaVector3d:
        """Return ``self * rhs``."""
        inputs = _Tuple2_c_void_p_c_double(self._areavector3d_ptr, rhs)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_mul_AreaVector3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    @overload
    def __truediv__(self, rhs: float) -> AreaVector3d:
        pass

    @overload
    def __truediv__(self, rhs: Length) -> Displacement3d:
        pass

    @overload
    def __truediv__(self, rhs: Area) -> Vector3d:
        pass

    def __truediv__(self, rhs):
        """Return ``self / rhs``."""
        match rhs:
            case float() | int():
                inputs = _Tuple2_c_void_p_c_double(self._areavector3d_ptr, rhs)
                output = c_void_p()
                _lib.opensolid_AreaVector3d_div_AreaVector3d_Float(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return AreaVector3d._new(output)
            case Length():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areavector3d_ptr, rhs._length_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaVector3d_div_AreaVector3d_Length(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case Area():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._areavector3d_ptr, rhs._area_ptr
                )
                output = c_void_p()
                _lib.opensolid_AreaVector3d_div_AreaVector3d_Area(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Vector3d._new(output)
            case _:
                return NotImplemented

    def dot(self, rhs: Vector3d) -> Area:
        """Compute the dot product of two vector-like values."""
        inputs = _Tuple2_c_void_p_c_void_p(self._areavector3d_ptr, rhs._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_dot_AreaVector3d_Vector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Area._new(output)

    def cross(self, rhs: Vector3d) -> AreaVector3d:
        """Compute the cross product of two vector-like values."""
        inputs = _Tuple2_c_void_p_c_void_p(self._areavector3d_ptr, rhs._vector3d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_cross_AreaVector3d_Vector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)

    def __rmul__(self, lhs: float) -> AreaVector3d:
        """Return ``lhs * self``."""
        inputs = _Tuple2_c_double_c_void_p(lhs, self._areavector3d_ptr)
        output = c_void_p()
        _lib.opensolid_AreaVector3d_mul_Float_AreaVector3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return AreaVector3d._new(output)


def _areavector3d_zero() -> AreaVector3d:
    output = c_void_p()
    _lib.opensolid_AreaVector3d_zero(c_void_p(), ctypes.byref(output))
    return AreaVector3d._new(output)


AreaVector3d.zero = _areavector3d_zero()


class Direction3d(Vector3d):
    """A direction in 3D.

    This is effectively a type-safe unit vector.
    """

    _direction3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Direction3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Direction3d)
        obj._direction3d_ptr = ptr
        obj._vector3d_ptr = c_void_p()
        _lib.opensolid_Direction3d_upcast(
            ctypes.byref(obj._direction3d_ptr), ctypes.byref(obj._vector3d_ptr)
        )
        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._direction3d_ptr)
        super().__del__()

    def perpendicular_direction(self) -> Direction3d:
        """Generate an arbitrary direction perpendicular to the given one."""
        inputs = self._direction3d_ptr
        output = c_void_p()
        _lib.opensolid_Direction3d_perpendicularDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def angle_to(self, other: Direction3d) -> Angle:
        """Measure the angle from one direction to another.

        The result will always be between 0 and 180 degrees.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            other._direction3d_ptr, self._direction3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Direction3d_angleTo_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Angle._new(output)

    def rotate_in(self, direction: Direction3d, angle: Angle) -> Direction3d:
        """Rotate a direction in a given other direction.

        This is equivalent to rotating around an axis with the given direction.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, angle._angle_ptr, self._direction3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Direction3d_rotateIn_Direction3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Direction3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._direction3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Direction3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def mirror_in(self, direction: Direction3d) -> Direction3d:
        """Mirror a direction in a given other direction.

        This is equivalent to mirroring across a plane with the given normal direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            direction._direction3d_ptr, self._direction3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Direction3d_mirrorIn_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def mirror_across(self, plane: Plane3d) -> Direction3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._direction3d_ptr)
        output = c_void_p()
        _lib.opensolid_Direction3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def place_in(self, frame: Frame3d) -> Direction3d:
        """Convert a direction defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._direction3d_ptr)
        output = c_void_p()
        _lib.opensolid_Direction3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def relative_to(self, frame: Frame3d) -> Direction3d:
        """Convert a direction defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._direction3d_ptr)
        output = c_void_p()
        _lib.opensolid_Direction3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def __neg__(self) -> Direction3d:
        """Return ``-self``."""
        inputs = self._direction3d_ptr
        output = c_void_p()
        _lib.opensolid_Direction3d_neg(ctypes.byref(inputs), ctypes.byref(output))
        return Direction3d._new(output)


class Point3d:
    """A point in 3D."""

    _point3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Point3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Point3d)
        obj._point3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._point3d_ptr)

    @staticmethod
    def along(axis: Axis3d, distance: Length) -> Point3d:
        """Construct a point the given distance along the given axis."""
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis3d_ptr, distance._length_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_along_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    @staticmethod
    def xyz(
        convention: Convention3d, coordinates: tuple[Length, Length, Length]
    ) -> Point3d:
        """Construct a point from its XYZ coordinates, given the coordinate convention to use."""
        inputs = _Tuple2_c_void_p_Tuple3_c_void_p_c_void_p_c_void_p(
            convention._convention3d_ptr,
            _Tuple3_c_void_p_c_void_p_c_void_p(
                coordinates[0]._length_ptr,
                coordinates[1]._length_ptr,
                coordinates[2]._length_ptr,
            ),
        )
        output = c_void_p()
        _lib.opensolid_Point3d_xyz_Convention3d_Tuple3LengthLengthLength(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    @staticmethod
    def z_up(
        x_coordinate: Length, y_coordinate: Length, z_coordinate: Length
    ) -> Point3d:
        """Construct a point from its XYZ coordinates, using a Z-up convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            x_coordinate._length_ptr, y_coordinate._length_ptr, z_coordinate._length_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_zUp_Length_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    @staticmethod
    def y_up(
        x_coordinate: Length, y_coordinate: Length, z_coordinate: Length
    ) -> Point3d:
        """Construct a point from its XYZ coordinates, using a Y-up convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            x_coordinate._length_ptr, y_coordinate._length_ptr, z_coordinate._length_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_yUp_Length_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def coordinates(self, convention: Convention3d) -> tuple[Length, Length, Length]:
        """Get the XYZ coordinates of a point, given an XYZ coordinate convention to use."""
        inputs = _Tuple2_c_void_p_c_void_p(
            convention._convention3d_ptr, self._point3d_ptr
        )
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Point3d_coordinates_Convention3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
            Length._new(c_void_p(output.field2)),
        )

    def z_up_coordinates(self) -> tuple[Length, Length, Length]:
        """Get the XYZ coordinates of a point using a Z-up coordinate convention.

        This is a convention where positive X is rightward, positive Y is forward and positive Z is upward.
        """
        inputs = self._point3d_ptr
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Point3d_zUpCoordinates(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
            Length._new(c_void_p(output.field2)),
        )

    def y_up_coordinates(self) -> tuple[Length, Length, Length]:
        """Get the XYZ coordinates of a point using a Y-up coordinate convention.

        This is a convention where positive X is leftward, positive Y is upward, and positive Z is forward.
        """
        inputs = self._point3d_ptr
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Point3d_yUpCoordinates(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Length._new(c_void_p(output.field0)),
            Length._new(c_void_p(output.field1)),
            Length._new(c_void_p(output.field2)),
        )

    def distance_to(self, other: Point3d) -> Length:
        """Compute the distance from one point to another."""
        inputs = _Tuple2_c_void_p_c_void_p(other._point3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_distanceTo_Point3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    def midpoint(self, other: Point3d) -> Point3d:
        """Find the midpoint between two points."""
        inputs = _Tuple2_c_void_p_c_void_p(other._point3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_midpoint_Point3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def project_onto(self, plane: Plane3d) -> Point3d:
        """Project a point onto a plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_projectOnto_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def project_into(self, plane: Plane3d) -> Point2d:
        """Project a point *into* a plane.

        Conceptualy, this projects the point onto the plane in 3D,
        then expresses the projected point in 2D planar XY coordinates.
        """
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_projectInto_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def place_in(self, frame: Frame3d) -> Point3d:
        """Convert a point defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def relative_to(self, frame: Frame3d) -> Point3d:
        """Convert a point defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def scale_along(self, axis: Axis3d, scale: float) -> Point3d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis3d_ptr, scale, self._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_scaleAlong_Axis3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def scale_about(self, point: Point3d, scale: float) -> Point3d:
        """Scale uniformly about the given point by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            point._point3d_ptr, scale, self._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_scaleAbout_Point3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def mirror_across(self, plane: Plane3d) -> Point3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._point3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def translate_by(self, displacement: Displacement3d) -> Point3d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement3d_ptr, self._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_translateBy_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def translate_in(self, direction: Direction3d, distance: Length) -> Point3d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, distance._length_ptr, self._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_translateIn_Direction3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def translate_along(self, axis: Axis3d, distance: Length) -> Point3d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, distance._length_ptr, self._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_translateAlong_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Point3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Point3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)

    @overload
    def __sub__(self, rhs: Point3d) -> Displacement3d:
        pass

    @overload
    def __sub__(self, rhs: Displacement3d) -> Point3d:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case Point3d():
                inputs = _Tuple2_c_void_p_c_void_p(self._point3d_ptr, rhs._point3d_ptr)
                output = c_void_p()
                _lib.opensolid_Point3d_sub_Point3d_Point3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Displacement3d._new(output)
            case Displacement3d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._point3d_ptr, rhs._displacement3d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Point3d_sub_Point3d_Displacement3d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Point3d._new(output)
            case _:
                return NotImplemented

    def __add__(self, rhs: Displacement3d) -> Point3d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._point3d_ptr, rhs._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Point3d_add_Point3d_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point3d._new(output)


class Bounds3d:
    """A bounding box in 3D."""

    _bounds3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Bounds3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Bounds3d)
        obj._bounds3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._bounds3d_ptr)

    @staticmethod
    def constant(point: Point3d) -> Bounds3d:
        """Construct a zero-size bounding box containing a single point."""
        inputs = point._point3d_ptr
        output = c_void_p()
        _lib.opensolid_Bounds3d_constant_Point3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    @staticmethod
    def from_corners(first_point: Point3d, second_point: Point3d) -> Bounds3d:
        """Construct a bounding box from two corner points."""
        inputs = _Tuple2_c_void_p_c_void_p(
            first_point._point3d_ptr, second_point._point3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_fromCorners_Point3d_Point3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    @staticmethod
    def hull(points: list[Point3d]) -> Bounds3d:
        """Construct a bounding box containing all vertices in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(points))(*[item._point3d_ptr for item in points]),
            )
            if points
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_hull_NonEmptyPoint3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    @staticmethod
    def aggregate(bounds: list[Bounds3d]) -> Bounds3d:
        """Construct a bounding box containing all bounding boxes in the given non-empty list."""
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(bounds))(*[item._bounds3d_ptr for item in bounds]),
            )
            if bounds
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_aggregate_NonEmptyBounds3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def coordinates(
        self, convention: Convention3d
    ) -> tuple[LengthBounds, LengthBounds, LengthBounds]:
        """Get the XYZ coordinate ranges of a bounding box, given an XYZ coordinate convention to use."""
        inputs = _Tuple2_c_void_p_c_void_p(
            convention._convention3d_ptr, self._bounds3d_ptr
        )
        output = _Tuple3_c_void_p_c_void_p_c_void_p()
        _lib.opensolid_Bounds3d_coordinates_Convention3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            LengthBounds._new(c_void_p(output.field0)),
            LengthBounds._new(c_void_p(output.field1)),
            LengthBounds._new(c_void_p(output.field2)),
        )

    def scale_along(self, axis: Axis3d, scale: float) -> Bounds3d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis3d_ptr, scale, self._bounds3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_scaleAlong_Axis3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def scale_about(self, point: Point3d, scale: float) -> Bounds3d:
        """Scale uniformly about the given point by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            point._point3d_ptr, scale, self._bounds3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_scaleAbout_Point3d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def mirror_across(self, plane: Plane3d) -> Bounds3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._bounds3d_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def translate_by(self, displacement: Displacement3d) -> Bounds3d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement3d_ptr, self._bounds3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_translateBy_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def translate_in(self, direction: Direction3d, distance: Length) -> Bounds3d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, distance._length_ptr, self._bounds3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_translateIn_Direction3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def translate_along(self, axis: Axis3d, distance: Length) -> Bounds3d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, distance._length_ptr, self._bounds3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_translateAlong_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Bounds3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._bounds3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Bounds3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def __add__(self, rhs: Displacement3d) -> Bounds3d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._bounds3d_ptr, rhs._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds3d_add_Bounds3d_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)

    def __sub__(self, rhs: Displacement3d) -> Bounds3d:
        """Return ``self - rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._bounds3d_ptr, rhs._displacement3d_ptr)
        output = c_void_p()
        _lib.opensolid_Bounds3d_sub_Bounds3d_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Bounds3d._new(output)


class Axis3d:
    """An axis in 3D, defined by an origin point and direction."""

    _axis3d_ptr: c_void_p

    def __init__(self, origin_point: Point3d, direction: Direction3d) -> None:
        """Construct an axis from its origin point and direction."""
        inputs = _Tuple2_c_void_p_c_void_p(
            origin_point._point3d_ptr, direction._direction3d_ptr
        )
        self._axis3d_ptr = c_void_p()
        _lib.opensolid_Axis3d_constructor_Point3d_Direction3d(
            ctypes.byref(inputs), ctypes.byref(self._axis3d_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Axis3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Axis3d)
        obj._axis3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._axis3d_ptr)

    @cached_property
    def origin_point(self) -> Point3d:
        """Get the origin point of an axis."""
        inputs = self._axis3d_ptr
        output = c_void_p()
        _lib.opensolid_Axis3d_originPoint(ctypes.byref(inputs), ctypes.byref(output))
        return Point3d._new(output)

    @cached_property
    def direction(self) -> Direction3d:
        """Get the direction of an axis."""
        inputs = self._axis3d_ptr
        output = c_void_p()
        _lib.opensolid_Axis3d_direction(ctypes.byref(inputs), ctypes.byref(output))
        return Direction3d._new(output)

    def normal_plane(self) -> Plane3d:
        """Construct a plane normal (perpendicular) to the given axis.

        The origin point of the plane will be the origin point of the axis,
        and the normal direction of the plane will be the direction of the axis.
        The X and Y directions of the plane will be chosen arbitrarily.
        """
        inputs = self._axis3d_ptr
        output = c_void_p()
        _lib.opensolid_Axis3d_normalPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    def move_to(self, point: Point3d) -> Axis3d:
        """Move an axis so that its origin point is the given point.

        The direction of the axis will remain unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(point._point3d_ptr, self._axis3d_ptr)
        output = c_void_p()
        _lib.opensolid_Axis3d_moveTo_Point3d(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    def reverse(self) -> Axis3d:
        """Reverse an axis (negate/reverse its direction).

        The origin point of the axis will remain unchanged.
        """
        inputs = self._axis3d_ptr
        output = c_void_p()
        _lib.opensolid_Axis3d_reverse(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    def place_in(self, frame: Frame3d) -> Axis3d:
        """Convert an axis defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._axis3d_ptr)
        output = c_void_p()
        _lib.opensolid_Axis3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def relative_to(self, frame: Frame3d) -> Axis3d:
        """Convert an axis defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._axis3d_ptr)
        output = c_void_p()
        _lib.opensolid_Axis3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def mirror_across(self, plane: Plane3d) -> Axis3d:
        """Mirror across the given plane."""
        inputs = _Tuple2_c_void_p_c_void_p(plane._plane3d_ptr, self._axis3d_ptr)
        output = c_void_p()
        _lib.opensolid_Axis3d_mirrorAcross_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def translate_by(self, displacement: Displacement3d) -> Axis3d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement3d_ptr, self._axis3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis3d_translateBy_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def translate_in(self, direction: Direction3d, distance: Length) -> Axis3d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, distance._length_ptr, self._axis3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis3d_translateIn_Direction3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def translate_along(self, axis: Axis3d, distance: Length) -> Axis3d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, distance._length_ptr, self._axis3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis3d_translateAlong_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Axis3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._axis3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Axis3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Axis3d._new(output)


class PlaneOrientation3d:
    """A pair of perpendicular X and Y directions defining the orientation of a plane in 3D."""

    _planeorientation3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> PlaneOrientation3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(PlaneOrientation3d)
        obj._planeorientation3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._planeorientation3d_ptr)

    @staticmethod
    def from_normal_direction(direction: Direction3d) -> PlaneOrientation3d:
        """Construct a plane orientation normal to the given direction.

        Both the X and Y directions of the returned orientation will be perpendicular to the given direction
        (and, of course, they will be perpendicular to each other),
        but otherwise they will be chosen arbitrarily.
        """
        inputs = direction._direction3d_ptr
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_fromNormalDirection_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @staticmethod
    def from_x_direction(direction: Direction3d) -> PlaneOrientation3d:
        """Construct a plane orientation from its X direction.

        The Y direction of the returned basis will be perpendicular to the given X direction,
        but otherwise will be chosen arbitrarily.
        """
        inputs = direction._direction3d_ptr
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_fromXDirection_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @staticmethod
    def from_y_direction(direction: Direction3d) -> PlaneOrientation3d:
        """Construct a plane orientation from its Y direction.

        The X direction of the returned basis will be perpendicular to the given Y direction,
        but otherwise will be chosen arbitrarily.
        """
        inputs = direction._direction3d_ptr
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_fromYDirection_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def x_direction(self) -> Direction3d:
        """Get the X direction of a plane orientation."""
        inputs = self._planeorientation3d_ptr
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_xDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def y_direction(self) -> Direction3d:
        """Get the Y direction of a plane orientation."""
        inputs = self._planeorientation3d_ptr
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_yDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def normal_direction(self) -> Direction3d:
        """Get the normal (outward) direction of a plane orientation."""
        inputs = self._planeorientation3d_ptr
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_normalDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    def place_in(self, frame: Frame3d) -> PlaneOrientation3d:
        """Convert a orientation defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(
            frame._frame3d_ptr, self._planeorientation3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    def relative_to(self, frame: Frame3d) -> PlaneOrientation3d:
        """Convert a orientation defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(
            frame._frame3d_ptr, self._planeorientation3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_PlaneOrientation3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)


class Plane3d:
    """A plane in 3D, defined by an origin point and two perpendicular X and Y directions.

    The normal direction  of the plane is then defined as
    the cross product of its X and Y directions.
    """

    _plane3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Plane3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Plane3d)
        obj._plane3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._plane3d_ptr)

    @staticmethod
    def from_point_and_normal(
        origin_point: Point3d, normal_direction: Direction3d
    ) -> Plane3d:
        """Construct a plane with the given origin point and normal direction.

        Both the X and Y directions of the returned plane will be perpendicular to the given direction
        (and, of course, they will be perpendicular to each other),
        but otherwise they will be chosen arbitrarily.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            origin_point._point3d_ptr, normal_direction._direction3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Plane3d_fromPointAndNormal_Point3d_Direction3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    @staticmethod
    def from_x_axis(axis: Axis3d) -> Plane3d:
        """Construct a plane having the given X axis, with an arbitrarily-chosen Y direction."""
        inputs = axis._axis3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_fromXAxis_Axis3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    @staticmethod
    def from_y_axis(axis: Axis3d) -> Plane3d:
        """Construct a plane having the given Y axis, with an arbitrarily-chosen X direction."""
        inputs = axis._axis3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_fromYAxis_Axis3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    @cached_property
    def origin_point(self) -> Point3d:
        """Get the origin point of a plane.

        This is the 3D point corresponding to (0,0) in the plane's local coordinates.
        """
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_originPoint(ctypes.byref(inputs), ctypes.byref(output))
        return Point3d._new(output)

    @cached_property
    def x_direction(self) -> Direction3d:
        """Get the X direction of a plane."""
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_xDirection(ctypes.byref(inputs), ctypes.byref(output))
        return Direction3d._new(output)

    @cached_property
    def y_direction(self) -> Direction3d:
        """Get the Y direction of a plane."""
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_yDirection(ctypes.byref(inputs), ctypes.byref(output))
        return Direction3d._new(output)

    @cached_property
    def normal_direction(self) -> Direction3d:
        """Get the normal direction of a plane."""
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_normalDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def x_axis(self) -> Axis3d:
        """Get the X axis of a plane.

        This is an axis formed from the plane's origin point and X direction.
        """
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_xAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def y_axis(self) -> Axis3d:
        """Get the Y axis of a plane.

        This is an axis formed from the plane's origin point and Y direction.
        """
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_yAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def normal_axis(self) -> Axis3d:
        """Construct an axis normal (perpendicular) to a plane.

        The origin point of the axis will be the origin point of the plane,
        and the direction of the axis will be the normal direction of the plane.
        """
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_normalAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    def move_to(self, point: Point3d) -> Plane3d:
        """Move a plane so that its origin point is the given point.

        The orientation of the plane will remain unchanged.
        """
        inputs = _Tuple2_c_void_p_c_void_p(point._point3d_ptr, self._plane3d_ptr)
        output = c_void_p()
        _lib.opensolid_Plane3d_moveTo_Point3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def flip(self) -> Plane3d:
        """Flip a plane such that its normal and X directions are reversed.

        The Y direction will remain constant.
        """
        inputs = self._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Plane3d_flip(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    def offset_by(self, distance: Length) -> Plane3d:
        """Offset a plane in its normal direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._plane3d_ptr)
        output = c_void_p()
        _lib.opensolid_Plane3d_offsetBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def place_in(self, frame: Frame3d) -> Plane3d:
        """Convert a plane defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._plane3d_ptr)
        output = c_void_p()
        _lib.opensolid_Plane3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def relative_to(self, frame: Frame3d) -> Plane3d:
        """Convert a plane defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._plane3d_ptr)
        output = c_void_p()
        _lib.opensolid_Plane3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def translate_by(self, displacement: Displacement3d) -> Plane3d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement3d_ptr, self._plane3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Plane3d_translateBy_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def translate_in(self, direction: Direction3d, distance: Length) -> Plane3d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, distance._length_ptr, self._plane3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Plane3d_translateIn_Direction3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def translate_along(self, axis: Axis3d, distance: Length) -> Plane3d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, distance._length_ptr, self._plane3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Plane3d_translateAlong_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Plane3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._plane3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Plane3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Plane3d._new(output)


class Orientation3d:
    """A set of cardinal directions (forward, upward etc.) defining a 3D orientation."""

    _orientation3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Orientation3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Orientation3d)
        obj._orientation3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._orientation3d_ptr)

    world: Orientation3d = None  # type: ignore[assignment]
    """The global orientation of the current coordinate space.

    That is, the forward direction of this orientation is the global forward direction,
    the upward direction of this orientation is the global upward direction, etc.
    """

    @cached_property
    def forward_direction(self) -> Direction3d:
        """Get the forward direction of a orientation."""
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_forwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def backward_direction(self) -> Direction3d:
        """Get the backward direction of a orientation."""
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_backwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def leftward_direction(self) -> Direction3d:
        """Get the leftward direction of a orientation."""
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_leftwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def rightward_direction(self) -> Direction3d:
        """Get the rightward direction of a orientation."""
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_rightwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def upward_direction(self) -> Direction3d:
        """Get the upward direction of a orientation."""
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_upwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def downward_direction(self) -> Direction3d:
        """Get the downward direction of a orientation."""
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_downwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def front_plane_orientation(self) -> PlaneOrientation3d:
        """Construct a forward-facing plane orientation from a parent orientation.

        Relative to the parent orientation,
        the normal direction of the plane orientation will point forward,
        the X direction of the plane orientation will point leftward,
        and the Y direction of the plane orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_frontPlaneOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def back_plane_orientation(self) -> PlaneOrientation3d:
        """Construct a backward-facing plane orientation from a parent orientation.

        Relative to the parent orientation,
        the normal direction of the plane orientation will point backward,
        the X direction of the plane orientation will point rightward,
        and the Y direction of the plane orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_backPlaneOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def right_plane_orientation(self) -> PlaneOrientation3d:
        """Construct a rightward-facing plane orientation from a parent orientation.

        Relative to the parent orientation,
        the normal direction of the plane orientation will point rightward,
        the X direction of the plane orientation will point forward,
        and the Y direction of the plane orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_rightPlaneOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def left_plane_orientation(self) -> PlaneOrientation3d:
        """Construct a leftward-facing plane orientation from a parent orientation.

        Relative to the parent orientation,
        the normal direction of the plane orientation will point leftward,
        the X direction of the plane orientation will point backward,
        and the Y direction of the plane orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_leftPlaneOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def bottom_plane_orientation(self) -> PlaneOrientation3d:
        """Construct a downward-facing plane orientation from a parent orientation.

        Relative to the parent orientation,
        the normal direction of the plane orientation will point downward,
        the X direction of the plane orientation will point leftward,
        and the Y direction of the plane orientation will point forward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_bottomPlaneOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def top_plane_orientation(self) -> PlaneOrientation3d:
        """Construct a upward-facing plane orientation from a parent orientation.

        Relative to the parent orientation,
        the normal direction of the plane orientation will point upward,
        the X direction of the plane orientation will point rightward,
        and the Y direction of the plane orientation will point forward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_topPlaneOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PlaneOrientation3d._new(output)

    @cached_property
    def backward_orientation(self) -> Orientation3d:
        """Construct a backward facing orientation relative to a parent/reference orientation.

        Relative to the parent orientation,
        the forward direction of the orientation will point backward,
        the rightward direction of the orientation will point leftward,
        and the upward direction of the orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_backwardOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)

    @cached_property
    def rightward_orientation(self) -> Orientation3d:
        """Construct a rightward facing orientation relative to a parent/reference orientation.

        Relative to the parent orientation,
        the forward direction of the orientation will point rightward,
        the rightward direction of the orientation will point backward,
        and the upward direction of the orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_rightwardOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)

    @cached_property
    def leftward_orientation(self) -> Orientation3d:
        """Construct a leftward facing orientation relative to a parent/reference orientation.

        Relative to the parent orientation,
        the forward direction of the orientation will point leftward,
        the rightward direction of the orientation will point forward,
        and the upward direction of the orientation will point upward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_leftwardOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)

    @cached_property
    def upward_orientation(self) -> Orientation3d:
        """Construct an upward facing orientation relative to a parent/reference orientation.

        Relative to the parent orientation,
        the forward direction of the orientation will point upward,
        the rightward direction of the orientation will point leftward,
        and the upward direction of the orientation will point forward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_upwardOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)

    @cached_property
    def downward_orientation(self) -> Orientation3d:
        """Construct a downward facing orientation relative to a parent/reference orientation.

        Relative to the parent orientation,
        the forward direction of the orientation will point downward,
        the rightward direction of the orientation will point rightward,
        and the upward direction of the orientation will point forward.
        """
        inputs = self._orientation3d_ptr
        output = c_void_p()
        _lib.opensolid_Orientation3d_downwardOrientation(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)

    def place_in(self, frame: Frame3d) -> Orientation3d:
        """Convert a orientation defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._orientation3d_ptr)
        output = c_void_p()
        _lib.opensolid_Orientation3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)

    def relative_to(self, frame: Frame3d) -> Orientation3d:
        """Convert a orientation defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._orientation3d_ptr)
        output = c_void_p()
        _lib.opensolid_Orientation3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Orientation3d._new(output)


def _orientation3d_world() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_Orientation3d_world(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


Orientation3d.world = _orientation3d_world()


class Frame3d:
    """A frame of reference in 3D, defined by an origin point and orientation."""

    _frame3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Frame3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Frame3d)
        obj._frame3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._frame3d_ptr)

    world: Frame3d = None  # type: ignore[assignment]
    """A frame of reference defining a global coordinate system."""

    @staticmethod
    def from_front_plane(plane: Plane3d) -> Frame3d:
        """Construct a plane from its front plane."""
        inputs = plane._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_fromFrontPlane_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def from_back_plane(plane: Plane3d) -> Frame3d:
        """Construct a plane from its back plane."""
        inputs = plane._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_fromBackPlane_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def from_right_plane(plane: Plane3d) -> Frame3d:
        """Construct a plane from its right plane."""
        inputs = plane._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_fromRightPlane_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def from_left_plane(plane: Plane3d) -> Frame3d:
        """Construct a plane from its left plane."""
        inputs = plane._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_fromLeftPlane_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def from_top_plane(plane: Plane3d) -> Frame3d:
        """Construct a plane from its top plane."""
        inputs = plane._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_fromTopPlane_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def from_bottom_plane(plane: Plane3d) -> Frame3d:
        """Construct a plane from its bottom plane."""
        inputs = plane._plane3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_fromBottomPlane_Plane3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def align(frame: Frame3d, reference_frame: Frame3d) -> Frame3d:
        """Compute the relative orientation of two parent frames in order to align two child frames.

        Imagine you have one object defined in coordinate system A ("local"),
        with a particular frame X defined in coordinate system A.
        Similarly, you have another object defined in coordinate system B ("global"),
        with a particular frame Y defined in coordinate system B.
        This function lets you determine the necessary relative alignment between A and B
        such that the two frames X and Y are aligned with each other.
        Given the two frames X and Y, this function returns a new frame
        that defines the necessary orientation of A ("local") relative to B ("global").
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            frame._frame3d_ptr, reference_frame._frame3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Frame3d_align_Frame3d_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @staticmethod
    def mate(frame: Frame3d, reference_frame: Frame3d) -> Frame3d:
        """Compute the relative orientation of two parent frames in order to "mate" two child frames.

        This is the same as 'align' except that the two child frames will end up facing towards each other
        (with reversed forward directions, but the same upward directions)
        instead of being aligned with each other.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            frame._frame3d_ptr, reference_frame._frame3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Frame3d_mate_Frame3d_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @cached_property
    def origin_point(self) -> Point3d:
        """Get the origin point of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_originPoint(ctypes.byref(inputs), ctypes.byref(output))
        return Point3d._new(output)

    @cached_property
    def forward_direction(self) -> Direction3d:
        """Get the local forward direction of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_forwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def backward_direction(self) -> Direction3d:
        """Get the local backward direction of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_backwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def rightward_direction(self) -> Direction3d:
        """Get the local rightward direction of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_rightwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def leftward_direction(self) -> Direction3d:
        """Get the local leftward direction of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_leftwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def upward_direction(self) -> Direction3d:
        """Get the local upward direction of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_upwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def downward_direction(self) -> Direction3d:
        """Get the local downward direction of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_downwardDirection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Direction3d._new(output)

    @cached_property
    def forward_axis(self) -> Axis3d:
        """Get the forward axis of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_forwardAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def backward_axis(self) -> Axis3d:
        """Get the backward axis of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_backwardAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def rightward_axis(self) -> Axis3d:
        """Get the rightward axis of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_rightwardAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def leftward_axis(self) -> Axis3d:
        """Get the leftward axis of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_leftwardAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def upward_axis(self) -> Axis3d:
        """Get the upward axis of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_upwardAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def downward_axis(self) -> Axis3d:
        """Get the downward axis of a frame."""
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_downwardAxis(ctypes.byref(inputs), ctypes.byref(output))
        return Axis3d._new(output)

    @cached_property
    def front_plane(self) -> Plane3d:
        """Construct a locally forward-facing plane from a frame.

        The returned plane will have the same origin point as the frame,
        its normal direction will be the frame's forward direction,
        its X direction will be the frame's leftward direction
        and its Y direction will be frame's upward direction.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_frontPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    @cached_property
    def back_plane(self) -> Plane3d:
        """Construct a locally backward-facing plane from a frame.

        The returned plane will have the same origin point as the frame,
        its normal direction will be the frame's backward direction,
        its X direction will be the frame's rightward direction
        and its Y direction will be frame's upward direction.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_backPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    @cached_property
    def right_plane(self) -> Plane3d:
        """Construct a locally rightward-facing plane from a frame.

        The returned plane will have the same origin point as the frame,
        its normal direction will be the frame's rightward direction,
        its X direction will be the frame's forward direction
        and its Y direction will be frame's upward direction.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_rightPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    @cached_property
    def left_plane(self) -> Plane3d:
        """Construct a locally leftward-facing plane from a frame.

        The returned plane will have the same origin point as the frame,
        its normal direction will be the frame's leftward direction,
        its X direction will be the frame's backward direction
        and its Y direction will be frame's upward direction.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_leftPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    @cached_property
    def top_plane(self) -> Plane3d:
        """Construct a locally upward-facing plane from a frame.

        The returned plane will have the same origin point as the frame,
        its normal direction will be the frame's upward direction,
        its X direction will be the frame's rightward direction
        and its Y direction will be frame's forward direction.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_topPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    @cached_property
    def bottom_plane(self) -> Plane3d:
        """Construct a locally downward-facing plane from a frame.

        The returned plane will have the same origin point as the frame,
        its normal direction will be the frame's downward direction,
        its X direction will be the frame's leftward direction
        and its Y direction will be frame's forward direction.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_bottomPlane(ctypes.byref(inputs), ctypes.byref(output))
        return Plane3d._new(output)

    @cached_property
    def backward_frame(self) -> Frame3d:
        """Construct a backward-facing frame relative to a parent/reference frame.

        The forward direction of the frame will point backward,
        the upward direction of the frame will point upward,
        and the rightward direction of the frame will point leftward
        (all relative to the parent frame).
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_backwardFrame(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    @cached_property
    def leftward_frame(self) -> Frame3d:
        """Construct a leftward-facing frame relative to a parent/reference frame.

        The forward direction of the frame will point leftward,
        the upward direction of the frame will point upward,
        and the rightward direction of the frame will point forward
        (all relative to the parent frame).
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_leftwardFrame(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    @cached_property
    def rightward_frame(self) -> Frame3d:
        """Construct a rightward-facing frame relative to a parent/reference frame.

        The forward direction of the frame will point rightward,
        the upward direction of the frame will point upward,
        and the rightward direction of the frame will point backward
        (all relative to the parent frame).
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_rightwardFrame(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    @cached_property
    def upward_frame(self) -> Frame3d:
        """Construct an upward-facing frame relative to a parent/reference frame.

        The forward direction of the frame will point upward,
        the upward direction of the frame will point forward,
        and the rightward direction of the frame will point leftward
        (all relative to the parent frame).
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_upwardFrame(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    @cached_property
    def downward_frame(self) -> Frame3d:
        """Construct a downward-facing frame relative to a parent/reference frame.

        The forward direction of the frame will point downward,
        the upward direction of the frame will point upward,
        and the rightward direction of the frame will point rightward
        (all relative to the parent frame).
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_downwardFrame(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def place_in(self, other_frame: Frame3d) -> Frame3d:
        """Convert a frame defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(other_frame._frame3d_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def relative_to(self, other_frame: Frame3d) -> Frame3d:
        """Convert a frame defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(other_frame._frame3d_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def inverse(self) -> Frame3d:
        """Compute the "inverse" of a given frame.

        This is a frame that defines the current global coordinate system
        in terms of the frame's local coordinate system,
        instead of the other way around.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_inverse(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def move_to(self, point: Point3d) -> Frame3d:
        """Move a frame to a new origin point."""
        inputs = _Tuple2_c_void_p_c_void_p(point._point3d_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_moveTo_Point3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def offset_forward_by(self, distance: Length) -> Frame3d:
        """Move a frame in its own forward direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_offsetForwardBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def offset_backward_by(self, distance: Length) -> Frame3d:
        """Move a frame in its own backward direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_offsetBackwardBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def offset_rightward_by(self, distance: Length) -> Frame3d:
        """Move a frame in its own rightward direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_offsetRightwardBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def offset_leftward_by(self, distance: Length) -> Frame3d:
        """Move a frame in its own leftward direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_offsetLeftwardBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def offset_upward_by(self, distance: Length) -> Frame3d:
        """Move a frame in its own upward direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_offsetUpwardBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def offset_downward_by(self, distance: Length) -> Frame3d:
        """Move a frame in its own downward direction by the given distance."""
        inputs = _Tuple2_c_void_p_c_void_p(distance._length_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_offsetDownwardBy_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def turn_right_by(self, angle: Angle) -> Frame3d:
        """Rotate a frame clockwise around its own upward axis by the given angle.

        This rotates the frame's forward direction toward its rightward direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_turnRightBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def turn_left_by(self, angle: Angle) -> Frame3d:
        """Rotate a frame counterclockwise around its own upward axis by the given angle.

        This rotates the frame's forward direction toward its leftward direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_turnLeftBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def roll_right_by(self, angle: Angle) -> Frame3d:
        """Rotate a frame counterclockwise around its own forward axis by the given angle.

        This rotates the frame's upward direction toward its rightward direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_rollRightBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def roll_left_by(self, angle: Angle) -> Frame3d:
        """Rotate a frame clockwise around its own forward axis by the given angle.

        This rotates the frame's upward direction toward its leftward direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_rollLeftBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def tilt_up_by(self, angle: Angle) -> Frame3d:
        """Rotate a frame counterclockwise around its own rightward axis by the given angle.

        This rotates the frame's forward direction toward its upward direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_tiltUpBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def tilt_down_by(self, angle: Angle) -> Frame3d:
        """Rotate a frame clockwise around its own rightward axis by the given angle.

        This rotates the frame's forward direction toward its downward direction.
        """
        inputs = _Tuple2_c_void_p_c_void_p(angle._angle_ptr, self._frame3d_ptr)
        output = c_void_p()
        _lib.opensolid_Frame3d_tiltDownBy_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def turn_right(self) -> Frame3d:
        """Turn a frame right by 90 degrees.

        The forward direction of the returned frame
        will be equal to the rightward direction of the original frame.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_turnRight(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def turn_left(self) -> Frame3d:
        """Turn a frame left by 90 degrees.

        The forward direction of the returned frame
        will be equal to the leftward direction of the original frame.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_turnLeft(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def roll_right(self) -> Frame3d:
        """Roll a frame right by 90 degrees.

        The upward direction of the returned frame
        will be equal to the rightward direction of the original frame.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_rollRight(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def roll_left(self) -> Frame3d:
        """Roll a frame left by 90 degrees.

        The upward direction of the returned frame
        will be equal to the leftward direction of the original frame.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_rollLeft(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def tilt_up(self) -> Frame3d:
        """Tilt a frame up by 90 degrees.

        The forward direction of the returned frame
        will be equal to the upward direction of the original frame.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_tiltUp(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def tilt_down(self) -> Frame3d:
        """Tilt a frame down by 90 degrees.

        The forward direction of the returned frame
        will be equal to the downward direction of the original frame.
        """
        inputs = self._frame3d_ptr
        output = c_void_p()
        _lib.opensolid_Frame3d_tiltDown(ctypes.byref(inputs), ctypes.byref(output))
        return Frame3d._new(output)

    def translate_by(self, displacement: Displacement3d) -> Frame3d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement3d_ptr, self._frame3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Frame3d_translateBy_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def translate_in(self, direction: Direction3d, distance: Length) -> Frame3d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, distance._length_ptr, self._frame3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Frame3d_translateIn_Direction3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def translate_along(self, axis: Axis3d, distance: Length) -> Frame3d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, distance._length_ptr, self._frame3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Frame3d_translateAlong_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Frame3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._frame3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Frame3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Frame3d._new(output)


def _frame3d_world() -> Frame3d:
    output = c_void_p()
    _lib.opensolid_Frame3d_world(c_void_p(), ctypes.byref(output))
    return Frame3d._new(output)


Frame3d.world = _frame3d_world()


class World3d:
    """A collection of global datums."""

    _world3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> World3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(World3d)
        obj._world3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._world3d_ptr)

    origin_point: Point3d = None  # type: ignore[assignment]
    """The global origin point of a coordinate system."""

    forward_direction: Direction3d = None  # type: ignore[assignment]
    """The global forward direction of a coordinate system."""

    backward_direction: Direction3d = None  # type: ignore[assignment]
    """The global backward direction of a coordinate system."""

    leftward_direction: Direction3d = None  # type: ignore[assignment]
    """The global leftward direction of a coordinate system."""

    rightward_direction: Direction3d = None  # type: ignore[assignment]
    """The global rightward direction of a coordinate system."""

    upward_direction: Direction3d = None  # type: ignore[assignment]
    """The global upward direction of a coordinate system."""

    downward_direction: Direction3d = None  # type: ignore[assignment]
    """The global downward direction of a coordinate system."""

    forward_orientation: Orientation3d = None  # type: ignore[assignment]
    """The forward-facing or 'default' orientation of the global coordinate system.

    The directions of this orientation will match the global directions:
    the forward direction will point forward,
    the rightward direction will point rightward,
    and the upward direction will point upward.
    """

    backward_orientation: Orientation3d = None  # type: ignore[assignment]
    """The backward-facing orientation of the global coordinate system.

    The forward direction of the orientation will point backward,
    the rightward direction of the orientation will point leftward,
    and the upward direction of the orientation will point upward.
    """

    leftward_orientation: Orientation3d = None  # type: ignore[assignment]
    """The leftward-facing orientation of the global coordinate system.

    The forward direction of the orientation will point leftward,
    the rightward direction of the orientation will point forward,
    and the upward direction of the orientation will point upward.
    """

    rightward_orientation: Orientation3d = None  # type: ignore[assignment]
    """The rightward-facing orientation of the global coordinate system.

    The forward direction of the orientation will point rightward,
    the rightward direction of the orientation will point backward,
    and the upward direction of the orientation will point upward.
    """

    upward_orientation: Orientation3d = None  # type: ignore[assignment]
    """The upward-facing orientation of the global coordinate system.

    The forward direction of the orientation will point upward,
    the rightward direction of the orientation will point leftward,
    and the upward direction of the orientation will point forward.
    """

    downward_orientation: Orientation3d = None  # type: ignore[assignment]
    """The downward-facing orientation of the global coordinate system.

    The forward direction of the orientation will point downward,
    the rightward direction of the orientation will point rightward,
    and the upward direction of the orientation will point forward.
    """

    frame: Frame3d = None  # type: ignore[assignment]
    """A frame of reference defining a global coordinate system."""

    forward_axis: Axis3d = None  # type: ignore[assignment]
    """A forward-facing axis through the global origin point."""

    backward_axis: Axis3d = None  # type: ignore[assignment]
    """A backward-facing axis through the global origin point."""

    leftward_axis: Axis3d = None  # type: ignore[assignment]
    """A leftward-facing axis through the global origin point."""

    rightward_axis: Axis3d = None  # type: ignore[assignment]
    """A rightward-facing axis through the global origin point."""

    upward_axis: Axis3d = None  # type: ignore[assignment]
    """An upward-facing axis through the global origin point."""

    downward_axis: Axis3d = None  # type: ignore[assignment]
    """A downward-facing axis through the global origin point."""

    front_plane: Plane3d = None  # type: ignore[assignment]
    """A forward-facing plane through the global origin point.

    The X direction of the plane will be the global leftward direction,
    and the Y direction of the plane will be the global upward direction.
    """

    back_plane: Plane3d = None  # type: ignore[assignment]
    """A backward-facing plane through the global origin point.

    The X direction of the plane will be the global rightward direction,
    and the Y direction of the plane will be the global upward direction.
    """

    left_plane: Plane3d = None  # type: ignore[assignment]
    """A leftward-facing plane through the global origin point.

    The X direction of the plane will be the global backward direction,
    and the Y direction of the plane will be the global upward direction.
    """

    right_plane: Plane3d = None  # type: ignore[assignment]
    """A rightward-facing plane through the global origin point.

    The X direction of the plane will be the global forward direction,
    and the Y direction of the plane will be the global upward direction.
    """

    top_plane: Plane3d = None  # type: ignore[assignment]
    """An upward-facing plane through the global origin point.

    The X direction of the plane will be the global rightward direction,
    and the Y direction of the plane will be the global forward direction.
    """

    bottom_plane: Plane3d = None  # type: ignore[assignment]
    """An downward-facing plane through the global origin point.

    The X direction of the plane will be the global leftward direction,
    and the Y direction of the plane will be the global forward direction.
    """


def _world3d_origin_point() -> Point3d:
    output = c_void_p()
    _lib.opensolid_World3d_originPoint(c_void_p(), ctypes.byref(output))
    return Point3d._new(output)


World3d.origin_point = _world3d_origin_point()


def _world3d_forward_direction() -> Direction3d:
    output = c_void_p()
    _lib.opensolid_World3d_forwardDirection(c_void_p(), ctypes.byref(output))
    return Direction3d._new(output)


World3d.forward_direction = _world3d_forward_direction()


def _world3d_backward_direction() -> Direction3d:
    output = c_void_p()
    _lib.opensolid_World3d_backwardDirection(c_void_p(), ctypes.byref(output))
    return Direction3d._new(output)


World3d.backward_direction = _world3d_backward_direction()


def _world3d_leftward_direction() -> Direction3d:
    output = c_void_p()
    _lib.opensolid_World3d_leftwardDirection(c_void_p(), ctypes.byref(output))
    return Direction3d._new(output)


World3d.leftward_direction = _world3d_leftward_direction()


def _world3d_rightward_direction() -> Direction3d:
    output = c_void_p()
    _lib.opensolid_World3d_rightwardDirection(c_void_p(), ctypes.byref(output))
    return Direction3d._new(output)


World3d.rightward_direction = _world3d_rightward_direction()


def _world3d_upward_direction() -> Direction3d:
    output = c_void_p()
    _lib.opensolid_World3d_upwardDirection(c_void_p(), ctypes.byref(output))
    return Direction3d._new(output)


World3d.upward_direction = _world3d_upward_direction()


def _world3d_downward_direction() -> Direction3d:
    output = c_void_p()
    _lib.opensolid_World3d_downwardDirection(c_void_p(), ctypes.byref(output))
    return Direction3d._new(output)


World3d.downward_direction = _world3d_downward_direction()


def _world3d_forward_orientation() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_World3d_forwardOrientation(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


World3d.forward_orientation = _world3d_forward_orientation()


def _world3d_backward_orientation() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_World3d_backwardOrientation(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


World3d.backward_orientation = _world3d_backward_orientation()


def _world3d_leftward_orientation() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_World3d_leftwardOrientation(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


World3d.leftward_orientation = _world3d_leftward_orientation()


def _world3d_rightward_orientation() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_World3d_rightwardOrientation(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


World3d.rightward_orientation = _world3d_rightward_orientation()


def _world3d_upward_orientation() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_World3d_upwardOrientation(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


World3d.upward_orientation = _world3d_upward_orientation()


def _world3d_downward_orientation() -> Orientation3d:
    output = c_void_p()
    _lib.opensolid_World3d_downwardOrientation(c_void_p(), ctypes.byref(output))
    return Orientation3d._new(output)


World3d.downward_orientation = _world3d_downward_orientation()


def _world3d_frame() -> Frame3d:
    output = c_void_p()
    _lib.opensolid_World3d_frame(c_void_p(), ctypes.byref(output))
    return Frame3d._new(output)


World3d.frame = _world3d_frame()


def _world3d_forward_axis() -> Axis3d:
    output = c_void_p()
    _lib.opensolid_World3d_forwardAxis(c_void_p(), ctypes.byref(output))
    return Axis3d._new(output)


World3d.forward_axis = _world3d_forward_axis()


def _world3d_backward_axis() -> Axis3d:
    output = c_void_p()
    _lib.opensolid_World3d_backwardAxis(c_void_p(), ctypes.byref(output))
    return Axis3d._new(output)


World3d.backward_axis = _world3d_backward_axis()


def _world3d_leftward_axis() -> Axis3d:
    output = c_void_p()
    _lib.opensolid_World3d_leftwardAxis(c_void_p(), ctypes.byref(output))
    return Axis3d._new(output)


World3d.leftward_axis = _world3d_leftward_axis()


def _world3d_rightward_axis() -> Axis3d:
    output = c_void_p()
    _lib.opensolid_World3d_rightwardAxis(c_void_p(), ctypes.byref(output))
    return Axis3d._new(output)


World3d.rightward_axis = _world3d_rightward_axis()


def _world3d_upward_axis() -> Axis3d:
    output = c_void_p()
    _lib.opensolid_World3d_upwardAxis(c_void_p(), ctypes.byref(output))
    return Axis3d._new(output)


World3d.upward_axis = _world3d_upward_axis()


def _world3d_downward_axis() -> Axis3d:
    output = c_void_p()
    _lib.opensolid_World3d_downwardAxis(c_void_p(), ctypes.byref(output))
    return Axis3d._new(output)


World3d.downward_axis = _world3d_downward_axis()


def _world3d_front_plane() -> Plane3d:
    output = c_void_p()
    _lib.opensolid_World3d_frontPlane(c_void_p(), ctypes.byref(output))
    return Plane3d._new(output)


World3d.front_plane = _world3d_front_plane()


def _world3d_back_plane() -> Plane3d:
    output = c_void_p()
    _lib.opensolid_World3d_backPlane(c_void_p(), ctypes.byref(output))
    return Plane3d._new(output)


World3d.back_plane = _world3d_back_plane()


def _world3d_left_plane() -> Plane3d:
    output = c_void_p()
    _lib.opensolid_World3d_leftPlane(c_void_p(), ctypes.byref(output))
    return Plane3d._new(output)


World3d.left_plane = _world3d_left_plane()


def _world3d_right_plane() -> Plane3d:
    output = c_void_p()
    _lib.opensolid_World3d_rightPlane(c_void_p(), ctypes.byref(output))
    return Plane3d._new(output)


World3d.right_plane = _world3d_right_plane()


def _world3d_top_plane() -> Plane3d:
    output = c_void_p()
    _lib.opensolid_World3d_topPlane(c_void_p(), ctypes.byref(output))
    return Plane3d._new(output)


World3d.top_plane = _world3d_top_plane()


def _world3d_bottom_plane() -> Plane3d:
    output = c_void_p()
    _lib.opensolid_World3d_bottomPlane(c_void_p(), ctypes.byref(output))
    return Plane3d._new(output)


World3d.bottom_plane = _world3d_bottom_plane()


class VectorCurve2d:
    """A parametric curve defining a 2D unitless vector in terms of a parameter value."""

    _vectorcurve2d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> VectorCurve2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(VectorCurve2d)
        obj._vectorcurve2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._vectorcurve2d_ptr)

    zero: VectorCurve2d = None  # type: ignore[assignment]
    """The constant zero vector."""

    @staticmethod
    def constant(value: Vector2d) -> VectorCurve2d:
        """Create a curve with a constant value."""
        inputs = value._vector2d_ptr
        output = c_void_p()
        _lib.opensolid_VectorCurve2d_constant_Vector2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return VectorCurve2d._new(output)

    @staticmethod
    def xy(x_component: Curve, y_component: Curve) -> VectorCurve2d:
        """Create a curve from its X and Y component curves."""
        inputs = _Tuple2_c_void_p_c_void_p(
            x_component._curve_ptr, y_component._curve_ptr
        )
        output = c_void_p()
        _lib.opensolid_VectorCurve2d_xy_Curve_Curve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return VectorCurve2d._new(output)

    def evaluate(self, parameter_value: float) -> Vector2d:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._vectorcurve2d_ptr)
        output = c_void_p()
        _lib.opensolid_VectorCurve2d_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Vector2d._new(output)


def _vectorcurve2d_zero() -> VectorCurve2d:
    output = c_void_p()
    _lib.opensolid_VectorCurve2d_zero(c_void_p(), ctypes.byref(output))
    return VectorCurve2d._new(output)


VectorCurve2d.zero = _vectorcurve2d_zero()


class DisplacementCurve2d:
    """A parametric curve defining a 2D displacement vector in terms of a parameter value."""

    _displacementcurve2d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> DisplacementCurve2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(DisplacementCurve2d)
        obj._displacementcurve2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._displacementcurve2d_ptr)

    zero: DisplacementCurve2d = None  # type: ignore[assignment]
    """The constant zero vector."""

    @staticmethod
    def constant(value: Displacement2d) -> DisplacementCurve2d:
        """Create a curve with a constant value."""
        inputs = value._displacement2d_ptr
        output = c_void_p()
        _lib.opensolid_DisplacementCurve2d_constant_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return DisplacementCurve2d._new(output)

    @staticmethod
    def xy(x_component: LengthCurve, y_component: LengthCurve) -> DisplacementCurve2d:
        """Create a curve from its X and Y component curves."""
        inputs = _Tuple2_c_void_p_c_void_p(
            x_component._lengthcurve_ptr, y_component._lengthcurve_ptr
        )
        output = c_void_p()
        _lib.opensolid_DisplacementCurve2d_xy_LengthCurve_LengthCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return DisplacementCurve2d._new(output)

    def evaluate(self, parameter_value: float) -> Displacement2d:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(
            parameter_value, self._displacementcurve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_DisplacementCurve2d_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Displacement2d._new(output)


def _displacementcurve2d_zero() -> DisplacementCurve2d:
    output = c_void_p()
    _lib.opensolid_DisplacementCurve2d_zero(c_void_p(), ctypes.byref(output))
    return DisplacementCurve2d._new(output)


DisplacementCurve2d.zero = _displacementcurve2d_zero()


class UvVectorCurve:
    """A parametric vector curve in UV parameter space."""

    _uvvectorcurve_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> UvVectorCurve:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvVectorCurve)
        obj._uvvectorcurve_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvvectorcurve_ptr)

    zero: UvVectorCurve = None  # type: ignore[assignment]
    """The constant zero vector."""

    @staticmethod
    def constant(value: UvVector) -> UvVectorCurve:
        """Create a curve with a constant value."""
        inputs = value._uvvector_ptr
        output = c_void_p()
        _lib.opensolid_UvVectorCurve_constant_UvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVectorCurve._new(output)

    @staticmethod
    def uv(u_component: Curve, v_component: Curve) -> UvVectorCurve:
        """Construct a UV vector curve from its U and V components."""
        inputs = _Tuple2_c_void_p_c_void_p(
            u_component._curve_ptr, v_component._curve_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvVectorCurve_uv_Curve_Curve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVectorCurve._new(output)

    def evaluate(self, parameter_value: float) -> UvVector:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._uvvectorcurve_ptr)
        output = c_void_p()
        _lib.opensolid_UvVectorCurve_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvVector._new(output)


def _uvvectorcurve_zero() -> UvVectorCurve:
    output = c_void_p()
    _lib.opensolid_UvVectorCurve_zero(c_void_p(), ctypes.byref(output))
    return UvVectorCurve._new(output)


UvVectorCurve.zero = _uvvectorcurve_zero()


class Curve2d:
    """A parametric curve in 2D space."""

    _curve2d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Curve2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Curve2d)
        obj._curve2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._curve2d_ptr)

    @staticmethod
    def constant(point: Point2d) -> Curve2d:
        """Create a degenerate curve that is actually just a single point."""
        inputs = point._point2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_constant_Point2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def xy(x_coordinate: LengthCurve, y_coordinate: LengthCurve) -> Curve2d:
        """Create a curve from its X and Y coordinate curves."""
        inputs = _Tuple2_c_void_p_c_void_p(
            x_coordinate._lengthcurve_ptr, y_coordinate._lengthcurve_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_xy_LengthCurve_LengthCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def line(start_point: Point2d, end_point: Point2d) -> Curve2d:
        """Create a line between two points."""
        inputs = _Tuple2_c_void_p_c_void_p(
            start_point._point2d_ptr, end_point._point2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_line_Point2d_Point2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def arc(start_point: Point2d, end_point: Point2d, swept_angle: Angle) -> Curve2d:
        """Create an arc with the given start point, end point and swept angle.

        A positive swept angle means the arc turns counterclockwise (turns to the left),
        and a negative swept angle means it turns clockwise (turns to the right).
        For example, an arc with a swept angle of positive 90 degrees
        is quarter circle that turns to the left.
        """
        inputs = _Tuple4_c_void_p_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            start_point._point2d_ptr,
            end_point._point2d_ptr,
            swept_angle._angle_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_arc_Point2d_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def polar_arc(
        *, center_point: Point2d, radius: Length, start_angle: Angle, end_angle: Angle
    ) -> Curve2d:
        """Create an arc with the given center point, radius, start angle and end angle."""
        inputs = _Tuple4_c_void_p_c_void_p_c_void_p_c_void_p(
            center_point._point2d_ptr,
            radius._length_ptr,
            start_angle._angle_ptr,
            end_angle._angle_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_polarArc_Point2d_Length_Angle_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def swept_arc(
        center_point: Point2d, start_point: Point2d, swept_angle: Angle
    ) -> Curve2d:
        """Create an arc with the given center point, start point and swept angle.

        The start point will be swept around the center point by the given angle.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            center_point._point2d_ptr, start_point._point2d_ptr, swept_angle._angle_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_sweptArc_Point2d_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def corner_arc(
        corner_point: Point2d,
        *,
        incoming: Direction2d,
        outgoing: Direction2d,
        radius: Length,
    ) -> Curve2d:
        """Create an arc for rounding off the corner between two straight lines."""
        inputs = _Tuple5_c_void_p_c_void_p_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            corner_point._point2d_ptr,
            incoming._direction2d_ptr,
            outgoing._direction2d_ptr,
            radius._length_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_cornerArc_Point2d_Direction2d_Direction2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def circle(*, center_point: Point2d, diameter: Length) -> Curve2d:
        """Create a circle with the given center point and diameter."""
        inputs = _Tuple2_c_void_p_c_void_p(
            center_point._point2d_ptr, diameter._length_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_circle_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def bezier(control_points: list[Point2d]) -> Curve2d:
        """Construct a Bezier curve from its control points.

        For example,

        > Curve2d.bezier (NonEmpty.four p1 p2 p3 p4))

        will return a cubic Bezier curve with the given four control points.
        """
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(control_points))(
                    *[item._point2d_ptr for item in control_points]
                ),
            )
            if control_points
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_bezier_NonEmptyPoint2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @staticmethod
    def hermite(
        start_point: Point2d,
        start_derivatives: list[Displacement2d],
        end_point: Point2d,
        end_derivatives: list[Displacement2d],
    ) -> Curve2d:
        """Construct a Bezier curve with the given endpoints and derivatives at those endpoints.

        For example,

        > Curve2d.hermite p1 [v1] p2 [v2]

        will result in a cubic spline from @p1@ to @p2@ with first derivative equal to @v1@ at @p1@ and
        first derivative equal to @v2@ at @p2@.

        The numbers of derivatives at each endpoint do not have to be equal; for example,

        > Curve2d.hermite p1 [v1] p2 []

        will result in a quadratic spline from @p1@ to @p2@ with first derivative at @p1@ equal to @v1@.

        In general, the degree of the resulting spline will be equal to 1 plus the total number of
        derivatives given.
        """
        inputs = _Tuple4_c_void_p_List_c_void_p_c_void_p_List_c_void_p(
            start_point._point2d_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(start_derivatives))(
                    *[item._displacement2d_ptr for item in start_derivatives]
                ),
            ),
            end_point._point2d_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(end_derivatives))(
                    *[item._displacement2d_ptr for item in end_derivatives]
                ),
            ),
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_hermite_Point2d_ListDisplacement2d_Point2d_ListDisplacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @cached_property
    def start_point(self) -> Point2d:
        """The start point of the curve."""
        inputs = self._curve2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_startPoint(ctypes.byref(inputs), ctypes.byref(output))
        return Point2d._new(output)

    @cached_property
    def end_point(self) -> Point2d:
        """The end point of the curve."""
        inputs = self._curve2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_endPoint(ctypes.byref(inputs), ctypes.byref(output))
        return Point2d._new(output)

    @cached_property
    def derivative(self) -> DisplacementCurve2d:
        """The derivative of the curve."""
        inputs = self._curve2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_derivative(ctypes.byref(inputs), ctypes.byref(output))
        return DisplacementCurve2d._new(output)

    @cached_property
    def x_coordinate(self) -> LengthCurve:
        """Get the X coordinate of a 2D curve as a scalar curve."""
        inputs = self._curve2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_xCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return LengthCurve._new(output)

    @cached_property
    def y_coordinate(self) -> LengthCurve:
        """Get the Y coordinate of a 2D curve as a scalar curve."""
        inputs = self._curve2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_yCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return LengthCurve._new(output)

    def evaluate(self, parameter_value: float) -> Point2d:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._curve2d_ptr)
        output = c_void_p()
        _lib.opensolid_Curve2d_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Point2d._new(output)

    def reverse(self) -> Curve2d:
        """Reverse a curve, so that the start point is the end point and vice versa."""
        inputs = self._curve2d_ptr
        output = c_void_p()
        _lib.opensolid_Curve2d_reverse(ctypes.byref(inputs), ctypes.byref(output))
        return Curve2d._new(output)

    def scale_along(self, axis: Axis2d, scale: float) -> Curve2d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis2d_ptr, scale, self._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_scaleAlong_Axis2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def scale_about(self, point: Point2d, scale: float) -> Curve2d:
        """Scale uniformly about the given point by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            point._point2d_ptr, scale, self._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_scaleAbout_Point2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Curve2d:
        """Mirror across the given axis."""
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._curve2d_ptr)
        output = c_void_p()
        _lib.opensolid_Curve2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def translate_by(self, displacement: Displacement2d) -> Curve2d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement2d_ptr, self._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_translateBy_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def translate_in(self, direction: Direction2d, distance: Length) -> Curve2d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction2d_ptr, distance._length_ptr, self._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_translateIn_Direction2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def translate_along(self, axis: Axis2d, distance: Length) -> Curve2d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis2d_ptr, distance._length_ptr, self._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_translateAlong_Axis2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def rotate_around(self, point: Point2d, angle: Angle) -> Curve2d:
        """Rotate around the given point by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            point._point2d_ptr, angle._angle_ptr, self._curve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_rotateAround_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    def __add__(self, rhs: DisplacementCurve2d) -> Curve2d:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(
            self._curve2d_ptr, rhs._displacementcurve2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Curve2d_add_Curve2d_DisplacementCurve2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Curve2d._new(output)

    @overload
    def __sub__(self, rhs: DisplacementCurve2d) -> Curve2d:
        pass

    @overload
    def __sub__(self, rhs: Curve2d) -> DisplacementCurve2d:
        pass

    @overload
    def __sub__(self, rhs: Point2d) -> DisplacementCurve2d:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case DisplacementCurve2d():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._curve2d_ptr, rhs._displacementcurve2d_ptr
                )
                output = c_void_p()
                _lib.opensolid_Curve2d_sub_Curve2d_DisplacementCurve2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return Curve2d._new(output)
            case Curve2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve2d_ptr, rhs._curve2d_ptr)
                output = c_void_p()
                _lib.opensolid_Curve2d_sub_Curve2d_Curve2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return DisplacementCurve2d._new(output)
            case Point2d():
                inputs = _Tuple2_c_void_p_c_void_p(self._curve2d_ptr, rhs._point2d_ptr)
                output = c_void_p()
                _lib.opensolid_Curve2d_sub_Curve2d_Point2d(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return DisplacementCurve2d._new(output)
            case _:
                return NotImplemented


class UvCurve:
    """A curve in UV parameter space."""

    _uvcurve_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> UvCurve:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvCurve)
        obj._uvcurve_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvcurve_ptr)

    @staticmethod
    def constant(point: UvPoint) -> UvCurve:
        """Create a degenerate curve that is actually just a single point."""
        inputs = point._uvpoint_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_constant_UvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def uv(u_coordinate: Curve, v_coordinate: Curve) -> UvCurve:
        """Create a curve from its X and Y coordinate curves."""
        inputs = _Tuple2_c_void_p_c_void_p(
            u_coordinate._curve_ptr, v_coordinate._curve_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_uv_Curve_Curve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def line(start_point: UvPoint, end_point: UvPoint) -> UvCurve:
        """Create a line between two points."""
        inputs = _Tuple2_c_void_p_c_void_p(
            start_point._uvpoint_ptr, end_point._uvpoint_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_line_UvPoint_UvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def arc(start_point: UvPoint, end_point: UvPoint, swept_angle: Angle) -> UvCurve:
        """Create an arc with the given start point, end point and swept angle.

        A positive swept angle means the arc turns counterclockwise (turns to the left),
        and a negative swept angle means it turns clockwise (turns to the right).
        For example, an arc with a swept angle of positive 90 degrees
        is quarter circle that turns to the left.
        """
        inputs = _Tuple4_c_double_c_void_p_c_void_p_c_void_p(
            _float_tolerance(),
            start_point._uvpoint_ptr,
            end_point._uvpoint_ptr,
            swept_angle._angle_ptr,
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_arc_UvPoint_UvPoint_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def polar_arc(
        *, center_point: UvPoint, radius: float, start_angle: Angle, end_angle: Angle
    ) -> UvCurve:
        """Create an arc with the given center point, radius, start angle and end angle."""
        inputs = _Tuple4_c_void_p_c_double_c_void_p_c_void_p(
            center_point._uvpoint_ptr,
            radius,
            start_angle._angle_ptr,
            end_angle._angle_ptr,
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_polarArc_UvPoint_Float_Angle_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def circle(*, center_point: UvPoint, diameter: float) -> UvCurve:
        """Create a circle with the given center point and diameter."""
        inputs = _Tuple2_c_void_p_c_double(center_point._uvpoint_ptr, diameter)
        output = c_void_p()
        _lib.opensolid_UvCurve_circle_UvPoint_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def swept_arc(
        center_point: UvPoint, start_point: UvPoint, swept_angle: Angle
    ) -> UvCurve:
        """Create an arc with the given center point, start point and swept angle.

        The start point will be swept around the center point by the given angle.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            center_point._uvpoint_ptr, start_point._uvpoint_ptr, swept_angle._angle_ptr
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_sweptArc_UvPoint_UvPoint_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def corner_arc(
        corner_point: UvPoint,
        *,
        incoming: UvDirection,
        outgoing: UvDirection,
        radius: float,
    ) -> UvCurve:
        """Create an arc for rounding off the corner between two straight lines."""
        inputs = _Tuple5_c_double_c_void_p_c_void_p_c_void_p_c_double(
            _float_tolerance(),
            corner_point._uvpoint_ptr,
            incoming._uvdirection_ptr,
            outgoing._uvdirection_ptr,
            radius,
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_cornerArc_UvPoint_UvDirection_UvDirection_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def bezier(control_points: list[UvPoint]) -> UvCurve:
        """Construct a Bezier curve from its control points.

        For example,

        > Curve2d.bezier (NonEmpty.four p1 p2 p3 p4))

        will return a cubic Bezier curve with the given four control points.
        """
        inputs = (
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(control_points))(
                    *[item._uvpoint_ptr for item in control_points]
                ),
            )
            if control_points
            else _error("List is empty")
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_bezier_NonEmptyUvPoint(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @staticmethod
    def hermite(
        start_point: UvPoint,
        start_derivatives: list[UvVector],
        end_point: UvPoint,
        end_derivatives: list[UvVector],
    ) -> UvCurve:
        """Construct a Bezier curve with the given endpoints and derivatives at those endpoints.

        For example,

        > Curve2d.hermite p1 [v1] p2 [v2]

        will result in a cubic spline from @p1@ to @p2@ with first derivative equal to @v1@ at @p1@ and
        first derivative equal to @v2@ at @p2@.

        The numbers of derivatives at each endpoint do not have to be equal; for example,

        > Curve2d.hermite p1 [v1] p2 []

        will result in a quadratic spline from @p1@ to @p2@ with first derivative at @p1@ equal to @v1@.

        In general, the degree of the resulting spline will be equal to 1 plus the total number of
        derivatives given.
        """
        inputs = _Tuple4_c_void_p_List_c_void_p_c_void_p_List_c_void_p(
            start_point._uvpoint_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(start_derivatives))(
                    *[item._uvvector_ptr for item in start_derivatives]
                ),
            ),
            end_point._uvpoint_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(end_derivatives))(
                    *[item._uvvector_ptr for item in end_derivatives]
                ),
            ),
        )
        output = c_void_p()
        _lib.opensolid_UvCurve_hermite_UvPoint_ListUvVector_UvPoint_ListUvVector(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @cached_property
    def start_point(self) -> UvPoint:
        """The start point of the curve."""
        inputs = self._uvcurve_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_startPoint(ctypes.byref(inputs), ctypes.byref(output))
        return UvPoint._new(output)

    @cached_property
    def end_point(self) -> UvPoint:
        """The end point of the curve."""
        inputs = self._uvcurve_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_endPoint(ctypes.byref(inputs), ctypes.byref(output))
        return UvPoint._new(output)

    @cached_property
    def derivative(self) -> UvVectorCurve:
        """The derivative of the curve."""
        inputs = self._uvcurve_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_derivative(ctypes.byref(inputs), ctypes.byref(output))
        return UvVectorCurve._new(output)

    @cached_property
    def u_coordinate(self) -> Curve:
        """Get the U coordinate of a UV curve as a scalar curve."""
        inputs = self._uvcurve_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_uCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    @cached_property
    def v_coordinate(self) -> Curve:
        """Get the V coordinate of a UV curve as a scalar curve."""
        inputs = self._uvcurve_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_vCoordinate(ctypes.byref(inputs), ctypes.byref(output))
        return Curve._new(output)

    def evaluate(self, parameter_value: float) -> UvPoint:
        """Evaluate a curve at a given parameter value.

        The parameter value should be between 0 and 1.
        """
        inputs = _Tuple2_c_double_c_void_p(parameter_value, self._uvcurve_ptr)
        output = c_void_p()
        _lib.opensolid_UvCurve_evaluate_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvPoint._new(output)

    def reverse(self) -> UvCurve:
        """Reverse a curve, so that the start point is the end point and vice versa."""
        inputs = self._uvcurve_ptr
        output = c_void_p()
        _lib.opensolid_UvCurve_reverse(ctypes.byref(inputs), ctypes.byref(output))
        return UvCurve._new(output)

    def __add__(self, rhs: UvVectorCurve) -> UvCurve:
        """Return ``self <> rhs``."""
        inputs = _Tuple2_c_void_p_c_void_p(self._uvcurve_ptr, rhs._uvvectorcurve_ptr)
        output = c_void_p()
        _lib.opensolid_UvCurve_add_UvCurve_UvVectorCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return UvCurve._new(output)

    @overload
    def __sub__(self, rhs: UvVectorCurve) -> UvCurve:
        pass

    @overload
    def __sub__(self, rhs: UvCurve) -> UvVectorCurve:
        pass

    @overload
    def __sub__(self, rhs: UvPoint) -> UvVectorCurve:
        pass

    def __sub__(self, rhs):
        """Return ``self - rhs``."""
        match rhs:
            case UvVectorCurve():
                inputs = _Tuple2_c_void_p_c_void_p(
                    self._uvcurve_ptr, rhs._uvvectorcurve_ptr
                )
                output = c_void_p()
                _lib.opensolid_UvCurve_sub_UvCurve_UvVectorCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return UvCurve._new(output)
            case UvCurve():
                inputs = _Tuple2_c_void_p_c_void_p(self._uvcurve_ptr, rhs._uvcurve_ptr)
                output = c_void_p()
                _lib.opensolid_UvCurve_sub_UvCurve_UvCurve(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return UvVectorCurve._new(output)
            case UvPoint():
                inputs = _Tuple2_c_void_p_c_void_p(self._uvcurve_ptr, rhs._uvpoint_ptr)
                output = c_void_p()
                _lib.opensolid_UvCurve_sub_UvCurve_UvPoint(
                    ctypes.byref(inputs), ctypes.byref(output)
                )
                return UvVectorCurve._new(output)
            case _:
                return NotImplemented


class Region2d:
    """A closed 2D region (possibly with holes), defined by a set of boundary curves."""

    _region2d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Region2d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Region2d)
        obj._region2d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._region2d_ptr)

    @staticmethod
    def bounded_by(curves: list[Curve2d]) -> Region2d:
        """Create a region bounded by the given curves.

        The curves may be given in any order,
        do not need to have consistent directions
        and can form multiple separate loops if the region has holes.
        However, the curves must not overlap or intersect (other than at endpoints)
        and there must not be any gaps between them.
        """
        inputs = _Tuple2_c_void_p_List_c_void_p(
            _length_tolerance()._length_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(curves))(*[item._curve2d_ptr for item in curves]),
            ),
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_boundedBy_ListCurve2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def rectangle(bounding_box: Bounds2d) -> Region2d:
        """Create a rectangular region.

        Fails if the given bounds are empty
        (zero area, i.e. zero width in either direction).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, bounding_box._bounds2d_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_rectangle_Bounds2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def circle(*, center_point: Point2d, diameter: Length) -> Region2d:
        """Create a circular region.

        Fails if the given dimeter is zero.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            center_point._point2d_ptr,
            diameter._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_circle_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def polygon(points: list[Point2d]) -> Region2d:
        """Create a polygonal region from the given vertices.

        The last vertex will be connected back to the first vertex automatically if needed
        (you do not have to close the polygon manually, although it will still work if you do).
        """
        inputs = _Tuple2_c_void_p_List_c_void_p(
            _length_tolerance()._length_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(points))(*[item._point2d_ptr for item in points]),
            ),
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_polygon_ListPoint2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def hexagon(*, center_point: Point2d, height: Length) -> Region2d:
        """Create a hexagon with the given center point and height.

        The hexagon will be oriented such that its top and bottom edges are horizontal.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            center_point._point2d_ptr,
            height._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_hexagon_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def inscribed_polygon(
        num_sides: int, *, center_point: Point2d, diameter: Length
    ) -> Region2d:
        """Create a regular polygon with the given number of sides.

        The polygon will be sized to fit within a circle with the given center point and diameter
        (each polygon vertex will lie on the circle).
        The polygon will be oriented such that its bottom-most edge is horizontal.
        """
        inputs = _Tuple4_c_void_p_c_int64_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            num_sides,
            center_point._point2d_ptr,
            diameter._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_inscribedPolygon_Int_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def circumscribed_polygon(
        num_sides: int, *, center_point: Point2d, diameter: Length
    ) -> Region2d:
        """Create a regular polygon with the given number of sides.

        The polygon will be sized so that
        a circle with the given center point and diameter will just fit within the polygon
        (each polygon edge will touch the circle at the edge's midpoint).
        For a polygon with an even number of sides (square, hexagon, octagon etc.),
        this means that the "width across flats" will be equal to the given circle diameter.
        The polygon will be oriented such that its bottom-most edge is horizontal.
        """
        inputs = _Tuple4_c_void_p_c_int64_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            num_sides,
            center_point._point2d_ptr,
            diameter._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_circumscribedPolygon_Int_Point2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @cached_property
    def outer_loop(self) -> list[Curve2d]:
        """The list of curves forming the outer boundary of the region.

        The curves will be in counterclockwise order around the region,
        and will each be in the counterclockwise direction.
        """
        inputs = self._region2d_ptr
        output = _List_c_void_p()
        _lib.opensolid_Region2d_outerLoop(ctypes.byref(inputs), ctypes.byref(output))
        return [
            Curve2d._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @cached_property
    def inner_loops(self) -> list[list[Curve2d]]:
        """The lists of curves (if any) forming the holes within the region.

        The curves will be in clockwise order around each hole,
        and each curve will be in the clockwise direction.
        """
        inputs = self._region2d_ptr
        output = _List_List_c_void_p()
        _lib.opensolid_Region2d_innerLoops(ctypes.byref(inputs), ctypes.byref(output))
        return [
            [
                Curve2d._new(c_void_p(item))
                for item in [item.field1[index] for index in range(item.field0)]
            ]
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @cached_property
    def boundary_curves(self) -> list[Curve2d]:
        """The list of all (outer and inner) boundary curves of a region."""
        inputs = self._region2d_ptr
        output = _List_c_void_p()
        _lib.opensolid_Region2d_boundaryCurves(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            Curve2d._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    def fillet(self, points: list[Point2d], *, radius: Length) -> Region2d:
        """Fillet a region at the given corner points, with the given radius.

        Fails if any of the given points are not actually corner points of the region
        (within the given tolerance),
        or if it is not possible to solve for a given fillet
        (e.g. if either of the adjacent edges is not long enough).
        """
        inputs = _Tuple4_c_void_p_List_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(points))(*[item._point2d_ptr for item in points]),
            ),
            radius._length_ptr,
            self._region2d_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Region2d_fillet_ListPoint2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Region2d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def scale_along(self, axis: Axis2d, scale: float) -> Region2d:
        """Scale (stretch) along the given axis by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            axis._axis2d_ptr, scale, self._region2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Region2d_scaleAlong_Axis2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)

    def scale_about(self, point: Point2d, scale: float) -> Region2d:
        """Scale uniformly about the given point by the given scaling factor."""
        inputs = _Tuple3_c_void_p_c_double_c_void_p(
            point._point2d_ptr, scale, self._region2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Region2d_scaleAbout_Point2d_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)

    def mirror_across(self, axis: Axis2d) -> Region2d:
        """Mirror across the given axis."""
        inputs = _Tuple2_c_void_p_c_void_p(axis._axis2d_ptr, self._region2d_ptr)
        output = c_void_p()
        _lib.opensolid_Region2d_mirrorAcross_Axis2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)

    def translate_by(self, displacement: Displacement2d) -> Region2d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement2d_ptr, self._region2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Region2d_translateBy_Displacement2d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)

    def translate_in(self, direction: Direction2d, distance: Length) -> Region2d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction2d_ptr, distance._length_ptr, self._region2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Region2d_translateIn_Direction2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)

    def translate_along(self, axis: Axis2d, distance: Length) -> Region2d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis2d_ptr, distance._length_ptr, self._region2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Region2d_translateAlong_Axis2d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)

    def rotate_around(self, point: Point2d, angle: Angle) -> Region2d:
        """Rotate around the given point by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            point._point2d_ptr, angle._angle_ptr, self._region2d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Region2d_rotateAround_Point2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Region2d._new(output)


class UvRegion:
    """A region in UV parameter space."""

    _uvregion_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> UvRegion:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(UvRegion)
        obj._uvregion_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._uvregion_ptr)

    unit_square: UvRegion = None  # type: ignore[assignment]
    """The unit square in UV space."""

    @staticmethod
    def bounded_by(curves: list[UvCurve]) -> UvRegion:
        """Create a region bounded by the given curves.

        The curves may be given in any order,
        do not need to have consistent directions
        and can form multiple separate loops if the region has holes.
        However, the curves must not overlap or intersect (other than at endpoints)
        and there must not be any gaps between them.
        """
        inputs = _Tuple2_c_double_List_c_void_p(
            _float_tolerance(),
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(curves))(*[item._uvcurve_ptr for item in curves]),
            ),
        )
        output = _Result_c_void_p()
        _lib.opensolid_UvRegion_boundedBy_ListUvCurve(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            UvRegion._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def rectangle(bounding_box: UvBounds) -> UvRegion:
        """Create a rectangular region.

        Fails if the given bounds are empty
        (zero area, i.e. zero width in either direction).
        """
        inputs = _Tuple2_c_double_c_void_p(
            _float_tolerance(), bounding_box._uvbounds_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_UvRegion_rectangle_UvBounds(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            UvRegion._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def circle(*, center_point: UvPoint, diameter: float) -> UvRegion:
        """Create a circular region.

        Fails if the given dimeter is zero.
        """
        inputs = _Tuple3_c_double_c_void_p_c_double(
            _float_tolerance(), center_point._uvpoint_ptr, diameter
        )
        output = _Result_c_void_p()
        _lib.opensolid_UvRegion_circle_UvPoint_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            UvRegion._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @cached_property
    def outer_loop(self) -> list[UvCurve]:
        """The list of curves forming the outer boundary of the region.

        The curves will be in counterclockwise order around the region,
        and will each be in the counterclockwise direction.
        """
        inputs = self._uvregion_ptr
        output = _List_c_void_p()
        _lib.opensolid_UvRegion_outerLoop(ctypes.byref(inputs), ctypes.byref(output))
        return [
            UvCurve._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @cached_property
    def inner_loops(self) -> list[list[UvCurve]]:
        """The lists of curves (if any) forming the holes within the region.

        The curves will be in clockwise order around each hole,
        and each curve will be in the clockwise direction.
        """
        inputs = self._uvregion_ptr
        output = _List_List_c_void_p()
        _lib.opensolid_UvRegion_innerLoops(ctypes.byref(inputs), ctypes.byref(output))
        return [
            [
                UvCurve._new(c_void_p(item))
                for item in [item.field1[index] for index in range(item.field0)]
            ]
            for item in [output.field1[index] for index in range(output.field0)]
        ]

    @cached_property
    def boundary_curves(self) -> list[UvCurve]:
        """The list of all (outer and inner) boundary curves of a region."""
        inputs = self._uvregion_ptr
        output = _List_c_void_p()
        _lib.opensolid_UvRegion_boundaryCurves(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return [
            UvCurve._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]


def _uvregion_unit_square() -> UvRegion:
    output = c_void_p()
    _lib.opensolid_UvRegion_unitSquare(c_void_p(), ctypes.byref(output))
    return UvRegion._new(output)


UvRegion.unit_square = _uvregion_unit_square()


class Body3d:
    """A solid body in 3D, defined by a set of boundary surfaces."""

    _body3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Body3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Body3d)
        obj._body3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._body3d_ptr)

    @staticmethod
    def extruded(
        sketch_plane: Plane3d, profile: Region2d, start: Length, end: Length
    ) -> Body3d:
        """Create an extruded body from a sketch plane and profile."""
        inputs = _Tuple5_c_void_p_c_void_p_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            sketch_plane._plane3d_ptr,
            profile._region2d_ptr,
            start._length_ptr,
            end._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Body3d_extruded_Plane3d_Region2d_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Body3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def revolved(
        sketch_plane: Plane3d, profile: Region2d, axis: Axis2d, angle: Angle
    ) -> Body3d:
        """Create a revolved body from a sketch plane and profile.

        Note that the revolution profile and revolution axis
        are both defined within the given sketch plane.

        A positive angle will result in a counterclockwise revolution around the axis,
        and a negative angle will result in a clockwise revolution.
        """
        inputs = _Tuple5_c_void_p_c_void_p_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            sketch_plane._plane3d_ptr,
            profile._region2d_ptr,
            axis._axis2d_ptr,
            angle._angle_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Body3d_revolved_Plane3d_Region2d_Axis2d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Body3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def block(bounding_box: Bounds3d) -> Body3d:
        """Create a rectangular block body.

        Fails if the given bounds are empty
        (the length, width, or height is zero).
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, bounding_box._bounds3d_ptr
        )
        output = _Result_c_void_p()
        _lib.opensolid_Body3d_block_Bounds3d(ctypes.byref(inputs), ctypes.byref(output))
        return (
            Body3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def sphere(*, center_point: Point3d, diameter: Length) -> Body3d:
        """Create a sphere with the given center point and diameter.

        Fails if the diameter is zero.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            center_point._point3d_ptr,
            diameter._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Body3d_sphere_Point3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Body3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def cylinder(
        start_point: Point3d, end_point: Point3d, *, diameter: Length
    ) -> Body3d:
        """Create a cylindrical body from a start point, end point and diameter.

        Fails if the cylinder length or diameter is zero.
        """
        inputs = _Tuple4_c_void_p_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            start_point._point3d_ptr,
            end_point._point3d_ptr,
            diameter._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Body3d_cylinder_Point3d_Point3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Body3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    @staticmethod
    def cylinder_along(
        axis: Axis3d, start: Length, end: Length, *, diameter: Length
    ) -> Body3d:
        """Create a cylindrical body along a given axis.

        In addition to the axis itself, you will need to provide:

        - Where along the axis the cylinder starts and ends
          (given as a range of distances along the axis).
        - The cylinder diameter.

        Failes if the cylinder length or diameter is zero.
        """
        inputs = _Tuple5_c_void_p_c_void_p_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            axis._axis3d_ptr,
            start._length_ptr,
            end._length_ptr,
            diameter._length_ptr,
        )
        output = _Result_c_void_p()
        _lib.opensolid_Body3d_cylinderAlong_Axis3d_Length_Length_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return (
            Body3d._new(c_void_p(output.field2))
            if output.field0 == 0
            else _error(_text_to_str(output.field1))
        )

    def place_in(self, frame: Frame3d) -> Body3d:
        """Convert a body defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._body3d_ptr)
        output = c_void_p()
        _lib.opensolid_Body3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Body3d._new(output)

    def relative_to(self, frame: Frame3d) -> Body3d:
        """Convert a body defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._body3d_ptr)
        output = c_void_p()
        _lib.opensolid_Body3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Body3d._new(output)

    def write_stl(
        self, path: str, convention: Convention3d, resolution: Resolution
    ) -> None:
        """Write a body to a binary STL file, using units of millimeters."""
        inputs = _Tuple5_c_void_p_Text_c_void_p_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            _str_to_text(path),
            convention._convention3d_ptr,
            resolution._resolution_ptr,
            self._body3d_ptr,
        )
        output = _Result_c_int64()
        _lib.opensolid_Body3d_writeSTL_Text_Convention3d_Resolution(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return None if output.field0 == 0 else _error(_text_to_str(output.field1))

    def write_mitsuba(self, path: str, resolution: Resolution) -> None:
        """Write a body to Mitsuba 'serialized' file."""
        inputs = _Tuple4_c_void_p_Text_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            _str_to_text(path),
            resolution._resolution_ptr,
            self._body3d_ptr,
        )
        output = _Result_c_int64()
        _lib.opensolid_Body3d_writeMitsuba_Text_Resolution(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return None if output.field0 == 0 else _error(_text_to_str(output.field1))


class Resolution:
    """Specify the desired accuracy of a linear approximation such as a polyline or triangle mesh."""

    _resolution_ptr: c_void_p

    def __init__(self, max_error: Length, max_size: Length) -> None:
        """Specify both the maximum error and maximum element size in the approximation."""
        inputs = _Tuple2_c_void_p_c_void_p(max_error._length_ptr, max_size._length_ptr)
        self._resolution_ptr = c_void_p()
        _lib.opensolid_Resolution_constructor_Length_Length(
            ctypes.byref(inputs), ctypes.byref(self._resolution_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Resolution:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Resolution)
        obj._resolution_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._resolution_ptr)

    @staticmethod
    def max_error(error: Length) -> Resolution:
        """Specify the maximum error/deviation of the approximation from the actual shape."""
        inputs = error._length_ptr
        output = c_void_p()
        _lib.opensolid_Resolution_maxError_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Resolution._new(output)

    @staticmethod
    def max_size(size: Length) -> Resolution:
        """Specify the maximum size of any element (line segment, triangle) in the approximation."""
        inputs = size._length_ptr
        output = c_void_p()
        _lib.opensolid_Resolution_maxSize_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Resolution._new(output)


class PbrMaterial:
    """A metallic-roughness material used for physically-based rendering."""

    _pbrmaterial_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> PbrMaterial:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(PbrMaterial)
        obj._pbrmaterial_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._pbrmaterial_ptr)

    @staticmethod
    def metal(base_color: Color, *, roughness: float) -> PbrMaterial:
        """Create a metallic material with the given color and roughness."""
        inputs = _Tuple2_c_void_p_c_double(base_color._color_ptr, roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_metal_Color_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def aluminum(*, roughness: float) -> PbrMaterial:
        """Create an aluminum material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_aluminum_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def brass(*, roughness: float) -> PbrMaterial:
        """Create a brass material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_brass_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def chromium(*, roughness: float) -> PbrMaterial:
        """Create a chromium material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_chromium_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def copper(*, roughness: float) -> PbrMaterial:
        """Create a copper material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_copper_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def gold(*, roughness: float) -> PbrMaterial:
        """Create a gold material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_gold_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def iron(*, roughness: float) -> PbrMaterial:
        """Create an iron material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_iron_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def nickel(*, roughness: float) -> PbrMaterial:
        """Create a nickel material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_nickel_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def silver(*, roughness: float) -> PbrMaterial:
        """Create a silver material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_silver_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def titanium(*, roughness: float) -> PbrMaterial:
        """Create a titanium material with the given roughness."""
        inputs = c_double(roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_titanium_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def nonmetal(base_color: Color, *, roughness: float) -> PbrMaterial:
        """Create a non-metallic material with the given color and roughness."""
        inputs = _Tuple2_c_void_p_c_double(base_color._color_ptr, roughness)
        output = c_void_p()
        _lib.opensolid_PbrMaterial_nonmetal_Color_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)

    @staticmethod
    def custom(base_color: Color, *, metallic: float, roughness: float) -> PbrMaterial:
        """Create a material with the given base color, metallic factor and roughness."""
        inputs = _Tuple3_c_void_p_c_double_c_double(
            base_color._color_ptr, metallic, roughness
        )
        output = c_void_p()
        _lib.opensolid_PbrMaterial_custom_Color_Float_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return PbrMaterial._new(output)


class Model3d:
    """A generic hierarchical 3D model for visualization/archival purposes.

    A model is composed of bodies (parts) and groups of models (assemblies),
    each with optional attributes such as name or material.
    """

    _model3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Model3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Model3d)
        obj._model3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._model3d_ptr)

    nothing: Model3d = None  # type: ignore[assignment]
    """An empty model."""

    @staticmethod
    def body(body: Body3d) -> Model3d:
        """Create a model from a single solid body (a part)."""
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, body._body3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Model3d_body_Body3d(ctypes.byref(inputs), ctypes.byref(output))
        return Model3d._new(output)

    @staticmethod
    def body_with(attributes: list[Model3d.Attribute], body: Body3d) -> Model3d:
        """Create a model from a single solid body (a part), with the given attributes."""
        inputs = _Tuple3_c_void_p_List_c_void_p_c_void_p(
            _length_tolerance()._length_ptr,
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            body._body3d_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Model3d_bodyWith_ListModel3dAttribute_Body3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    @staticmethod
    def group(children: list[Model3d]) -> Model3d:
        """Create a model formed from a group of sub-models (an assembly)."""
        inputs = _list_argument(
            _List_c_void_p,
            (c_void_p * len(children))(*[item._model3d_ptr for item in children]),
        )
        output = c_void_p()
        _lib.opensolid_Model3d_group_ListModel3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    @staticmethod
    def group_with(
        attributes: list[Model3d.Attribute], children: list[Model3d]
    ) -> Model3d:
        """Create a model formed from a group of sub-models (an assembly), with the given attributes."""
        inputs = _Tuple2_List_c_void_p_List_c_void_p(
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(children))(*[item._model3d_ptr for item in children]),
            ),
        )
        output = c_void_p()
        _lib.opensolid_Model3d_groupWith_ListModel3dAttribute_ListModel3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    @staticmethod
    def name(name: str) -> Model3d.Attribute:
        """Create a name attribute."""
        inputs = _str_to_text(name)
        output = c_void_p()
        _lib.opensolid_Model3d_name_Text(ctypes.byref(inputs), ctypes.byref(output))
        return Model3d.Attribute._new(output)

    @staticmethod
    def pbr_material(material: PbrMaterial) -> Model3d.Attribute:
        """Create a PBR material attribute for rendering."""
        inputs = material._pbrmaterial_ptr
        output = c_void_p()
        _lib.opensolid_Model3d_pbrMaterial_PbrMaterial(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d.Attribute._new(output)

    @staticmethod
    def opacity(opacity: float) -> Model3d.Attribute:
        """Create an opacity attribute, where 0 is fully transparent and 1 is fully opaque."""
        inputs = c_double(opacity)
        output = c_void_p()
        _lib.opensolid_Model3d_opacity_Float(ctypes.byref(inputs), ctypes.byref(output))
        return Model3d.Attribute._new(output)

    def with_name(self, name: str) -> Model3d:
        """Set the name of a model."""
        inputs = _Tuple2_Text_c_void_p(_str_to_text(name), self._model3d_ptr)
        output = c_void_p()
        _lib.opensolid_Model3d_withName_Text(ctypes.byref(inputs), ctypes.byref(output))
        return Model3d._new(output)

    def with_pbr_material(self, material: PbrMaterial) -> Model3d:
        """Set the PBR material used by a model."""
        inputs = _Tuple2_c_void_p_c_void_p(material._pbrmaterial_ptr, self._model3d_ptr)
        output = c_void_p()
        _lib.opensolid_Model3d_withPBRMaterial_PbrMaterial(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def with_opacity(self, opacity: float) -> Model3d:
        """Set the opacity of a model, where 0 is fully transparent and 1 is fully opaque."""
        inputs = _Tuple2_c_double_c_void_p(opacity, self._model3d_ptr)
        output = c_void_p()
        _lib.opensolid_Model3d_withOpacity_Float(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def with_attributes(self, attributes: list[Model3d.Attribute]) -> Model3d:
        """Add the given attributes to the given model."""
        inputs = _Tuple2_List_c_void_p_c_void_p(
            _list_argument(
                _List_c_void_p,
                (c_void_p * len(attributes))(
                    *[item._attribute_ptr for item in attributes]
                ),
            ),
            self._model3d_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Model3d_withAttributes_ListModel3dAttribute(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def place_in(self, frame: Frame3d) -> Model3d:
        """Convert a model defined in local coordinates to one defined in global coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._model3d_ptr)
        output = c_void_p()
        _lib.opensolid_Model3d_placeIn_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def relative_to(self, frame: Frame3d) -> Model3d:
        """Convert a model defined in global coordinates to one defined in local coordinates."""
        inputs = _Tuple2_c_void_p_c_void_p(frame._frame3d_ptr, self._model3d_ptr)
        output = c_void_p()
        _lib.opensolid_Model3d_relativeTo_Frame3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def translate_by(self, displacement: Displacement3d) -> Model3d:
        """Translate by the given displacement."""
        inputs = _Tuple2_c_void_p_c_void_p(
            displacement._displacement3d_ptr, self._model3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Model3d_translateBy_Displacement3d(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def translate_in(self, direction: Direction3d, distance: Length) -> Model3d:
        """Translate in the given direction by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            direction._direction3d_ptr, distance._length_ptr, self._model3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Model3d_translateIn_Direction3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def translate_along(self, axis: Axis3d, distance: Length) -> Model3d:
        """Translate along the given axis by the given distance."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, distance._length_ptr, self._model3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Model3d_translateAlong_Axis3d_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    def rotate_around(self, axis: Axis3d, angle: Angle) -> Model3d:
        """Rotate around the given axis by the given angle."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            axis._axis3d_ptr, angle._angle_ptr, self._model3d_ptr
        )
        output = c_void_p()
        _lib.opensolid_Model3d_rotateAround_Axis3d_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Model3d._new(output)

    class Attribute:
        """An attribute that can be applied to a model."""

        _attribute_ptr: c_void_p

        @staticmethod
        def _new(ptr: c_void_p) -> Model3d.Attribute:
            """Construct directly from an underlying C pointer."""
            obj = object.__new__(Model3d.Attribute)
            obj._attribute_ptr = ptr

            return obj

        def __del__(self) -> None:
            """Free the underlying Haskell value."""
            _lib.opensolid_release(self._attribute_ptr)


def _model3d_nothing() -> Model3d:
    output = c_void_p()
    _lib.opensolid_Model3d_nothing(c_void_p(), ctypes.byref(output))
    return Model3d._new(output)


Model3d.nothing = _model3d_nothing()


class Gltf:
    """A glTF model that can be written out to a file."""

    _gltf_ptr: c_void_p

    def __init__(self, model: Model3d) -> None:
        """Construct a glTF model from a generic 3D model."""
        inputs = model._model3d_ptr
        self._gltf_ptr = c_void_p()
        _lib.opensolid_Gltf_constructor_Model3d(
            ctypes.byref(inputs), ctypes.byref(self._gltf_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Gltf:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Gltf)
        obj._gltf_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._gltf_ptr)

    def write_binary(self, path: str, resolution: Resolution) -> None:
        """Write a model to a binary glTF file with the given resolution."""
        inputs = _Tuple3_Text_c_void_p_c_void_p(
            _str_to_text(path), resolution._resolution_ptr, self._gltf_ptr
        )
        output = _Result_c_int64()
        _lib.opensolid_Gltf_writeBinary_Text_Resolution(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return None if output.field0 == 0 else _error(_text_to_str(output.field1))


class SpurGear:
    """A metric spur gear."""

    _spurgear_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> SpurGear:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(SpurGear)
        obj._spurgear_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._spurgear_ptr)

    @staticmethod
    def metric(*, num_teeth: int, module: Length) -> SpurGear:
        """Create a metric spur gear with the given number of teeth and module."""
        inputs = _Tuple2_c_int64_c_void_p(num_teeth, module._length_ptr)
        output = c_void_p()
        _lib.opensolid_SpurGear_metric_Int_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return SpurGear._new(output)

    @cached_property
    def num_teeth(self) -> int:
        """The number of teeth of a gear."""
        inputs = self._spurgear_ptr
        output = c_int64()
        _lib.opensolid_SpurGear_numTeeth(ctypes.byref(inputs), ctypes.byref(output))
        return output.value

    @cached_property
    def module(self) -> Length:
        """The module of a gear."""
        inputs = self._spurgear_ptr
        output = c_void_p()
        _lib.opensolid_SpurGear_module(ctypes.byref(inputs), ctypes.byref(output))
        return Length._new(output)

    @cached_property
    def pitch_diameter(self) -> Length:
        """The pitch diameter of a gear."""
        inputs = self._spurgear_ptr
        output = c_void_p()
        _lib.opensolid_SpurGear_pitchDiameter(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    @cached_property
    def outer_diameter(self) -> Length:
        """The outer diameter of a gear."""
        inputs = self._spurgear_ptr
        output = c_void_p()
        _lib.opensolid_SpurGear_outerDiameter(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Length._new(output)

    def profile(self) -> list[Curve2d]:
        """Get the outer profile of a gear as a list of curves, centered at the origin.

        This is just the profile of the gear teeth themselves,
        and does not include a bore hole or anything else
        (lightening holes etc.).
        It is expected that you will combine this with
        any additional curves you want
        (likely at least one circle for a bore hole)
        and then construct a profile region from the combined set of curves
        that you can then extrude to form a gear body.
        """
        inputs = _Tuple2_c_void_p_c_void_p(
            _length_tolerance()._length_ptr, self._spurgear_ptr
        )
        output = _List_c_void_p()
        _lib.opensolid_SpurGear_profile(ctypes.byref(inputs), ctypes.byref(output))
        return [
            Curve2d._new(c_void_p(item))
            for item in [output.field1[index] for index in range(output.field0)]
        ]


class Camera3d:
    """A perspective or orthographic camera in 3D."""

    _camera3d_ptr: c_void_p

    @staticmethod
    def _new(ptr: c_void_p) -> Camera3d:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Camera3d)
        obj._camera3d_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._camera3d_ptr)

    @staticmethod
    def look_at(
        *, eye_point: Point3d, focal_point: Point3d, projection: Camera3d.Projection
    ) -> Camera3d:
        """Construct a camera at a given point, looking at a given focal point.

        The camera will be oriented such that its local up direction
        will be as close as possible to the global up direction.
        """
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            eye_point._point3d_ptr, focal_point._point3d_ptr, projection._projection_ptr
        )
        output = c_void_p()
        _lib.opensolid_Camera3d_lookAt_Point3d_Point3d_Camera3dProjection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Camera3d._new(output)

    @staticmethod
    def orbit(
        *,
        focal_point: Point3d,
        azimuth: Angle,
        elevation: Angle,
        distance: Length,
        projection: Camera3d.Projection,
    ) -> Camera3d:
        """Construct a camera orbiting around a given focal point, a given distance away.

        The azimuth is the horizontal angle towards the camera from the focal point,
        measured clockwise from the global forward direction.
        The elevation is the vertical angle towards the camera from the focal point,
        measure upwards from the global top plane.
        """
        inputs = _Tuple5_c_void_p_c_void_p_c_void_p_c_void_p_c_void_p(
            focal_point._point3d_ptr,
            azimuth._angle_ptr,
            elevation._angle_ptr,
            distance._length_ptr,
            projection._projection_ptr,
        )
        output = c_void_p()
        _lib.opensolid_Camera3d_orbit_Point3d_Angle_Angle_Length_Camera3dProjection(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Camera3d._new(output)

    @staticmethod
    def perspective(*, vertical_fov: Angle) -> Camera3d.Projection:
        """Define a perspective projection with a given vertical field of view."""
        inputs = vertical_fov._angle_ptr
        output = c_void_p()
        _lib.opensolid_Camera3d_perspective_Angle(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Camera3d.Projection._new(output)

    @staticmethod
    def orthographic(*, viewport_height: Length) -> Camera3d.Projection:
        """Define an orthographic projection with a given viewport height."""
        inputs = viewport_height._length_ptr
        output = c_void_p()
        _lib.opensolid_Camera3d_orthographic_Length(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Camera3d.Projection._new(output)

    class Projection:
        """What kind of projection (perspective or orthographic) a camera should use."""

        _projection_ptr: c_void_p

        @staticmethod
        def _new(ptr: c_void_p) -> Camera3d.Projection:
            """Construct directly from an underlying C pointer."""
            obj = object.__new__(Camera3d.Projection)
            obj._projection_ptr = ptr

            return obj

        def __del__(self) -> None:
            """Free the underlying Haskell value."""
            _lib.opensolid_release(self._projection_ptr)


class Mitsuba:
    """A Mitsuba scene that can be written out to a file."""

    _mitsuba_ptr: c_void_p

    def __init__(
        self, model: Model3d, camera: Camera3d, lighting: Mitsuba.Lighting
    ) -> None:
        """Construct a Mitsuba scene from a 3D model, a camera and some lighting."""
        inputs = _Tuple3_c_void_p_c_void_p_c_void_p(
            model._model3d_ptr, camera._camera3d_ptr, lighting._lighting_ptr
        )
        self._mitsuba_ptr = c_void_p()
        _lib.opensolid_Mitsuba_constructor_Model3d_Camera3d_MitsubaLighting(
            ctypes.byref(inputs), ctypes.byref(self._mitsuba_ptr)
        )

    @staticmethod
    def _new(ptr: c_void_p) -> Mitsuba:
        """Construct directly from an underlying C pointer."""
        obj = object.__new__(Mitsuba)
        obj._mitsuba_ptr = ptr

        return obj

    def __del__(self) -> None:
        """Free the underlying Haskell value."""
        _lib.opensolid_release(self._mitsuba_ptr)

    @staticmethod
    def environment_map(frame: Frame3d, image: str) -> Mitsuba.Lighting:
        """Specify an environment map to be used as lighting.

        You should pass a frame that defines the orientation of the environment map
        (which can often just be 'World3d.frame')
        and the path to the environment map image itself.

        The environment map image will typically be in OpenEXR format;
        https://polyhaven.com is a good source for free ones.
        """
        inputs = _Tuple2_c_void_p_Text(frame._frame3d_ptr, _str_to_text(image))
        output = c_void_p()
        _lib.opensolid_Mitsuba_environmentMap_Frame3d_Text(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return Mitsuba.Lighting._new(output)

    def write_files(self, path: str, resolution: Resolution) -> None:
        """Write a Mitsuba scene out to an XML scene description and a file containing binary mesh data.

        The scene description file will be the given path with ".xml" appended,
        and the binary mesh data file with be the given path with ".serialized" appended.
        The given resolution will be used when meshing all objects in the scene.

        Note that calling this function does not actually render the given scene,
        it just generates the necessary input files for the Mitsuba renderer.
        To actually render the generated scene, you'll need to use the Mitsuba Python package
        (https://mitsuba.readthedocs.io/en/stable/),
        calling 'mitsuba.load_file' with the path to the generated XML file.

        The generated scene will by default use 16 samples per pixel, and render an image with resolution 800x600.
        However, these can be configured by setting the 'spp', 'width' and 'height' parameters when loading the scene,
        for example with 'mitsuba.load_file(path_to_xml_file, spp=256, width=1920, height=1080)'.
        """
        inputs = _Tuple3_Text_c_void_p_c_void_p(
            _str_to_text(path), resolution._resolution_ptr, self._mitsuba_ptr
        )
        output = _Result_c_int64()
        _lib.opensolid_Mitsuba_writeFiles_Text_Resolution(
            ctypes.byref(inputs), ctypes.byref(output)
        )
        return None if output.field0 == 0 else _error(_text_to_str(output.field1))

    class Lighting:
        """The lighting to use for a Mitsuba scene."""

        _lighting_ptr: c_void_p

        @staticmethod
        def _new(ptr: c_void_p) -> Mitsuba.Lighting:
            """Construct directly from an underlying C pointer."""
            obj = object.__new__(Mitsuba.Lighting)
            obj._lighting_ptr = ptr

            return obj

        def __del__(self) -> None:
            """Free the underlying Haskell value."""
            _lib.opensolid_release(self._lighting_ptr)


__all__ = [
    "Angle",
    "AngleBounds",
    "AngleCurve",
    "Area",
    "AreaBounds",
    "AreaCurve",
    "AreaVector2d",
    "AreaVector3d",
    "Axis2d",
    "Axis3d",
    "Body3d",
    "Bounds",
    "Bounds2d",
    "Bounds3d",
    "Camera3d",
    "Color",
    "Convention3d",
    "Curve",
    "Curve2d",
    "Direction2d",
    "Direction3d",
    "Displacement2d",
    "Displacement3d",
    "DisplacementCurve2d",
    "Drawing2d",
    "Frame3d",
    "Gltf",
    "Length",
    "LengthBounds",
    "LengthCurve",
    "Mitsuba",
    "Model3d",
    "Orientation3d",
    "PbrMaterial",
    "Plane3d",
    "PlaneOrientation3d",
    "Point2d",
    "Point3d",
    "Region2d",
    "Resolution",
    "SpurGear",
    "Tolerance",
    "UvAxis",
    "UvBounds",
    "UvCurve",
    "UvDirection",
    "UvPoint",
    "UvRegion",
    "UvVector",
    "UvVectorCurve",
    "Vector2d",
    "Vector3d",
    "VectorCurve2d",
    "World3d",
]
