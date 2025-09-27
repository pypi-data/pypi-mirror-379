"""DLT camera calibration class."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

import numpy as np
import pyquaternion

from trakcorelib.calibration.utils import (
    orthogonalise_rotation_matrix,
    validate_object_image_points,
)

if TYPE_CHECKING:
    import numpy.typing as npt


@dataclasses.dataclass
class IntrinsicProperties:
    """Intrinsic camera properties.

    Attributes:
        u_principal: u-coordinate of principal point in pixels.
        v_principal: v-coordinate of principal point in pixels.
        focal_length_u: Focal length along u in pixels.
        focal_length_v: Focal length along v in pixels.

    """

    u_principal: float
    v_principal: float
    focal_length_u: float
    focal_length_v: float


@dataclasses.dataclass
class ExtrinsicProperties:
    """Extrinsic camera properties.

    Returns:
        coord: Camera x, y, z coordinates.
        rotation: Quaternion describing the rotation of the camera from
            [0, 0, 1] to its actual orientation.

    """

    coords: tuple[float, float, float]
    rotation: pyquaternion.Quaternion


@dataclasses.dataclass
class CameraProperties:
    """Camera properties.

    Attributes:
        intrinsic: Intrinsic camera properties.
        extrinsic: Extrinsic camera properties.

    """

    intrinsic: IntrinsicProperties
    extrinsic: ExtrinsicProperties


class DltCameraCalibration:
    """A 3D DLT camera calibration."""

    def __init__(self, projection_matrix: npt.ArrayLike) -> None:
        """Initialise a DLT camera calibration.

        Args:
            projection_matrix: Projection matrix (3 x 4) from object coordinates
                to camera coordinates.

        """
        self._projection_matrix = np.asarray(projection_matrix, dtype=np.float64)

        if self._projection_matrix.shape != (3, 4):
            msg = "Projection matrix should be 3 x 4."
            raise ValueError(msg)

    @property
    def projection_matrix(self) -> npt.NDArray[np.float64]:
        """Projection matrix transforming object coordinates to camera coordinates."""
        return self._projection_matrix

    @property
    def coefficients(self) -> npt.NDArray[np.float64]:
        """Array with 11 independent DLT coefficients for this calibration."""
        # Flatten the projection matrix in row-major order.
        coefs = self._projection_matrix.flatten("C")
        # Drop the last coefficient as it is always 1.
        return coefs[:-1]

    def project(self, object_points: npt.ArrayLike) -> npt.NDArray[np.float64]:
        """Projects object points to camera coordinates.

        Args:
            object_points: Points in object coordinates (N x 3).

        Returns:
            Points in camera coordinates (N x 2).

        """
        points_arr = np.asarray(object_points, dtype=np.float64)
        # If we specify a single point, make sure we still get a 1 x 3 array.
        is_single_point = points_arr.ndim == 1
        if is_single_point:
            points_arr = points_arr[np.newaxis, :]

        if points_arr.shape[1] != 3:
            msg = "Specify the object points as an N x 3 array."
            raise ValueError(msg)

        num_points = points_arr.shape[0]
        points_homogeneous = np.hstack((points_arr, np.ones((num_points, 1))))

        # Project homogeneous object coordinates to homogeneous image coordinates.
        image_points_homogeneous = self._projection_matrix @ points_homogeneous.T

        # Perform perspective division to obtain the final image coordinates.
        uv: npt.NDArray[np.float64] = image_points_homogeneous[:-1, :].T
        w: npt.NDArray[np.float64] = image_points_homogeneous[-1, :].T

        image_points = uv / w[:, np.newaxis]
        return image_points if not is_single_point else image_points[0, :]

    def compute_reprojection_rms_error(
        self,
        object_points: npt.ArrayLike,
        image_points: npt.ArrayLike,
    ) -> float:
        """Compute the root mean square reprojection error.

        Args:
            object_points: Points in object coordinates (N x 3).
            image_points: Points in image coordinates (N x 2).

        Returns:
            The root mean square reprojection error of this calibration, given
            the specified object points and image points.

        """
        object_points_arr, image_points_arr = validate_object_image_points(
            object_points,
            image_points,
        )
        reprojected = self.project(object_points_arr)
        error_distances_squared: npt.NDArray[np.float64] = np.sum(
            (image_points_arr - reprojected) ** 2,
            axis=1,
        )
        rms_error: float = np.sqrt(np.mean(error_distances_squared))
        return rms_error

    def compute_camera_properties(self) -> CameraProperties:
        """Compute camera properties from the camera calibration.

        Note that these computations assume that the camera rotation matrix is
        orthogonal, which is not necessarily the case when using "classic" DLT.

        Returns:
            Intrinsic and extrinsic camera properties.

        """
        # We use a definition of the camera properties as detailed in
        #
        #     https://en.wikipedia.org/wiki/Camera_resectioning#Projection
        #
        # Here, the camera matrix L projects homogeneous object coordinates x'
        # to homogeneous image coordinates u':
        #
        #     L x' = u'
        #
        # We use the following definition for the coefficients of the matrix L:
        #
        #     [ L1  L2  L3  L4  ]
        #     [ L5  L6  L7  L8  ]
        #     [ L9  L10 L11 L12 ]
        #
        # The matrix L can be computed by multiplying the intrinsic matrix K by
        # the extrinsic matrix [R T]:
        #
        #     K [R T] x' = u'
        #
        # The matrix K is defined as:
        #
        #         [ fu 0  up ]
        #     K = [ 0  fv vp ]
        #         [ 0  0  1  ]
        #
        # The matrix R is a transformation matrix from world coordinates to
        # camera coordinates, and T is the origin of the world coordinate system
        # expressed in camera coordinates.
        #
        # Multiplying the two gives the following expression for the DLT matrix
        # coefficients:
        #
        # .   L1 = fu R11 + up R31
        # .   L2 = fu R12 + up R32
        # .   L3 = fu R13 + up R33
        # .   L4 = fu T1 + up T3
        # .   L5 = fv R21 + vp R31
        # .   L6 = fv R22 + vp R32
        # .   L7 = fv R23 + vp R33
        # .   L8 = fv T2 + vp T3
        # .   L9 = R31
        # .   L10 = R32
        # .   L11 = R33
        # .   L12 = T3
        #
        # Our rescaling of the matrix by defining L12 as 1 will in general
        # result in a matrix R with rows/columns that are not unit length. Since
        # R should be an orthogonal matrix (implying unit length basis vectors),
        # we rescale the entire matrix to make sure this is the case. The
        # current length of the basis vectors of R is:
        #
        # .    l = sqrt(R31^2 + R32^2 + R33^2)
        #
        # Or, given the definition of the coefficients:
        #
        # .    l = sqrt(L9^2 + L10^2 + L11^2)
        #
        # So we divide the entire matrix by 1 / l to make sure R is an
        # orthonormal matrix.
        l9_scaled, l10_scaled, l11_scaled = self._projection_matrix[2, :3]
        basis_vector_length: float = np.sqrt(
            l9_scaled**2 + l10_scaled**2 + l11_scaled**2,
        )
        rescaled_matrix = self._projection_matrix / basis_vector_length

        l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12 = rescaled_matrix.flatten("C")

        # To compute the principal points, we use:
        #
        #     up = L1 L9 + L2 L10 + L3 L11
        #     vp = L5 L9 + L6 L10 + L7 L11
        #
        #     up = L1 L9 + L2 L10 + L3 L11
        #        =   fu R11 R31 + up R31^2
        #          + fu R12 R32 + up R32^2
        #          + fu R13 R33 + up R33^2
        #        =   fu (R11 R31 + R12 R32 + R13 R33)
        # .        + up (R31^2 + R32^2 + R33^2)
        #
        # If we assume that R is an orthogonal matrix (which is to be expected
        # from a rotation matrix), we know:
        #
        #     - both rows and columns of the matrix are unit basis vectors;
        #     - the dot product between different rows and columns is hence zero
        #       due to orthogonality of the basis vectors;
        #     - the basis vectors are length 1.
        #
        # Hence:
        #
        #     R11 R31 + R12 R32 + R13 R33 = 0
        #     R31^2 + R32^2 + R33^2 = 1
        #
        # So:
        #
        #     up = fu * 0 + up * 1 = up
        #
        # Therefore, our expression for up is indeed valid. A similar derivation
        # can be done for the principal point in the y-direction.
        up = l1 * l9 + l2 * l10 + l3 * l11
        vp = l5 * l9 + l6 * l10 + l7 * l11

        # To compute the focal lengths, we use:
        # .   fu = sqrt(
        # .                ( up * L9 - L1 )^2
        # .              + ( up * L10 - L2 )^2
        # .              + ( up * L11 - L3 )^2
        # .            )
        #        = sqrt(
        # .                ( up R31 - ( fu R11 + up R31 ) )^2
        # .                ( up R32 - ( fu R12 + up R32 ) )^2
        # .                ( up R33 - ( fu R13 + up R33 ) )^2
        # .            )
        # .      = sqrt( fu^2 ( R11^2 + R12^2 + R13^2 ) )
        # .      = fu sqrt( R11^2 + R12^2 + R13^2 )
        #
        # Again, the rows/columns of R are unit length, so this reduces to:
        #
        #     fu = fu * 1 = fu
        #
        # So this is valid expression for fu. The focal length in y-direction
        # can be computed with a similar reasoning. Note that it should in
        # general (for square pixels) be approximately the same as the focal
        # length in x-direction.
        fu: float = np.sqrt(
            (up * l9 - l1) ** 2 + (up * l10 - l2) ** 2 + (up * l11 - l3) ** 2,
        )
        fv: float = np.sqrt(
            (vp * l9 - l5) ** 2 + (vp * l10 - l6) ** 2 + (vp * l11 - l7) ** 2,
        )

        # We can compute the coefficients of the transformation matrix
        # straightforwardly now:
        #
        # .   R11 = (L1 - up * L9) / fu = (fu R11 + up R31 - up * R31) / fu
        # .   R12 = (L2 - up * L10) / fu
        # .   R13 = (L3 - up * L11) / fu
        # .   R21 = (L5 - vp * L9) / fv
        # .   R22 = (L6 -vp * L10) / fv
        # .   R23 = (L7 - vp * L11) / fv
        # .   R31 = L9
        # .   R32 = L10
        # .   R33 = L11
        #
        # In addition, to get a consistent rotation matrix regardless of scaling
        # we make sure that its determinant is always 1 (the alternative being
        # -1 for an orthogonal matrix).
        #
        # The transformation matrix transform from world coordinates to camera
        # coordinates, i.e. it expresses the basis vectors of the world
        # coordinate system in the camera coordinate system. To get the rotation
        # matrix for the camera, we need to transpose (i.e. invert) this matrix
        # to get the basis vectors of the camera coordinates. This is a rotation
        # matrix in world coordinates for the camera itself.
        world_to_camera = np.array(
            [
                [(l1 - up * l9) / fu, (l2 - up * l10) / fu, (l3 - up * l11) / fu],
                [(l5 - vp * l9) / fv, (l6 - vp * l10) / fv, (l7 - vp * l11) / fv],
                [l9, l10, l11],
            ],
            dtype=np.float64,
        )

        do_negate_transformation = np.linalg.det(world_to_camera) < 0
        if do_negate_transformation:
            world_to_camera *= -1
            # Note that we also negate the matrix coefficients L4, L8 and L12
            # below, for computing the translation. The negation does not matter
            # for the principal points and focal lengths, so we do not need to
            # adjust those.

        # When the calibration has been computed with DLT, the rotation matrix
        # may not be exactly orthogonal, which leads to problems when creating a
        # quaternion. Hence, we orthogonalise the matrix. This is a no-op when
        # the matrix is already orthogonal
        rotation_matrix = orthogonalise_rotation_matrix(world_to_camera.T)

        # Convert to quaternion.
        rotation = pyquaternion.Quaternion(matrix=rotation_matrix).normalised

        # The translation component T = [T1, T2, T3] expresses the position of
        # the world coordinate system origin in camera coordinates. We can
        # compute it from coefficients the following system of linear equations:
        #
        # .   fu T1 + up T3 = L4
        # .   fv T2 + vp T3 = L8
        # .   T3 = L12
        #
        # We can then compute the camera position in world coordinates with:
        #
        #     C = -R^T T
        #
        # Where R is the transformation matrix from world to camera coordinates,
        # so its inverse R^T is our camera rotation matrix.
        system = np.array(
            [
                [fu, 0, up],
                [0, fv, vp],
                [0, 0, 1],
            ],
            dtype=np.float64,
        )
        rhs = np.array([l4, l8, l12])
        if do_negate_transformation:
            rhs *= -1

        translation_world_to_camera = np.linalg.solve(system, rhs)

        camera_position_arr = -rotation_matrix @ translation_world_to_camera
        camera_position: tuple[float, float, float] = tuple(camera_position_arr)

        intrinsic = IntrinsicProperties(up, vp, fu, fv)
        extrinsic = ExtrinsicProperties(camera_position, rotation)

        return CameraProperties(intrinsic, extrinsic)

    @classmethod
    def from_camera_properties(
        cls,
        properties: CameraProperties,
    ) -> DltCameraCalibration:
        """Create a DLT camera calibration from camera properties.

        We use the properties to set up a projection matrix, and then rescale
        that matrix such that coefficient L12 = 1. This gives consistent results
        with our DLT estimation functions.

        Args:
            properties: Camera properties to create a calibration for.

        Returns:
            A new 3D DLT camera calibration that satisfies the specified
            properties.

        """
        # We use the same definition of the DLT matrix as in the method
        # computing the camera properties:
        #
        #     L = K [R T]
        #
        # Where the matrix K is defined as:
        #
        #         [ fu 0  up ]
        #     K = [ 0  fv vp ]
        #         [ 0  0  1  ]
        #
        # The matrix R is a transformation matrix from world to camera
        # coordinates, and the vector T expresses the coordinates of the world
        # coordinate system in camera coordinates.
        fu = properties.intrinsic.focal_length_u
        fv = properties.intrinsic.focal_length_v
        up = properties.intrinsic.u_principal
        vp = properties.intrinsic.v_principal
        intrinsic_matrix = np.array(
            [[fu, 0, up], [0, fv, vp], [0, 0, 1]],
            dtype=np.float64,
        )

        camera_to_world: npt.NDArray[np.float64] = (
            properties.extrinsic.rotation.rotation_matrix
        )
        world_to_camera = camera_to_world.T

        # We have the position of the camera in world coordinates C:
        #
        #     C = -R^T T
        #
        # Hence the position of the world origin in camera coordinates T is:
        #
        #     T = -R C
        #
        position = np.asarray(properties.extrinsic.coords, dtype=np.float64)
        translation = -world_to_camera @ position

        # Compute the extrinsic matrix [3 x 4].
        extrinsic_matrix = np.hstack((world_to_camera, translation[:, np.newaxis]))

        # Compute the final DLT matrix.
        projection_matrix = intrinsic_matrix @ extrinsic_matrix

        # Make sure that the entire matrix is scaled such that coefficient
        # L12 is 1.
        l12_unscaled = projection_matrix[-1, -1]
        # We cannot do the rescaling if the camera is in the origin of the world
        # coordinate system in z-direction, as this would mean L12 = 0.
        if np.isclose(l12_unscaled, 0):
            msg = (
                "Camera cannot be in the origin of the world coordinate"
                "system. Please add a coordinate offset to the all cameras in "
                "your system."
            )
            raise ValueError(msg)
        projection_matrix /= l12_unscaled

        return cls(projection_matrix)

    @classmethod
    def from_coefficients(cls, coefficients: npt.ArrayLike) -> DltCameraCalibration:
        """Create a DLT camera calibration from an array of coefficients.

        Args:
            coefficients: Array with 11 DLT coefficients. We assume that the
                12th coefficient is always 1.

        Returns:
            A new 3D DLT camera calibration with the specified coefficients.

        """
        coefs_arr = np.asarray(coefficients, dtype=np.float64)
        if coefs_arr.shape != (11,):
            msg = "Specify the DLT coefficients as a 1D array with 11 coefficients."
            raise ValueError(msg)

        coefs_arr = np.append(coefs_arr, 1)
        projection_matrix = coefs_arr.reshape((3, 4))

        return cls(projection_matrix)
