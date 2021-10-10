"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730214639"


def test_only_evens_empty() -> None:
    """Edge case for only evens function."""
    assert only_evens([]) == []


def test_only_evens_single() -> None:
    """Use case for only evens function."""
    assert only_evens([1, 2]) == [2]


def test_only_evens_multiple() -> None:
    """Use case for only evens function."""
    assert only_evens([1, 2, 4, 3]) == [2, 4]


def test_sub_empty() -> None:
    """Edge case for sub function."""
    assert sub([], 0, 0) == []


def test_sub_single() -> None:
    """Use case for sub function."""
    assert sub([10, 20, 30], 0, 1) == [10]


def test_sub_multiple() -> None:
    """Use case for a sub function."""
    assert sub([10, 20, 30], 0, 2) == [10, 20]


def test_concat_empty() -> None:
    """Edge case for concat function."""
    assert concat([], []) == []


def test_concat_single() -> None:
    """Use case for concat function."""    
    assert concat([1], [2]) == [1, 2]


def test_concat_mutliple() -> None:
    """Use case for concat function."""
    assert concat([1], [2, 3]) == [1, 2, 3]