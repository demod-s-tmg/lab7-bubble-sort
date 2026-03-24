import pytest

from main import bubble_sort, parse_input


def test_parse_input_valid_integers() -> None:
    result = parse_input("9 3 7 1 5")
    assert result == [9, 3, 7, 1, 5]


def test_parse_input_raises_on_empty_input() -> None:
    with pytest.raises(ValueError, match="at least one integer"):
        parse_input("   ")


def test_parse_input_raises_on_non_integer_values() -> None:
    with pytest.raises(ValueError, match="only integers"):
        parse_input("1 two 3")


def test_bubble_sort_returns_sorted_list_and_swap_count() -> None:
    sorted_values, swaps = bubble_sort([5, 1, 4, 2, 8])
    assert sorted_values == [1, 2, 4, 5, 8]
    assert swaps == 4


def test_bubble_sort_does_not_mutate_input_list() -> None:
    original = [3, 2, 1]
    original_before = original.copy()

    sorted_values, _ = bubble_sort(original)

    assert original == original_before
    assert sorted_values == [1, 2, 3]
