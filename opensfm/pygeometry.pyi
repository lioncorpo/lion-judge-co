from typing import List, Tuple

from typing import overload
import Dict[opensfm.pygeometry
import List[numpy
import List[opensfm.pygeometry
import Tuple[bool,numpy
import Tuple[numpy.ndarray[float32[m,n]],numpy
import numpy
BROWN: Any
DUAL: Any
FISHEYE: Any
FISHEYE_OPENCV: Any
PERSPECTIVE: Any
SPHERICAL: Any
aspect_ratio: Any
focal: Any
k1: Any
k2: Any
k3: Any
k4: Any
p1: Any
p2: Any
transition: Any

def absolute_pose_n_points(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[3,4]]: ...
def absolute_pose_n_points_known_rotation(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[3,1]]: ...
def absolute_pose_three_points(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]]) -> List[numpy.ndarray[float64[3,4]]]: ...
def compute_camera_mapping(arg0: Camera, arg1: Camera, arg2: int, arg3: int) -> Tuple[numpy.ndarray[float32[m,n]],numpy.ndarray[float32[m,n]]]: ...
def essential_five_points(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]]) -> List[numpy.ndarray[float64[3,3]]]: ...
def essential_n_points(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]]) -> List[numpy.ndarray[float64[3,3]]]: ...
def relative_pose_from_essential(arg0: numpy.ndarray[float64[3,3]], arg1: numpy.ndarray[float64[m,3]], arg2: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[3,4]]: ...
def relative_pose_refinement(arg0: numpy.ndarray[float64[3,4]], arg1: numpy.ndarray[float64[m,3]], arg2: numpy.ndarray[float64[m,3]], arg3: int) -> numpy.ndarray[float64[3,4]]: ...
def relative_rotation_n_points(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[3,3]]: ...
def triangulate_bearings_dlt(arg0: List[numpy.ndarray[float64[3,4]]], arg1: numpy.ndarray[float64[m,3]], arg2: float, arg3: float) -> Tuple[bool,numpy.ndarray[float64[3,1]]]: ...
def triangulate_bearings_midpoint(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]], arg2: List[float], arg3: float) -> Tuple[bool,numpy.ndarray[float64[3,1]]]: ...
def triangulate_two_bearings_midpoint(arg0: numpy.ndarray[float64[2,3]], arg1: numpy.ndarray[float64[2,3]]) -> numpy.ndarray[float64[3,1]]: ...
def triangulate_two_bearings_midpoint_many(arg0: numpy.ndarray[float64[m,3]], arg1: numpy.ndarray[float64[m,3]], arg2: numpy.ndarray[float64[3,3]], arg3: numpy.ndarray[float64[3,1]]) -> List[numpy.ndarray[float64[3,1]]]: ...

class Camera:
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def create_brown(arg0: float, arg1: float, arg2: numpy.ndarray[float64[2,1]], arg3: numpy.ndarray[float64[m,1]]) -> Camera: ...
    @classmethod
    def create_dual(arg0: float, arg1: float, arg2: float, arg3: float) -> Camera: ...
    @classmethod
    def create_fisheye(arg0: float, arg1: float, arg2: float) -> Camera: ...
    @classmethod
    def create_fisheye_opencv(arg0: float, arg1: float, arg2: numpy.ndarray[float64[2,1]], arg3: numpy.ndarray[float64[m,1]]) -> Camera: ...
    @classmethod
    def create_perspective(arg0: float, arg1: float, arg2: float) -> Camera: ...
    @classmethod
    def create_spherical(self, *args, **kwargs) -> Any: ...
    def get_K(self) -> numpy.ndarray[float64[3,3]]: ...
    def get_K_in_pixel_coordinates(self, arg0: int, arg1: int) -> numpy.ndarray[float64[3,3]]: ...
    def get_parameters_map(self) -> Dict[opensfm.pygeometry.CameraParameters,float]: ...
    def get_parameters_types(self) -> List[opensfm.pygeometry.CameraParameters]: ...
    def get_parameters_values(self) -> numpy.ndarray[float64[m,1]]: ...
    @classmethod
    def is_panorama(arg0: str) -> bool: ...
    def pixel_bearing(self, arg0: numpy.ndarray[float64[2,1]]) -> numpy.ndarray[float64[3,1]]: ...
    def pixel_bearing_many(self, arg0: numpy.ndarray[float64[m,2]]) -> numpy.ndarray[float64[m,3]]: ...
    def project(self, arg0: numpy.ndarray[float64[3,1]]) -> numpy.ndarray[float64[2,1]]: ...
    def project_many(self, arg0: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[m,2]]: ...
    def set_parameter_value(self, arg0: CameraParameters, arg1: float) -> None: ...
    def __copy__(self) -> Camera: ...
    def __deepcopy__(self, arg0: dict) -> Camera: ...
    def __getstate__(self) -> tuple: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    @property
    def aspect_ratio(self) -> float: ...
    @aspect_ratio.setter
    def aspect_ratio(self, val: float) -> None: ...
    @property
    def distortion(self) -> numpy.ndarray[float64[m,1]]: ...
    @distortion.setter
    def distortion(self, val: numpy.ndarray[float64[m,1]]) -> None: ...
    @property
    def focal(self) -> float: ...
    @focal.setter
    def focal(self, val: float) -> None: ...
    @property
    def height(self) -> int: ...
    @height.setter
    def height(self, val: int) -> None: ...
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, val: str) -> None: ...
    @property
    def k1(self) -> float: ...
    @property
    def k2(self) -> float: ...
    @property
    def k3(self) -> float: ...
    @property
    def k4(self) -> float: ...
    @property
    def p1(self) -> float: ...
    @property
    def p2(self) -> float: ...
    @property
    def principal_point(self) -> numpy.ndarray[float64[2,1]]: ...
    @principal_point.setter
    def principal_point(self, val: numpy.ndarray[float64[2,1]]) -> None: ...
    @property
    def projection_type(self) -> str: ...
    @property
    def transition(self) -> float: ...
    @transition.setter
    def transition(self, val: float) -> None: ...
    @property
    def width(self) -> int: ...
    @width.setter
    def width(self, val: int) -> None: ...

