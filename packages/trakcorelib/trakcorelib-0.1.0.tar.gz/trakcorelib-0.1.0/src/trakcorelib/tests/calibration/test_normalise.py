import numpy as np

import pytest

from trakcorelib.calibration.normalise import Normaliser


@pytest.fixture(autouse=True)
def set_fixed_seed() -> None:
    np.random.seed(12345)


@pytest.mark.parametrize("num_dimensions", [2, 3])
def test_identity_transformation(num_dimensions: int) -> None:
    origin = np.zeros((num_dimensions,))
    length_scale = 1
    normaliser = Normaliser(origin, length_scale)

    points = np.random.rand(10, num_dimensions)
    normalised = normaliser.to_normalised(points)
    np.testing.assert_almost_equal(points, normalised)

    denormalised = normaliser.from_normalised(points)
    np.testing.assert_almost_equal(points, denormalised)


@pytest.mark.parametrize("num_dimensions", [2, 3])
def test_only_scale(num_dimensions: int) -> None:
    origin = np.zeros((num_dimensions,))
    length_scale = np.random.random() * 10
    normaliser = Normaliser(origin, length_scale)

    # Check whether a point with the specified length scale is transformed to
    # a length of 1.
    points_unit = length_scale * np.ones((1, num_dimensions))
    np.testing.assert_almost_equal(
        np.ones((1, num_dimensions)), normaliser.to_normalised(points_unit)
    )

    points = np.random.rand(10, num_dimensions)

    np.testing.assert_almost_equal(
        points / length_scale, normaliser.to_normalised(points)
    )
    np.testing.assert_almost_equal(
        points * length_scale, normaliser.from_normalised(points)
    )


@pytest.mark.parametrize("num_dimensions", [2, 3])
def test_only_translate(num_dimensions: int) -> None:
    origin = np.random.rand(num_dimensions)
    length_scale = 1
    normaliser = Normaliser(origin, length_scale)

    points = np.random.rand(10, num_dimensions)

    # Check whether a point in the origin is transformed to (0, 0) or (0, 0, 0).
    points_origin = [origin]
    np.testing.assert_almost_equal(
        np.zeros((1, num_dimensions)), normaliser.to_normalised(points_origin)
    )

    np.testing.assert_almost_equal(points - origin, normaliser.to_normalised(points))
    np.testing.assert_almost_equal(points + origin, normaliser.from_normalised(points))


@pytest.mark.parametrize("num_dimensions", [2, 3])
def test_to_and_from_transformation(num_dimensions: int) -> None:
    origin = np.random.rand(num_dimensions)
    scale = 2 * np.random.random()
    normaliser = Normaliser(origin, scale)

    points = np.random.rand(10, num_dimensions)
    normalised = normaliser.to_normalised(points)
    denormalised = normaliser.from_normalised(normalised)

    np.testing.assert_almost_equal(points, denormalised)
