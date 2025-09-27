from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

import pyquaternion
import pytest

from trakcorelib.calibration.utils import orthogonalise_rotation_matrix

if TYPE_CHECKING:
    import numpy.typing as npt


@pytest.fixture
def random_rotation_matrix() -> npt.NDArray[np.float64]:
    rng = np.random.default_rng()
    quaternion = pyquaternion.Quaternion(rng.uniform(-10, 10, 4))
    return quaternion.normalised.rotation_matrix  # type: ignore[no-any-return]


def test_orthogonalise_orthogonal_matrix(
    random_rotation_matrix: npt.NDArray[np.float64],
) -> None:
    orthogonalised = orthogonalise_rotation_matrix(random_rotation_matrix)
    np.testing.assert_almost_equal(random_rotation_matrix, orthogonalised)


def test_orthogonalise_near_orthogonal_matrix(
    random_rotation_matrix: npt.NDArray[np.float64],
) -> None:
    # Disturb the original matrix slightly so it is non-orthogonal.
    disturbed = random_rotation_matrix.copy()
    disturbed += np.random.default_rng().uniform(-0.01, 0.01, (3, 3))

    # Verify that the matrix is non-orthogonal.
    assert not np.isclose(abs(np.linalg.det(disturbed)), 1.0)

    # Orthogonalise the matrix and verify that it is close to the original.
    orthogonalised = orthogonalise_rotation_matrix(random_rotation_matrix)
    np.testing.assert_allclose(random_rotation_matrix, orthogonalised)
