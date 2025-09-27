from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import numpy as np
import pyquaternion
import pytest

from trakcorelib.calibration.camera import (
    CameraProperties,
    DltCameraCalibration,
    ExtrinsicProperties,
    IntrinsicProperties,
)
from trakcorelib.calibration.dlt import estimate_dlt_classic, estimate_dlt_optimisation
from trakcorelib.tests.calibration.utils import compare_camera_properties

if TYPE_CHECKING:
    import numpy.typing as npt


@pytest.fixture
def random_matrix_object_image_points() -> tuple[
    CameraProperties,
    npt.NDArray[np.float64],
    npt.NDArray[np.float64],
    npt.NDArray[np.float64],
]:
    # Create random DLT matrix from camera properties, to guarantee that it has
    # appropriate properties.
    rng = np.random.default_rng()
    intrinsic = IntrinsicProperties(
        rng.uniform(low=-1000, high=1000),
        rng.uniform(low=-1000, high=1000),
        rng.uniform(low=0, high=1000),
        rng.uniform(low=0, high=1000),
    )

    coords = tuple(rng.uniform(low=-10, high=10, size=(3,)))
    rotation = pyquaternion.Quaternion(
        rng.uniform(low=-10, high=10, size=(4,))
    ).normalised
    extrinsic = ExtrinsicProperties(coords, rotation)

    properties = CameraProperties(intrinsic, extrinsic)

    dlt = DltCameraCalibration.from_camera_properties(properties)
    matrix = dlt.projection_matrix

    num_points = 12
    object_points = np.random.random_sample((num_points, 3))

    object_points_homogeneous = np.hstack((object_points, np.ones((num_points, 1))))
    image_points_homogeneous = matrix @ object_points_homogeneous.T

    uv = image_points_homogeneous[:-1, :].T
    w = image_points_homogeneous[-1, :].T
    image_points = uv / w[:, np.newaxis]

    return properties, matrix, object_points, image_points


@pytest.mark.parametrize("do_normalise", [False, True])
def test_classic_dlt_reconstruct_random_matrix(
    random_matrix_object_image_points: tuple[
        CameraProperties,
        npt.NDArray[np.float64],
        npt.NDArray[np.float64],
        npt.NDArray[np.float64],
    ],
    do_normalise: bool,
) -> None:
    properties, matrix, object_points, image_points = random_matrix_object_image_points
    calibration = estimate_dlt_classic(
        object_points, image_points, do_normalise=do_normalise
    )
    np.testing.assert_allclose(matrix, calibration.projection_matrix)

    projected = calibration.project(object_points)
    np.testing.assert_allclose(image_points, projected)

    reconstructed_properties = calibration.compute_camera_properties()
    compare_camera_properties(properties, reconstructed_properties)


@pytest.mark.parametrize(
    "do_fix_intrinsic,do_fix_extrinsic", [(False, False), (True, False), (False, True)]
)
def test_optimisation_dlt_reconstruct_random_matrix(
    random_matrix_object_image_points: tuple[
        CameraProperties,
        npt.NDArray[np.float64],
        npt.NDArray[np.float64],
        npt.NDArray[np.float64],
    ],
    *,
    do_fix_intrinsic: bool,
    do_fix_extrinsic: bool,
) -> None:
    properties, matrix, object_points, image_points = random_matrix_object_image_points

    fixed_intrinsic = properties.intrinsic if do_fix_intrinsic else None
    fixed_extrinsic = properties.extrinsic if do_fix_extrinsic else None

    calibration = estimate_dlt_optimisation(
        object_points, image_points, fixed_intrinsic, fixed_extrinsic
    )
    np.testing.assert_allclose(matrix, calibration.projection_matrix)

    projected = calibration.project(object_points)
    np.testing.assert_allclose(image_points, projected)

    reconstructed_properties = calibration.compute_camera_properties()
    compare_camera_properties(properties, reconstructed_properties)


def test_dlt_to_from_coefficients() -> None:
    matrix = np.random.random_sample((3, 4))
    matrix[2, 3] = 1.0

    dlt = DltCameraCalibration(matrix)

    from_coefs = DltCameraCalibration.from_coefficients(dlt.coefficients)

    np.testing.assert_almost_equal(dlt.coefficients, from_coefs.coefficients)
    np.testing.assert_almost_equal(dlt.projection_matrix, from_coefs.projection_matrix)


@pytest.mark.parametrize(
    "method,do_normalise",
    [("classic", False), ("classic", True), ("optimisation", False)],
)
def test_dlt_example_data(
    example_calibration_data: tuple[
        npt.NDArray[np.float64], list[npt.NDArray[np.float64]]
    ],
    method: Literal["classic", "optimisation"],
    do_normalise: bool,
) -> None:
    object_points, image_points = example_calibration_data

    # These data are not great so the mean reprojection error is pretty large...
    maximum_rms_error = 10

    for image_points_view in image_points:
        if method == "classic":
            dlt_view = estimate_dlt_classic(
                object_points, image_points_view, do_normalise=do_normalise
            )
        else:
            dlt_view = estimate_dlt_optimisation(object_points, image_points_view)

        reprojected = dlt_view.project(object_points)

        error_distance_squared: npt.NDArray[np.float64] = np.sum(
            (image_points_view - reprojected) ** 2, axis=1
        )
        rms_error = np.sqrt(np.mean(error_distance_squared))

        assert rms_error == dlt_view.compute_reprojection_rms_error(
            object_points, image_points_view
        )
        assert rms_error < maximum_rms_error
