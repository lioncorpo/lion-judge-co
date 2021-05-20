from distutils.version import LooseVersion

import pytest
import numpy as np

from collections import defaultdict
from itertools import combinations

from opensfm import multiview
from opensfm.synthetic_data import synthetic_examples


def pytest_configure(config):
    use_legacy_numpy_printoptions()


def use_legacy_numpy_printoptions():
    """Ensure numpy use legacy print formant."""
    if LooseVersion(np.__version__).version[:2] > [1, 13]:
        np.set_printoptions(legacy='1.13')


@pytest.fixture(scope='module')
def scene_synthetic():
    np.random.seed(42)
    data = synthetic_examples.synthetic_ellipse_scene()

    maximum_depth = 40
    projection_noise = 1.0
    gps_noise = 5.0

    exifs = data.get_scene_exifs(gps_noise)
    features, desc, colors, graph = data.get_tracks_data(maximum_depth,
                                                         projection_noise)
    return data, exifs, features, desc, colors, graph


@pytest.fixture(scope='session')
def scene_synthetic_cube():
    np.random.seed(42)
    data = synthetic_examples.synthetic_cube_scene()
    _, _, _, tracks_manager = data.get_tracks_data(40, 0.0)
    return data.get_reconstruction(), tracks_manager


@pytest.fixture(scope='module')
def pairs_and_poses():
    np.random.seed(42)
    data = synthetic_examples.synthetic_cube_scene()
    reconstruction = data.get_reconstruction()

    scale = 0.0
    features, _, _, tracks_manager = data.get_tracks_data(40, scale)

    points_keys = list(reconstruction.points.keys())
    pairs, poses = defaultdict(list), defaultdict(list)
    for (im1, im2), tuples in tracks_manager.get_all_common_observations_all_pairs().items():
        f1 = [p.point for k, p, _ in tuples if k in points_keys]
        f2 = [p.point for k, _, p in tuples if k in points_keys]
        pairs[im1, im2].append((f1, f2))
        poses[im1, im2] = reconstruction.shots[im2].pose.\
            compose(reconstruction.shots[im1].pose.inverse())

    camera = list(reconstruction.cameras.values())[0]
    return pairs, poses, camera, features, tracks_manager, reconstruction


@pytest.fixture(scope='module')
def pairs_and_their_E(pairs_and_poses):
    pairs, poses, camera, _, _, _ = pairs_and_poses

    pairs = list(sorted(zip(pairs.values(), poses.values()), key=lambda x: -len(x[0])))

    num_pairs = 20
    indices = [np.random.randint(0, len(pairs)-1) for i in range(num_pairs)]

    ret_pairs = []
    for idx in indices:
        pair = pairs[idx]

        f1 = camera.pixel_bearing_many(np.array([x for x, _ in pair[0]]))
        f2 = camera.pixel_bearing_many(np.array([x for _, x in pair[0]]))

        pose = pair[1]
        R = pose.get_rotation_matrix()
        t_x = multiview.cross_product_matrix(pose.get_origin())
        e = R.dot(t_x)
        e /= np.linalg.norm(e)

        ret_pairs.append((f1, f2, e, pose))
    return ret_pairs


@pytest.fixture(scope='module')
def shots_and_their_points(pairs_and_poses):
    _, _, _, _, tracks_manager, reconstruction = pairs_and_poses

    ret_shots = []
    for shot in reconstruction.shots.values():
        bearings, points = [], []
        for k, obs in tracks_manager.get_shot_observations(shot.id).items():
            if k not in reconstruction.points:
                continue
            p = reconstruction.points[k]
            bearings.append(shot.camera.pixel_bearing(obs.point))
            points.append(p.coordinates)
        ret_shots.append((shot.pose, np.array(bearings), np.array(points)))

    return ret_shots
