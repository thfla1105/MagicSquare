import copy

import pytest


@pytest.fixture
def tq_01_grid() -> list[list[int]]:
    return [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 15, 0],
    ]


@pytest.fixture
def tq_nosol_grid() -> list[list[int]]:
    return [
        [0, 3, 2, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 0, 1],
    ]


@pytest.fixture
def deep_copy():
    return copy.deepcopy
