# **************************************************************************************

# @package        satelles
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from math import cos, isclose, radians, sin, sqrt
from typing import Literal

from .common import CartesianCoordinate

# **************************************************************************************


def normalise(
    vector: CartesianCoordinate,
) -> CartesianCoordinate:
    """
    Normalise a 3D vector (x, y, z) to a unit vector.

    Args:
        vector (CartesianCoordinate): The input vector.

    Returns:
        CartesianCoordinate: The unit vector in the same direction as the input vector.

    Raises:
        ValueError: If the input vector's magnitude is zero.
    """
    x, y, z = vector["x"], vector["y"], vector["z"]

    # Compute the vector's magnitude (length):
    r = sqrt(x**2 + y**2 + z**2)

    if isclose(r, 0.0, abs_tol=1e-15):
        raise ValueError("Cannot convert a zero-length vector to a unit vector.")

    return CartesianCoordinate(
        x=x / r,
        y=y / r,
        z=z / r,
    )


# **************************************************************************************


def dot(i: CartesianCoordinate, j: CartesianCoordinate) -> float:
    """
    Compute the dot product of two 3D vectors.

    Args:
        i (CartesianCoordinate): The first vector.
        j (CartesianCoordinate): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """
    return i["x"] * j["x"] + i["y"] * j["y"] + i["z"] * j["z"]


# **************************************************************************************


def rotate(
    vector: CartesianCoordinate, angle: float, axis: Literal["x", "y", "z"]
) -> CartesianCoordinate:
    """
    Rotate a 3D vector (x, y, z) by a given angle (in degrees) around the specified axis.

    Args:
        vector (CartesianCoordinate): The vector to rotate.
        angle (float): The rotation angle (in degrees).
        axis (Literal['x', 'y', 'z']): The axis to rotate around ('x', 'y', or 'z').

    Returns:
        CartesianCoordinate: The rotated vector as a CartesianCoordinate object.

    Raises:
        ValueError: If the provided axis is not one of 'x', 'y', or 'z'.
    """
    x, y, z = vector["x"], vector["y"], vector["z"]

    A = radians(angle)

    # Rotate the vector around the z-axis:
    if axis == "z":
        return CartesianCoordinate(
            x=x * cos(A) - y * sin(A),
            y=x * sin(A) + y * cos(A),
            z=z,
        )

    # Rotate the vector around the x-axis:
    if axis == "x":
        return CartesianCoordinate(
            x=x,
            y=y * cos(A) - z * sin(A),
            z=y * sin(A) + z * cos(A),
        )

    # Rotate the vector around the y-axis:
    if axis == "y":
        return CartesianCoordinate(
            x=x * cos(A) + z * sin(A),
            y=y,
            z=-x * sin(A) + z * cos(A),
        )

    raise ValueError("Axis must be 'x', 'y', or 'z'.")


# **************************************************************************************
