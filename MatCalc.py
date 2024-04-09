import numpy as np
import sys
import math


def x_rotation_3d(angle: float) -> np.ndarray:
    """
    Generate a 3D rotation matrix around the X-axis.

    Parameters:
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 3D rotation matrix.
    """
    angle = np.deg2rad(angle)
    return np.array([[1.0, 0.0, 0.0],
                     [0.0, np.cos(angle), -np.sin(angle)],
                     [0.0, np.sin(angle), np.cos(angle)]])


def y_rotation_3d(angle: float) -> np.ndarray:
    """
    Generate a 3D rotation matrix around the Y-axis.

    Parameters:
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 3D rotation matrix.
    """
    angle = np.deg2rad(angle)
    return np.array([[np.cos(angle), 0.0, np.sin(angle)],
                     [0.0, 1.0, 0.0],
                     [-np.sin(angle), 0.0, np.cos(angle)]])


def z_rotation_3d(angle: float) -> np.ndarray:
    """
    Generate a 3D rotation matrix around the Z-axis.

    Parameters:
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 3D rotation matrix.
    """
    angle = np.deg2rad(angle)
    return np.array([[np.cos(angle), -np.sin(angle), 0.0],
                     [np.sin(angle), np.cos(angle), 0.0],
                     [0.0, 0.0, 1.0]])


def rotation_3d(yaw: float, pitch: float, roll: float) -> np.ndarray:
    """
    Generate a combined 3D rotation matrix using yaw, pitch, and roll angles.

    Parameters:
        yaw (float): The rotation angle around the Z-axis in degrees.
        pitch (float): The rotation angle around the Y-axis in degrees.
        roll (float): The rotation angle around the X-axis in degrees.

    Returns:
        np.ndarray: The combined 3D rotation matrix.
    """
    return z_rotation_3d(yaw) @ y_rotation_3d(pitch) @ x_rotation_3d(roll)


def axis_angle_3d(axis: list, angle: float) -> np.ndarray:
    """
    Generate a 3D rotation matrix based on the axis-angle representation.

    Parameters:
        axis (list): The rotation axis represented as [x, y, z].
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 3D rotation matrix.
    """
    angle = np.deg2rad(angle)
    t = 1.0 - np.cos(angle)
    x, y, z = axis[0], axis[1], axis[2]
    magnitude_squared = np.dot(axis, axis)
    if math.isclose(1.0 + 2.0, 3.0, rel_tol=sys.float_info.epsilon) != 1.0:
        normalized_magnitude = 1.0 / np.sqrt(magnitude_squared)
        x *= normalized_magnitude
        y *= normalized_magnitude
        z *= normalized_magnitude
    return np.array([[t * x * x + np.cos(angle), t * x * y - np.sin(angle) * z, t * x * z + np.sin(angle) * y],
                     [t * y * x + np.sin(angle) * z, t * y * y + np.cos(angle), t * y * z - np.sin(angle) * x],
                     [t * z * x - np.sin(angle) * y, t * z * y + np.sin(angle) * x, t * z * z + np.cos(angle)]])


def translation_4d(x: float, y: float, z: float) -> np.ndarray:
    """
    Generate a 4D translation matrix.

    Parameters:
        x (float): Translation along the X-axis.
        y (float): Translation along the Y-axis.
        z (float): Translation along the Z-axis.

    Returns:
        np.ndarray: The 4D translation matrix.
    """
    return np.array([[1.0, 0.0, 0.0, x],
                     [0.0, 1.0, 0.0, y],
                     [0.0, 0.0, 1.0, z],
                     [0.0, 0.0, 0.0, 1.0]])


def x_rotation_4d(angle: float) -> np.ndarray:
    """
    Generate a 4D rotation matrix around the X-axis.

    Parameters:
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 4D rotation matrix.
    """
    angle = np.deg2rad(angle)
    return np.array([[1.0, 0.0, 0.0, 0.0],
                     [0.0, np.cos(angle), -np.sin(angle), 0.0],
                     [0.0, np.sin(angle), np.cos(angle), 0.0],
                     [0.0, 0.0, 0.0, 1.0]])


def y_rotation_4d(angle: float) -> np.ndarray:
    """
    Generate a 4D rotation matrix around the Y-axis.

    Parameters:
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 4D rotation matrix.
    """
    angle = np.deg2rad(angle)
    return np.array([[np.cos(angle), 0.0, np.sin(angle), 0.0],
                     [0.0, 1.0, 0.0, 0.0],
                     [-np.sin(angle), 0.0, np.cos(angle), 0.0],
                     [0.0, 0.0, 0.0, 1.0]])


def z_rotation_4d(angle: float) -> np.ndarray:
    """
    Generate a 4D rotation matrix around the Z-axis.

    Parameters:
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 4D rotation matrix.
    """
    angle = np.deg2rad(angle)
    return np.array([[np.cos(angle), -np.sin(angle), 0.0, 0.0],
                     [np.sin(angle), np.cos(angle), 0.0, 0.0],
                     [0.0, 0.0, 1.0, 0.0],
                     [0.0, 0.0, 0.0, 1.0]])


def rotation_4d(yaw: float, pitch: float, roll: float) -> np.ndarray:
    """
    Generate a combined 4D rotation matrix using yaw, pitch, and roll angles.

    Parameters:
        yaw (float): The rotation angle around the Z-axis in degrees.
        pitch (float): The rotation angle around the Y-axis in degrees.
        roll (float): The rotation angle around the X-axis in degrees.

    Returns:
        np.ndarray: The combined 4D rotation matrix.
    """
    return z_rotation_4d(yaw) @ y_rotation_4d(pitch) @ x_rotation_4d(roll)


def axis_angle_4d(axis: list, angle: float) -> np.ndarray:
    """
    Generate a 4D rotation matrix based on the axis-angle representation.

    Parameters:
        axis (list): The rotation axis represented as [x, y, z].
        angle (float): The rotation angle in degrees.

    Returns:
        np.ndarray: The 4D rotation matrix.
    """
    angle = np.deg2rad(angle)
    t = 1.0 - np.cos(angle)
    x, y, z = axis[0], axis[1], axis[2]
    magnitude_squared = np.dot(axis, axis)
    if math.isclose(1.0 + 2.0, 3.0, rel_tol=sys.float_info.epsilon) != 1.0:
        normalized_magnitude = 1.0 / np.sqrt(magnitude_squared)
        x *= normalized_magnitude
        y *= normalized_magnitude
        z *= normalized_magnitude
    return np.array([[t * x * x + np.cos(angle), t * x * y - np.sin(angle) * z, t * x * z + np.sin(angle) * y, 0.0],
                     [t * y * x + np.sin(angle) * z, t * y * y + np.cos(angle), t * y * z - np.sin(angle) * x, 0.0],
                     [t * z * x - np.sin(angle) * y, t * z * y + np.sin(angle) * x, t * z * z + np.cos(angle), 0.0],
                     [0.0, 0.0, 0.0, 1.0]])