class CameraParameters:
    aspect_ratio: Any = ...
    focal: Any = ...
    k1: Any = ...
    k2: Any = ...
    k3: Any = ...
    k4: Any = ...
    p1: Any = ...
    p2: Any = ...
    transition: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: CameraParameters) -> bool: ...
    def __getstate__(self) -> tuple: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: CameraParameters) -> bool: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    @property
    def __members__(self) -> dict: ...

class Pose:
    @overload
    def __init__(self, rotation: numpy.ndarray[float64[3,3]] = ..., translation: numpy.ndarray[float64[3,1]] = ...) -> None: ...
    @overload
    def __init__(self, rotation: numpy.ndarray[float64[3,1]] = ..., translation: numpy.ndarray[float64[3,1]] = ...) -> None: ...
    @overload
    def __init__(self, arg0: numpy.ndarray[float64[3,1]]) -> None: ...
    @overload
    def __init__(*args, **kwargs) -> Any: ...
    def compose(self, arg0: Pose) -> Pose: ...
    def get_R_cam_to_world(self) -> numpy.ndarray[float64[3,3]]: ...
    def get_R_cam_to_world_min(self) -> numpy.ndarray[float64[3,1]]: ...
    def get_R_world_to_cam(self) -> numpy.ndarray[float64[3,3]]: ...
    def get_R_world_to_cam_min(self) -> numpy.ndarray[float64[3,1]]: ...
    def get_Rt(self) -> numpy.ndarray[float64[3,4]]: ...
    def get_cam_to_world(self) -> numpy.ndarray[float64[4,4]]: ...
    def get_origin(self) -> numpy.ndarray[float64[3,1]]: ...
    def get_rotation_matrix(self) -> numpy.ndarray[float64[3,3]]: ...
    def get_t_cam_to_world(self) -> numpy.ndarray[float64[3,1]]: ...
    def get_t_world_to_cam(self) -> numpy.ndarray[float64[3,1]]: ...
    def get_world_to_cam(self) -> numpy.ndarray[float64[4,4]]: ...
    def inverse(self) -> Pose: ...
    def relative_to(self, arg0: Pose) -> Pose: ...
    @overload
    def set_from_cam_to_world(self, arg0: numpy.ndarray[float64[4,4]]) -> None: ...
    @overload
    def set_from_cam_to_world(self, arg0: numpy.ndarray[float64[3,3]], arg1: numpy.ndarray[float64[3,1]]) -> None: ...
    @overload
    def set_from_cam_to_world(self, arg0: numpy.ndarray[float64[3,1]], arg1: numpy.ndarray[float64[3,1]]) -> None: ...
    @overload
    def set_from_cam_to_world(*args, **kwargs) -> Any: ...
    @overload
    def set_from_world_to_cam(self, arg0: numpy.ndarray[float64[4,4]]) -> None: ...
    @overload
    def set_from_world_to_cam(self, arg0: numpy.ndarray[float64[3,3]], arg1: numpy.ndarray[float64[3,1]]) -> None: ...
    @overload
    def set_from_world_to_cam(self, arg0: numpy.ndarray[float64[3,1]], arg1: numpy.ndarray[float64[3,1]]) -> None: ...
    @overload
    def set_from_world_to_cam(*args, **kwargs) -> Any: ...
    def set_origin(self, arg0: numpy.ndarray[float64[3,1]]) -> None: ...
    def set_rotation_matrix(self, arg0: numpy.ndarray[float64[3,3]]) -> None: ...
    def transform(self, arg0: numpy.ndarray[float64[3,1]]) -> numpy.ndarray[float64[3,1]]: ...
    def transform_inverse(self, arg0: numpy.ndarray[float64[3,1]]) -> numpy.ndarray[float64[3,1]]: ...
    def transform_inverse_many(self, arg0: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[m,3]]: ...
    def transform_many(self, arg0: numpy.ndarray[float64[m,3]]) -> numpy.ndarray[float64[m,3]]: ...
    def __copy__(self) -> Pose: ...
    def __deepcopy__(self, arg0: dict) -> Pose: ...
    def __getstate__(self) -> tuple: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    @property
    def rotation(self) -> numpy.ndarray[float64[3,1]]: ...
    @rotation.setter
    def rotation(self, val: numpy.ndarray[float64[3,1]]) -> None: ...
    @property
    def translation(self) -> numpy.ndarray[float64[3,1]]: ...
    @translation.setter
    def translation(self, val: numpy.ndarray[float64[3,1]]) -> None: ...

class ProjectionType:
    BROWN: Any = ...
    DUAL: Any = ...
    FISHEYE: Any = ...
    FISHEYE_OPENCV: Any = ...
    PERSPECTIVE: Any = ...
    SPHERICAL: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: ProjectionType) -> bool: ...
    def __getstate__(self) -> tuple: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: ProjectionType) -> bool: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    @property
    def __members__(self) -> dict: ...
