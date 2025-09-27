"""Functions related to Direct Linear Transformation (DLT) camera calibration."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import numpy as np
import pyquaternion
import scipy.optimize

from trakcorelib.calibration.camera import (
    CameraProperties,
    DltCameraCalibration,
    ExtrinsicProperties,
    IntrinsicProperties,
)
from trakcorelib.calibration.normalise import Normaliser
from trakcorelib.calibration.utils import validate_object_image_points

if TYPE_CHECKING:
    import numpy.typing as npt


def estimate_dlt_classic(
    object_points: npt.ArrayLike,
    image_points: npt.ArrayLike,
    *,
    do_normalise: bool = True,
) -> DltCameraCalibration:
    """Estimate DLT matrix with the classic method.

    This code performs 3D Direct Linear Transformation (DLT) camera calibration
    with from multiple camera views.

    The coordinates (x, y, z and u, v) are given as columns and the different
    points as rows. At least 6 calibration points must be specified.

    Args:
        object_points: Points in object coordinates (N x 3).
        image_points: Points in image coordinates (N x 2).
        do_normalise: Whether to normalise coordinates before performing the
            DLT estimation.

    Returns:
        The DLT camera calibration.

    """
    object_points_arr, image_points_arr = validate_object_image_points(
        object_points,
        image_points,
    )

    # Normalize the coordinates to improve the numerical behaviour of the
    # estimation, this is relevant when there is considerable perspective
    # distortion.
    if do_normalise:
        object_normaliser = Normaliser.from_points(object_points_arr)
        image_normaliser = Normaliser.from_points(image_points_arr)

        object_points_arr = object_normaliser.to_normalised(object_points_arr)
        image_points_arr = image_normaliser.to_normalised(image_points_arr)
    else:
        object_normaliser = None
        image_normaliser = None

    # Compose least squares matrix with coefficients on the columns. Each point
    # pair results in two equations in the coefficients. Consider a DLT matrix
    # with coefficients L1...L12 that has the following property:
    #
    #     [L1  L2  L3  L4 ] [x]   [u']
    #     [L5  L6  L7  L8 ] [y] = [v']
    #     [L9  L10 L11 L12] [z]   [w]
    #     .                 [1]
    #
    # where the image coordinates u, v can be computed from u', v' by
    # perspective division by w:
    #
    #     u = u' / w
    #     v = v' / w
    #
    # That is:
    #
    #     L1 x + L2 y + L3 z + L4 = u'
    #                             = u w
    #     L5 x + L6 y + L7 z + L8 = v'
    #                             = v w
    #     L9 x + L10 y + L11 z + L12 = w
    #
    # Substituting w in the first two equations with the last equation, then
    # subtracting it from the left-hand side yields the following two equations
    # for each point pair:
    #
    #     L1 x + L2 y + L3 z + L4 - L9 x u - L10 y u - L11 z u - L12 u = 0
    #     L5 x + L6 y + L7 z + L8 - L9 x v - L10 y v - L11 z v - L12 v = 0
    #
    # These equations are satisfied even when multiplied with an arbitrary
    # scaling factor, so one coefficient is not independent. We (by convention)
    # choose L12 to be the dependent coefficient and assume a value for it (by
    # convention, 1). This leads to the equations:
    #
    #     L1 x + L2 y + L3 z + L4 - L9 x u - L10 y u - L11 z u = L12 * u
    #     L5 x + L6 y + L7 z + L8 - L9 x v - L10 y v - L11 z v = L12 * v
    #
    # We add these two equations and right-hand sides for each of the normalised
    # object/image point pairs to the system.
    assumed_l12 = 1.0
    x = object_points_arr[:, 0]
    y = object_points_arr[:, 1]
    z = object_points_arr[:, 2]
    u = image_points_arr[:, 0]
    v = image_points_arr[:, 1]
    num_points = object_points_arr.shape[0]
    zeros = np.zeros(num_points)
    ones = np.ones(num_points)

    # L1 x + L2 y + L3 z + L4 - L9 x u - L10 y u - L11 z u = L12 * u
    system_eqn1 = np.column_stack(
        (x, y, z, ones, zeros, zeros, zeros, zeros, -x * u, -y * u, -z * u),
    )
    rhs_eqn1 = assumed_l12 * u

    # L5 x + L6 y + L7 z + L8 - L9 x v - L10 y v - L11 z v = L12 * v
    system_eqn2 = np.column_stack(
        (zeros, zeros, zeros, zeros, x, y, z, ones, -x * v, -y * v, -z * v),
    )
    rhs_eqn2 = assumed_l12 * v
    system = np.concatenate((system_eqn1, system_eqn2))
    rhs = np.concatenate((rhs_eqn1, rhs_eqn2))

    # Solve the system with least squares.
    sol = np.linalg.lstsq(system, rhs)
    coefs_norm = sol[0]

    # The resulting solution are the DLT matrix coefficients in row-major order,
    # but without coefficient L12. Hence, we add a value of 1 for L12 and then
    # reshape to a matrix.
    dlt = np.append(coefs_norm, assumed_l12).reshape(3, 4, order="C")

    if object_normaliser is not None and image_normaliser is not None:
        # The coefficients are computed based on normalised coordinates, so
        # rescale back to "regular" coordinates. Consider the normalised DLT
        # matrix L', normalised object point x' = Tx x and normalised image
        # point u' = Tu u:
        #
        #     L' x' = u'
        #     L' (Tx x) = Tu u
        #     inv(Tu) L' Tx x = u
        #
        # Hence, the unscaled DLT matrix is:
        #
        #     L = inv(Tu) L' Tx
        dlt = (
            image_normaliser.normalised_to_regular
            @ dlt
            @ object_normaliser.regular_to_normalised
        )
        # Because of the rescaling, L12 is no longer 1, so normalise all
        # coefficients of the matrix to make sure L12 is 1 again.
        dlt /= dlt[-1, -1]

    return DltCameraCalibration(dlt)


def estimate_dlt_optimisation(
    object_points: npt.ArrayLike,
    image_points: npt.ArrayLike,
    fixed_intrinsic: IntrinsicProperties | None = None,
    fixed_extrinsic: ExtrinsicProperties | None = None,
) -> DltCameraCalibration:
    """Estimate DLT matrix by optimising camera properties.

    This code performs 3D Direct Linear Transformation (DLT) camera calibration
    with from multiple camera views. It optimises camera properties directly
    with a non-linear least squares algorithm, thus enforcing orthogonality of
    the camera transformation matrix. Hence, unlike classic DLT, this
    transformation matrix will always be a valid rotation (i.e. an orthogonal
    matrix).

    The coordinates (x, y, z and u, v) are given as columns and the different
    points as rows. At least 6 calibration points must be specified.

    Args:
        object_points: Points in object coordinates (N x 3).
        image_points: Points in image coordinates (N x 2).
        fixed_intrinsic: Intrinsic properties to be fixed in the optimisation,
            only the extrinsic properties will be optimised.
        fixed_extrinsic: Extrinsic properties to be fixed in the optimisation,
            only the intrinsic properties will be optimised.

    Returns:
        The DLT camera calibration.

    """
    is_fixed_intrinsic = fixed_intrinsic is not None
    is_fixed_extrinsic = fixed_extrinsic is not None
    if is_fixed_intrinsic and is_fixed_extrinsic:
        msg = (
            "Specify either no fixed properties, only fixed intrinsic "
            "properties, or only fixed extrinsic properties, not both."
        )
        raise ValueError(msg)

    object_points_arr, image_points_arr = validate_object_image_points(
        object_points,
        image_points,
    )

    # Initialise with classic DLT.
    calib_init = estimate_dlt_classic(object_points, image_points)
    vector_init = _convert_to_optimisation_vector(
        calib_init,
        is_fixed_intrinsic=is_fixed_intrinsic,
        is_fixed_extrinsic=is_fixed_extrinsic,
    )

    # Minimise the sum squares of the differences between reprojected points and
    # reference image points.
    solution = scipy.optimize.least_squares(
        _objective_function,
        vector_init,
        args=(object_points_arr, image_points_arr, fixed_intrinsic, fixed_extrinsic),
        method="lm",
        loss="linear",
        x_scale="jac",
    )
    if not solution.success:
        msg = "Least squares optimisation failed to converge."
        raise ValueError(msg)

    return _convert_from_optimisation_vector(
        solution.x,
        fixed_intrinsic,
        fixed_extrinsic,
    )


def _convert_to_optimisation_vector(
    calibration: DltCameraCalibration,
    *,
    is_fixed_intrinsic: bool,
    is_fixed_extrinsic: bool,
) -> npt.NDArray[np.float64]:
    """Convert camera properties to an array to optimise."""
    properties = calibration.compute_camera_properties()

    if is_fixed_intrinsic:
        intrinsic_vector = np.array([])

    else:
        intrinsic = properties.intrinsic
        intrinsic_vector = np.array(
            [
                intrinsic.u_principal,
                intrinsic.v_principal,
                intrinsic.focal_length_u,
                intrinsic.focal_length_v,
            ],
            dtype=np.float64,
        )

    extrinsic_vector: npt.NDArray[np.float64] = np.array([], dtype=np.float64)
    if not is_fixed_extrinsic:
        extrinsic = properties.extrinsic
        rotation_vector = cast("npt.NDArray[np.float64]", extrinsic.rotation.elements)
        extrinsic_vector = np.concatenate(
            (extrinsic.coords, rotation_vector),
        )

    return np.concatenate((intrinsic_vector, extrinsic_vector))


def _convert_from_optimisation_vector(
    vector: npt.NDArray[np.float64],
    fixed_intrinsic: IntrinsicProperties | None,
    fixed_extrinsic: ExtrinsicProperties | None,
) -> DltCameraCalibration:
    """Convert an optimisation vector to a DLT camera calibration."""
    assert fixed_intrinsic is None or fixed_extrinsic is None

    if fixed_intrinsic is not None:
        assert vector.shape == (7,)

        intrinsic = fixed_intrinsic
        extrinsic = ExtrinsicProperties(
            tuple(vector[:3]),
            pyquaternion.Quaternion(vector[3:]),
        )
    else:
        intrinsic = IntrinsicProperties(vector[0], vector[1], vector[2], vector[3])
        if fixed_extrinsic is not None:
            assert vector.shape == (4,)
            extrinsic = fixed_extrinsic
        else:
            assert vector.shape == (11,)
            extrinsic = ExtrinsicProperties(
                tuple(vector[4:7]),
                pyquaternion.Quaternion(vector[7:]),
            )

    properties = CameraProperties(intrinsic, extrinsic)
    return DltCameraCalibration.from_camera_properties(properties)


def _objective_function(
    vector: npt.NDArray[np.float64],
    object_points: npt.NDArray[np.float64],
    image_points: npt.NDArray[np.float64],
    fixed_intrinsic: IntrinsicProperties | None,
    fixed_extrinsic: ExtrinsicProperties | None,
) -> npt.NDArray[np.float64]:
    """Compute objective function for optimising camera properties.

    The result is an array of reprojection errors for each point pair.
    """
    calibration = _convert_from_optimisation_vector(
        vector,
        fixed_intrinsic,
        fixed_extrinsic,
    )
    reprojected = calibration.project(object_points)

    # Compute the reprojection error in pixels for each point, along each
    # dimension.
    return image_points.flatten() - reprojected.flatten()
