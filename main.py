"""Bubble sort CLI app with optional in-place terminal visualization."""

import os
import time


def clear_screen() -> None:
    """Clear the terminal so the next frame can be redrawn in place."""
    os.system("cls" if os.name == "nt" else "clear")


def build_bars(values: list[int], active_i: int | None, active_j: int | None) -> list[str]:
    """Build one ASCII bar line per value and mark active indices."""
    bars: list[str] = []
    for idx, val in enumerate(values):
        marker = "> " if idx == active_i or idx == active_j else "  "
        bar_graphic = "#" * max(0, val)
        bars.append(f"{marker}[{idx:02}] {bar_graphic} ({val})")
    return bars


def render_frame(
    values: list[int],
    pass_index: int,
    comparisons: int,
    swaps: int,
    active_i: int | None,
    active_j: int | None,
) -> str:
    """Render a full text frame for the current sorting state."""
    header = f"--- Pass: {pass_index} | Comparisons: {comparisons} | Swaps: {swaps} ---\n"
    bars = build_bars(values, active_i, active_j)
    return header + "\n".join(bars)


def visualize_bubble_sort(values: list[int], delay_seconds: float = 0.15) -> tuple[list[int], int]:
    """Sort values while redrawing an ASCII frame in place after each comparison."""
    arr = values.copy()
    n = len(arr)
    swap_count = 0
    comparison_count = 0
    pass_index = 0

    for i in range(n):
        pass_index = i + 1
        swapped = False
        for j in range(0, n - i - 1):
            comparison_count += 1

            clear_screen()
            print(render_frame(arr, pass_index, comparison_count, swap_count, j, j + 1))
            time.sleep(delay_seconds)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True

        if not swapped:
            break

    if pass_index == 0:
        pass_index = 1

    clear_screen()
    print(render_frame(arr, pass_index, comparison_count, swap_count, None, None))
    print("\nSorting Complete!")

    return arr, swap_count


def bubble_sort(values: list[int]) -> tuple[list[int], int]:
    """Return a sorted copy of values and the number of swaps performed."""
    arr = values.copy()
    n = len(arr)
    swap_count = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True

        if not swapped:
            break

    return arr, swap_count


def parse_input(raw: str) -> list[int]:
    """Parse a space-separated string of integers."""
    parts = raw.split()

    if not parts:
        raise ValueError("Please enter at least one integer.")

    try:
        return [int(p) for p in parts]
    except ValueError as exc:
        raise ValueError("Input must contain only integers.") from exc


def print_results(original: list[int], sorted_values: list[int], swaps: int) -> None:
    """Print sorting results in a readable format."""
    print(f"\nOriginal List: {original}")
    print(f"Sorted List:   {sorted_values}")
    print(f"Total Swaps:   {swaps}")


def choose_mode() -> str:
    """Prompt until the user selects a valid mode."""
    while True:
        mode = input("Choose mode (normal/visual): ").strip().lower()
        if mode in {"normal", "visual"}:
            return mode
        print("Invalid mode. Please type 'normal' or 'visual'.")


def main() -> None:
    """Run the bubble sort CLI app."""
    print("Bubble Sort (CLI Tool)")
    print("Enter integers separated by spaces. Example: 9 3 7 1 5")

    raw = input("> ")
    try:
        numbers = parse_input(raw)
    except ValueError as err:
        print(f"Error: {err}")
        return

    mode = choose_mode()

    if mode == "visual":
        sorted_numbers, swaps = visualize_bubble_sort(numbers)
    else:
        sorted_numbers, swaps = bubble_sort(numbers)

    print_results(numbers, sorted_numbers, swaps)


if __name__ == "__main__":
    main()