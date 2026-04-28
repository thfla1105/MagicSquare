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
def tq_first_attempt_ok_grid() -> list[list[int]]:
    """Valid 4×4 with two zeros; FR-05 placement1 (low→first empty, high→second) already yields magic sum 34."""
    return [
        [16, 0, 2, 0],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def deep_copy():
    return copy.deepcopy
