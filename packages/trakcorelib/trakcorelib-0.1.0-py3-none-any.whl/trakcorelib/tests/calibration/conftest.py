from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import pytest

if TYPE_CHECKING:
    import numpy.typing as npt


@pytest.fixture
def example_calibration_data() -> tuple[
    npt.NDArray[np.float64], list[npt.NDArray[np.float64]]
]:
    # These example data were taken from the original implementation in
    # FLiTrak3D, which in turn took them from the following archived mailing
    # list:
    #
    #     https://www.mail-archive.com/floatcanvas@mithis.com/msg00513.html

    # Coordinates in centimetres of the corners of a cube; the measurement error
    # is at least 0.2 cm.
    object_points = np.array(
        [
            [0, 0, 0],
            [0, 12.3, 0],
            [14.5, 12.3, 0],
            [14.5, 0, 0],
            [0, 0, 14.5],
            [0, 12.3, 14.5],
            [14.5, 12.3, 14.5],
            [14.5, 0, 14.5],
        ],
        dtype=np.float64,
    )

    # Image coordinates (in pixels) of 4 different views of the cube.
    image_points = [
        np.array(
            [
                [1302, 1147],
                [1110, 976],
                [1411, 863],
                [1618, 1012],
                [1324, 812],
                [1127, 658],
                [1433, 564],
                [1645, 704],
            ],
            dtype=np.float64,
        ),
        np.array(
            [
                [1094, 1187],
                [1130, 956],
                [1514, 968],
                [1532, 1187],
                [1076, 854],
                [1109, 647],
                [1514, 659],
                [1523, 860],
            ],
            dtype=np.float64,
        ),
        np.array(
            [
                [1073, 866],
                [1319, 761],
                [1580, 896],
                [1352, 1016],
                [1064, 545],
                [1304, 449],
                [1568, 557],
                [1313, 668],
            ],
            dtype=np.float64,
        ),
        np.array(
            [
                [1205, 1511],
                [1193, 1142],
                [1601, 1121],
                [1631, 1487],
                [1157, 1550],
                [1139, 1124],
                [1628, 1100],
                [1661, 1520],
            ],
            dtype=np.float64,
        ),
    ]
    return object_points, image_points
