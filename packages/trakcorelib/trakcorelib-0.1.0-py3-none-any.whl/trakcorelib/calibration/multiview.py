"""Multi-view camera calibration class definition."""

from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

import numpy as np

from trakcorelib.calibration.camera import DltCameraCalibration

if TYPE_CHECKING:
    import os
    from collections.abc import Iterable

    import numpy.typing as npt


class MultiViewCalibration:
    """Calibration for multiple camera views simultaneously."""

    def __init__(
        self,
        calibrations: Iterable[DltCameraCalibration],
        names: Iterable[str] | None = None,
    ) -> None:
        """Initialise a multi-view camera calibration.

        Args:
            calibrations: Calibrations for the individual views.
            names: Optional names for each of the views. If not specified, they
                are named "view001", "view002", ...

        """
        self._calibrations = list(calibrations)

        if names is None:
            self._names = [f"view{i + 1}" for i in range(len(self._calibrations))]
        else:
            self._names = list(names)
            if len(self._names) != len(self._calibrations):
                msg = (
                    "Specify the same number of names as individual camera "
                    "calibrations."
                )
                raise ValueError(msg)

    @property
    def names(self) -> list[str]:
        """Names of the individual views."""
        return self._names

    def __len__(self) -> int:
        """Retrieve the number of views in the calibration."""
        return len(self._calibrations)

    def __getitem__(self, index: int) -> DltCameraCalibration:
        """Retrieve the calibration of the view at the specified index.

        Args:
            index: Index of the view for which to retrieve the calibration.

        Returns:
            The calibration for the specified view.

        """
        return self._calibrations[index]

    def reconstruct_object_point(
        self,
        image_points: npt.ArrayLike,
    ) -> tuple[float, float, float]:
        """Reconstructs object point coordinates from image points from multiple views.

        Args:
            image_points: Image points for which to reconstruct object point
                coordinates. The points should be specified as an N x 2 array,
                where N is the number of views in this calibration.

        Returns:
            The object point reconstructed from the specified image points, as
            a 3-tuple.

        """
        image_points_arr = np.asarray(image_points, dtype=np.float64)

        num_views = len(self._calibrations)
        if num_views == 1:
            msg = "Cannot reconstruct 3D points from a single camera view."
            raise ValueError(msg)
        if image_points_arr.shape != (num_views, 2):
            msg = f"Specify the image points as a {num_views} x 2 array."
            raise ValueError(msg)

        # The DLT projection matrix is defined as follows:
        #
        #     [ L1 L2  L3  L4  ][ x ]   [ uw ]
        #     [ L5 L6  L7  L8  ][ y ] = [ vw ]
        #     [ L9 L10 L11 L12 ][ z ]   [ w  ]
        # .                     [ 1 ]
        #
        # Hence, for each image point, we get the following equations in object
        # point coordinates x, y, and z:
        #
        #     L1 x + L2 y + L3 z + L4 = u w
        #     L5 x + L6 y + L7 z + L8 = v w
        #     L9 x + L10 y + L11 z + L12 = w
        #
        # Eliminating w, this leaves two equations for each image point:
        #
        #     L1 x + L2 y + L3 z + L4 = u (L9 x + L10 y + L11 z + L12)
        #     L5 x + L6 y + L7 z + L8 = v (L9 x + L10 y + L11 z + L12)
        #
        # Simplifying and grouping coefficients:
        #
        #     (L1 - L9 u) x + (L2 - L10 u) y + (L3 - L11 u) z = L12 u - L4
        #     (L5 - L9 v) x + (L6 - L10 v) y + (L4 - L11 v) z = L12 v - L8
        #
        # These equations allow us to set up an overdetermined system of
        # equations that we can solve with least squares.
        num_equations = 2 * num_views
        system = np.zeros((num_equations, 3))
        rhs = np.zeros((num_equations,))
        for i_view in range(num_views):
            l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11 = self._calibrations[
                i_view
            ].coefficients
            l12 = 1.0

            u, v = image_points_arr[i_view, :]

            i_eqn_u = 2 * i_view
            system[i_eqn_u, :] = [l1 - l9 * u, l2 - l10 * u, l3 - l11 * u]
            rhs[i_eqn_u] = l12 * u - l4

            i_eqn_v = 2 * i_view + 1
            system[i_eqn_v, :] = [l5 - l9 * v, l6 - l10 * v, l7 - l11 * v]
            rhs[i_eqn_v] = l12 * v - l8

        # Solve the system with least squares.
        sol = np.linalg.lstsq(system, rhs)
        return tuple(sol[0])

    def to_csv(self, path: str | os.PathLike[str]) -> None:
        """Save the multi-view calibration as a CSV file.

        Each row is a specific coefficient, specified for each camera along the
        columns.

        Args:
            path: Path to save the calibration to.

        """
        csv_path = pathlib.Path(path)
        if csv_path.exists():
            msg = f'Specified path "{csv_path}" already exists.'
            raise ValueError(msg)

        # Create header and concatenate all DLT coefficients along the columns.
        header = ",".join(self.names)
        data = np.stack(
            [calibration.coefficients for calibration in self._calibrations],
            axis=1,
        )
        np.savetxt(csv_path, data, header=header, delimiter=",")

    @classmethod
    def from_csv(cls, path: str | os.PathLike[str]) -> MultiViewCalibration:
        """Load a multi-view calibration from a CSV file.

        Args:
            path: Path to load the calibration from.

        Returns:
            Initialised multi-view calibration.

        """
        csv_path = pathlib.Path(path)
        with csv_path.open() as file:
            header = file.readline()
            raw = np.loadtxt(file, delimiter=",")

        names = [name.strip() for name in header.lstrip("#").split(",")]

        num_views = len(names)
        calibrations = (
            DltCameraCalibration.from_coefficients(raw[:, i_view])
            for i_view in range(num_views)
        )
        return MultiViewCalibration(calibrations, names)
