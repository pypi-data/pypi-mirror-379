from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pytest

from trakcorelib.calibration.dlt import estimate_dlt_classic
from trakcorelib.calibration.multiview import MultiViewCalibration

if TYPE_CHECKING:
    import numpy.typing as npt


@pytest.fixture
def example_multiview_calibration(
    example_calibration_data: tuple[
        npt.NDArray[np.float64], list[npt.NDArray[np.float64]]
    ],
) -> MultiViewCalibration:
    object_points, image_points = example_calibration_data

    calibrations = (
        estimate_dlt_classic(object_points, image_points_view)
        for image_points_view in image_points
    )
    return MultiViewCalibration(calibrations)


def test_reconstruct_example_object_points(
    example_calibration_data: tuple[
        npt.NDArray[np.float64], list[npt.NDArray[np.float64]]
    ],
    example_multiview_calibration: MultiViewCalibration,
) -> None:
    object_points, image_points = example_calibration_data

    num_points = object_points.shape[0]
    mean_error = 0.0
    for i in range(num_points):
        current_image_points = [
            image_points_view[i] for image_points_view in image_points
        ]
        original = object_points[i, :]
        reconstructed = example_multiview_calibration.reconstruct_object_point(
            current_image_points
        )

        mean_error += np.sqrt(np.sum((original - reconstructed) ** 2))
    mean_error /= num_points

    max_mean_reconstruction_error = 0.2
    assert mean_error < max_mean_reconstruction_error


def test_to_from_csv(
    tmp_path_factory: pytest.TempPathFactory,
    example_multiview_calibration: MultiViewCalibration,
) -> None:
    csv_path = tmp_path_factory.mktemp("multiview") / "coefs.csv"
    example_multiview_calibration.to_csv(csv_path)

    with open(csv_path, "r") as file:
        lines = file.readlines()

    # Check whether we get a valid header.
    header = lines[0]
    assert header.startswith("#")
    assert all(name in header for name in example_multiview_calibration.names)

    # Check whether we get 11 data lines (12 including header), with 3 comma's
    # per line.
    assert len(lines) == 12
    assert all(line.count(",") == 3 for line in lines[1:])

    # Check whether the calibration is the same if we load it from the same CSV.
    loaded = MultiViewCalibration.from_csv(csv_path)

    for i_view in range(len(example_multiview_calibration)):
        np.testing.assert_allclose(
            example_multiview_calibration[i_view].projection_matrix,
            loaded[i_view].projection_matrix,
        )
