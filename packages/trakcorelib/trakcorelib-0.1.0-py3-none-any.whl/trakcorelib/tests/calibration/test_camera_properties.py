from __future__ import annotations

import numpy as np
import pyquaternion

from trakcorelib.calibration.camera import (
    CameraProperties,
    DltCameraCalibration,
    ExtrinsicProperties,
    IntrinsicProperties,
)
from trakcorelib.tests.calibration.utils import compare_camera_properties


def random(start: float = -10, end: float = 10) -> float:
    assert end > start
    range = end - start
    return np.random.random() * range + start


def test_to_and_from_properties() -> None:
    # Create a DLT calibration from camera properties.
    rotation = pyquaternion.Quaternion(np.random.random_sample((4,))).normalised
    coords = (random(), random(), random())

    xp = random()
    yp = random()
    fx = random(0, 10)
    fy = random(0, 10)

    properties = CameraProperties(
        IntrinsicProperties(xp, yp, fx, fy), ExtrinsicProperties(coords, rotation)
    )
    dlt = DltCameraCalibration.from_camera_properties(properties)

    # Make sure the DLT has appropriately scaled coefficients.
    assert np.isclose(dlt.projection_matrix[-1, -1], 1)

    # Then reconstruct camera properties from the DLT; they should be close to
    # identical.
    reconstructed = dlt.compute_camera_properties()

    compare_camera_properties(properties, reconstructed)


def test_from_almost_identity_properties() -> None:
    # No rotation.
    rotation = pyquaternion.Quaternion()
    # No translation, except in z, because that coordinate cannot be 0. Note
    # that this is the location of the camera in world coordinates, while the
    # translation in the final matrix is the location of the world coordinate
    # origin in camera coordinates, so inverted.
    coords = (0, 0, -1)

    # Principal point in (0, 0), focal lengths of (1, 1); results in identity
    # matrix for the intrinsic matrix.
    xp = 0
    yp = 0
    fx = 1
    fy = 1

    properties = CameraProperties(
        IntrinsicProperties(xp, yp, fx, fy), ExtrinsicProperties(coords, rotation)
    )
    dlt = DltCameraCalibration.from_camera_properties(properties)

    reference = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]], dtype=np.float64)
    np.testing.assert_allclose(dlt.projection_matrix, reference)


def test_to_almost_identity_properties() -> None:
    matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]], dtype=np.float64)
    dlt = DltCameraCalibration(matrix)

    properties = dlt.compute_camera_properties()

    assert np.isclose(properties.intrinsic.u_principal, 0)
    assert np.isclose(properties.intrinsic.v_principal, 0)
    assert np.isclose(properties.intrinsic.focal_length_u, 1)
    assert np.isclose(properties.intrinsic.focal_length_v, 1)

    np.testing.assert_allclose(properties.extrinsic.coords, (0, 0, -1))
    np.testing.assert_allclose(properties.extrinsic.rotation.elements, (1, 0, 0, 0))


def test_pure_translation_properties() -> None:
    # No rotation.
    rotation = pyquaternion.Quaternion()
    # Note that the translation has the opposite sign as the translation in the
    # projection matrix, as the latter is defined as the translation of the
    # world coordinate origin in the camera coordinate system.
    x = -1.1
    y = -3.45
    z = 6.123
    coords = (x, y, z)

    # Principal point in (0, 0), focal lengths of (1, 1); results in identity
    # matrix for the intrinsic matrix.
    xp = 0
    yp = 0
    fx = 1
    fy = 1

    properties = CameraProperties(
        IntrinsicProperties(xp, yp, fx, fy), ExtrinsicProperties(coords, rotation)
    )
    dlt = DltCameraCalibration.from_camera_properties(properties)

    reference = np.array(
        [[1, 0, 0, -x], [0, 1, 0, -y], [0, 0, 1, -z]], dtype=np.float64
    )
    reference /= -z
    np.testing.assert_allclose(dlt.projection_matrix, reference)

    reconstructed = dlt.compute_camera_properties()
    assert reconstructed == properties


def test_simple_properties() -> None:
    # No rotation.
    rotation = pyquaternion.Quaternion()
    # No translation, except in z, because that coordinate cannot be 0.
    coords = (0, 0, 1)

    # Principal point in (1, 2), focal lengths of (1, 1)
    xp = 1
    yp = 2
    fx = 1
    fy = 1

    properties = CameraProperties(
        IntrinsicProperties(xp, yp, fx, fy), ExtrinsicProperties(coords, rotation)
    )
    dlt = DltCameraCalibration.from_camera_properties(properties)

    assert properties == dlt.compute_camera_properties()

    np.testing.assert_allclose(dlt.project([0, 0, 0]), [1, 2])
    np.testing.assert_allclose(dlt.project([-1, -2, 0]), [2, 4])
