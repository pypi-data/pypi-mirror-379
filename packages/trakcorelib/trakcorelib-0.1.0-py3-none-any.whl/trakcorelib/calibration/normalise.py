"""Functions for normalising points."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    import numpy.typing as npt


class Normaliser:
    """A transformer that normalises 2D or 3D points.

    This transform the origin of the points and scales the points by the same
    factor in all dimensions.

    It can also invert the normalisation to convert normalised points to
    regular points.
    """

    def __init__(self, origin: npt.ArrayLike, length_scale: float) -> None:
        """Initialise a normaliser.

        Args:
            origin: Origin of the normalised coordinate system.
            length_scale: Length scale for which a point is transformed to a
                distance of 1 in the normalised coordinate system.

        """
        origin_arr = np.asarray(origin, dtype=np.float64)
        self.num_dims = origin_arr.size

        if origin_arr.ndim > 1 or not 2 <= self.num_dims <= 3:
            msg = (
                "The origin of the normalised coordinate system should be"
                "specified as a 1D array with 2 or 3 values."
            )
            raise ValueError(msg)

        if self.num_dims == 2:
            self.normalised_to_regular = np.array(
                [
                    [length_scale, 0, origin_arr[0]],
                    [0, length_scale, origin_arr[1]],
                    [0, 0, 1],
                ],
                dtype=np.float64,
            )
        else:
            self.normalised_to_regular = np.array(
                [
                    [length_scale, 0, 0, origin_arr[0]],
                    [0, length_scale, 0, origin_arr[1]],
                    [0, 0, length_scale, origin_arr[2]],
                    [0, 0, 0, 1],
                ],
                dtype=np.float64,
            )

        # Also compute the inverse transformation.
        self.regular_to_normalised = np.linalg.inv(self.normalised_to_regular)

    @property
    def origin(self) -> npt.NDArray[np.float64]:
        """Origin of the normalised coordinate system."""
        return self.normalised_to_regular[:, -1].squeeze()

    @property
    def length_scale(self) -> float:
        """Scale of the normalised coordinate system."""
        length_scale: float = self.normalised_to_regular[0, 0]
        return length_scale

    def to_normalised(self, points: npt.ArrayLike) -> npt.NDArray[np.float64]:
        """Transform regular points to normalised points.

        Args:
            points: Points to transform, with points on the rows and dimensions
                on the columns.

        Returns:
            Normalised points as a NumPy array with points on the rows and
            dimensions on the columns.

        """
        points_homogeneous = self._to_homogeneous_coordinates(points)
        normalised = self.regular_to_normalised @ points_homogeneous.T
        return normalised[:-1, :].T

    def from_normalised(self, points: npt.ArrayLike) -> npt.NDArray[np.float64]:
        """Transform normalised points to regular points.

        Args:
            points: Points to transform, with points on the rows and dimensions
                on the columns.

        Returns:
            De-normalised points as a NumPy array with points on the rows and
            dimensions on the columns.

        """
        points_homogeneous = self._to_homogeneous_coordinates(points)
        denormalised = self.normalised_to_regular @ points_homogeneous.T
        return denormalised[:-1, :].T

    def _to_homogeneous_coordinates(
        self,
        points: npt.ArrayLike,
    ) -> npt.NDArray[np.float64]:
        """Convert an array of points to homogeneous coordinates."""
        points_arr = np.asarray(points, dtype=np.float64)
        if points_arr.ndim != 2 or points_arr.shape[1] != self.num_dims:
            msg = (
                "Points should should be specified as a 2D array with the same "
                f"number of rows as points and {self.num_dims} columns."
            )
            raise ValueError(msg)

        # Append a column of ones to the points, ignore extra dimensions.
        return np.hstack(
            (points_arr, np.ones((points_arr.shape[0], 1))),
        )

    @classmethod
    def from_points(cls, points: npt.ArrayLike) -> Normaliser:
        """Create a normaliser from a set of points.

        This uses the mean coordinates of the points as the origin of the
        coordinate system, and the standard deviation of all coordinates
        together as the length scale.

        Args:
            points: Points to create a normaliser for, a N x M array, where N is
                the number of points, and M is the number of dimensions.

        Returns:
            A normaliser for the specified set of points.

        """
        points_arr = np.asarray(points, dtype=np.float64)
        origin = np.mean(points_arr, axis=0)
        length_scale = np.std(points_arr)
        return cls(origin, float(length_scale))
