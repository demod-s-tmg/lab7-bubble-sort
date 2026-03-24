import pytest

from main import bubble_sort, parse_numbers


def test_parse_numbers_valid_csv() -> None:
    assert parse_numbers("8, 3, 1, 7") == [8, 3, 1, 7]


def test_parse_numbers_rejects_empty_token() -> None:
    with pytest.raises(ValueError, match="Empty token"):
        parse_numbers("1,,2")


def test_parse_numbers_rejects_non_integer() -> None:
    with pytest.raises(ValueError, match="not a valid integer"):
        parse_numbers("3, x, 5")


def test_bubble_sort_orders_values_ascending() -> None:
    assert bubble_sort([5, 1, 4, 2], verbose=False) == [1, 2, 4, 5]


def test_bubble_sort_preserves_input_list() -> None:
    original = [3, 2, 1]
    result = bubble_sort(original, verbose=False)

    assert result == [1, 2, 3]
    assert original == [3, 2, 1]
