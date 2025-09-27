"""Internal utility functions for camera calibrations."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    import numpy.typing as npt


def orthogonalise_rotation_matrix(
    rotation_matrix: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    """Orthogonalises a slightly non-orthogonal rotation matrix."""
    assert rotation_matrix.shape == (3, 3)
    # Perform a singular value decomposition, defined as R = U S V, where U and
    # V are real-valued orthogonal matrices, and S is a diagonal matrix with
    # non-negative singular values. If R is a (square) orthogonal matrix, then
    # all singular values are 1 and S is an identity matrix, hence R = U V. We
    # assume that our input matrix is near-orthogonal, so we ignore the singular
    # values by assuming S is close to an identity matrix, so R ~= U V.
    u, _, v = np.linalg.svd(rotation_matrix)
    orthogonal: npt.NDArray[np.float64] = u @ v
    return orthogonal


def validate_object_image_points(
    object_points: npt.ArrayLike,
    image_points: npt.ArrayLike,
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Validate object and image points and guarantee NumPy arrays."""
    object_points_arr = np.asarray(object_points, dtype=np.float64)
    image_points_arr = np.asarray(image_points, dtype=np.float64)

    num_points = object_points_arr.shape[0]

    if object_points_arr.shape[1] != 3:
        msg = "Specify the object points as an N x 3 array."
        raise ValueError(msg)

    if image_points_arr.shape[0] != num_points:
        msg = (
            f"Specify the same number of object points ({num_points} points) "
            f"as image points ({image_points_arr.shape[0]} points)."
        )
        raise ValueError(msg)

    if image_points_arr.shape[1] != 2:
        msg = "Specify the image points as an N x 2 array."
        raise ValueError(msg)

    if num_points < 6:
        msg = (
            "Specify at least at least 6 object/image point pairs, only "
            f"{num_points} were specified."
        )
        raise ValueError(msg)

    return object_points_arr, image_points_arr
