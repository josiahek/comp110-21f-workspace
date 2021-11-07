"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730214639"


def test_invert_empty() -> None:
    """Edge case for invert function."""
    assert invert({}) == {}


def test_invert_single() -> None:
    """Use case for invert function."""
    assert invert({'1': '2'}) == {'2': '1'}


def test_only_evens_multiple() -> None:
    """Use case for invert function."""
    assert invert({'1': '2', '4': '3'}) == {'2': '1', '3': '4'}


def test_favorite_color_empty() -> None:
    """Edge case for favorite color function."""
    assert favorite_color({}) == ""


def test_favorite_color_single() -> None:
    """Use case for favorite color function."""
    assert favorite_color({'10': '5'}) == '5'


def test_favorite_color_multiple() -> None:
    """Use case for favorite color function."""
    assert favorite_color({'10': '20', '30': '20'}) == "20"


def test_count_empty() -> None:
    """Edge case for count function."""
    assert count([]) == {}


def test_count_single() -> None:
    """Use case for count function."""    
    assert count(['1']) == {'1': 1}


def test_count_mutliple() -> None:
    """Use case for count function."""
    assert count(['1', '2']) == {'1': 1, '2': 1}