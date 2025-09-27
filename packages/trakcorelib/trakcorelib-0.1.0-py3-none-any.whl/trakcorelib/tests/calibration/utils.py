import numpy as np

from trakcorelib.calibration.camera import CameraProperties


def compare_camera_properties(
    a: CameraProperties, b: CameraProperties, atol: float = 1e-6
) -> None:
    """Compare camera properties for almost equality."""
    np.isclose(a.intrinsic.u_principal, b.intrinsic.u_principal, atol=atol)
    np.isclose(a.intrinsic.v_principal, b.intrinsic.v_principal, atol=atol)
    np.isclose(a.intrinsic.focal_length_u, b.intrinsic.focal_length_u, atol=atol)
    np.isclose(a.intrinsic.focal_length_v, b.intrinsic.focal_length_v, atol=atol)

    np.isclose(a.extrinsic.coords, b.extrinsic.coords, atol=atol)
    np.isclose(a.extrinsic.rotation.elements, b.extrinsic.rotation.elements, atol=atol)
