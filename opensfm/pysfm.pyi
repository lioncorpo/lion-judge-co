from typing import List, Tuple

import Dict[str,opensfm.pysfm
import List[Tuple[str,opensfm.pysfm.Observation,opensfm.pysfm

def count_tracks_per_shot(arg0: TracksManager, arg1: List[str], arg2: List[str]) -> Dict[str,int]: ...

class Observation:
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...
    @property
    def color(self) -> numpy.ndarray[int32[3,1]]: ...
    @color.setter
    def color(self, val: numpy.ndarray[int32[3,1]]) -> None: ...
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, val: int) -> None: ...
    @property
    def point(self) -> numpy.ndarray[float64[2,1]]: ...
    @point.setter
    def point(self, val: numpy.ndarray[float64[2,1]]) -> None: ...
    @property
    def scale(self) -> float: ...
    @scale.setter
    def scale(self, val: float) -> None: ...

class TracksManager:
    def __init__(self) -> None: ...
    def add_observation(self, arg0: str, arg1: str, arg2: Observation) -> None: ...
    def as_string(self) -> str: ...
    def construct_sub_tracks_manager(self, arg0: List[str], arg1: List[str]) -> TracksManager: ...
    def get_all_common_observations(self, arg0: str, arg1: str) -> List[Tuple[str,opensfm.pysfm.Observation,opensfm.pysfm.Observation]]: ...
    def get_all_pairs_connectivity(self, shots: List[str] = ..., tracks: List[str] = ...) -> Dict[Tuple[str,str],int]: ...
    def get_observation(self, arg0: str, arg1: str) -> Observation: ...
    def get_shot_ids(self) -> List[str]: ...
    def get_shot_observations(self, arg0: str) -> Dict[str,opensfm.pysfm.Observation]: ...
    def get_track_ids(self) -> List[str]: ...
    def get_track_observations(self, arg0: str) -> Dict[str,opensfm.pysfm.Observation]: ...
    @classmethod
    def instanciate_from_file(arg0: str) -> TracksManager: ...
    @classmethod
    def instanciate_from_string(arg0: str) -> TracksManager: ...
    def num_shots(self) -> int: ...
    def num_tracks(self) -> int: ...
    def remove_observation(self, arg0: str, arg1: str) -> None: ...
    def write_to_file(self, arg0: str) -> None: ...
