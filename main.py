"""Bubble Sort CLI app with text and animated terminal visualization."""

import time

ANSI_CLEAR_HOME = "\033[H\033[J"
ANSI_YELLOW = "\033[33m"
ANSI_RED = "\033[31m"
ANSI_RESET = "\033[0m"


def show_intro() -> None:
    """Print app banner."""
    print("\n" + "=" * 35)
    print("=== Bubble Sort Visual ===")
    print("=" * 35)
    print("Type 'exit' at any time to quit.\n")


def parse_numbers(raw_text: str) -> list[int]:
    """Converts text to integers with strict comma validation."""
    if not raw_text.strip():
        raise ValueError("Input cannot be empty.")

    parts = raw_text.split(",")
    numbers: list[int] = []
    for item in parts:
        clean_item = item.strip()
        if not clean_item:
            raise ValueError("Empty token detected (e.g., '1,,2').")
        try:
            numbers.append(int(clean_item))
        except ValueError as exc:
            raise ValueError(f"'{clean_item}' is not a valid integer.")
    return numbers


def needs_swap(left: int, right: int) -> bool:
    return left > right


def clear_terminal_in_place() -> None:
    """Uses ANSI escape codes to clear screen and move cursor to home."""
    print(ANSI_CLEAR_HOME, end="")


def render_bar_line(value: int, max_value: int, is_comparing: bool, bar_width: int = 40) -> str:
    """Builds an ASCII bar line with highlighting."""
    if max_value <= 0:
        return f"{value:>3} |"

    scaled = max(1, int((value / max_value) * bar_width)) if value > 0 else 0
    bar = "#" * scaled
    
    if is_comparing:
        return f"{ANSI_YELLOW}{value:>3} | {bar} <--- COMPARING{ANSI_RESET}"
    return f"{value:>3} | {bar}"


def render_animation_frame(values: list[int], pass_idx: int, comp_idx: int, is_swap: bool) -> None:
    """Renders the current state of the sort with highlights."""
    clear_terminal_in_place()
    status = f"{ANSI_RED}SWAPPING!{ANSI_RESET}" if is_swap else "Comparing..."

    print("=== Bubble Sort Animation ===")
    print(f"Pass: {pass_idx + 1} | Pair: ({comp_idx}, {comp_idx + 1}) | Status: {status}")
    print("-" * 45)

    max_val = max(values) if values else 0
    for idx, val in enumerate(values):
        comparing = idx == comp_idx or idx == comp_idx + 1
        print(render_bar_line(val, max_val, comparing))
    print("-" * 45)


def bubble_sort(values: list[int], verbose: bool = False) -> list[int]:
    """Standard Bubble Sort implementation."""
    sorted_values = values.copy()
    n = len(sorted_values)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if needs_swap(sorted_values[j], sorted_values[j + 1]):
                sorted_values[j], sorted_values[j + 1] = sorted_values[j + 1], sorted_values[j]
                swapped = True

        if verbose:
            print(f"Pass {i + 1}: {sorted_values}")

        if not swapped:
            break

    return sorted_values


def bubble_sort_animated(values: list[int], frame_delay: float) -> list[int]:
    """Sorts with real-time ANSI animation."""
    sorted_values = values.copy()
    n = len(sorted_values)

    for i in range(n - 1):
        swapped_in_pass = False
        for j in range(n - 1 - i):
            if frame_delay > 0:
                render_animation_frame(sorted_values, i, j, False)
                time.sleep(frame_delay)

            if needs_swap(sorted_values[j], sorted_values[j + 1]):
                sorted_values[j], sorted_values[j + 1] = sorted_values[j + 1], sorted_values[j]
                swapped_in_pass = True
                
                if frame_delay > 0:
                    render_animation_frame(sorted_values, i, j, True)
                    time.sleep(frame_delay)

        if not swapped_in_pass:
            break

    return sorted_values


def run_app() -> None:
    """Run the interactive CLI loop."""
    show_intro()

    while True:
        user_input = input("\nEnter numbers (e.g., 8, 3, 1) or 'exit': ")

        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break

        try:
            numbers = parse_numbers(user_input)
            mode = input("Choose mode: (A)nimation or (V)erbose text? ").lower()

            if mode == "a":
                speed_input = input("Choose speed: (1) Slow, (2) Medium, (3) Fast: ")
                speeds: dict[str, float] = {"1": 0.5, "2": 0.2, "3": 0.05}
                delay = speeds.get(speed_input, 0.2)

                print("\nStarting Animation...")
                time.sleep(1)
                sorted_numbers = bubble_sort_animated(numbers, delay)
            else:
                print("\nStarting Standard Sort...")
                sorted_numbers = bubble_sort(numbers, verbose=True)

            print(f"\nFinal Sorted List: {sorted_numbers}")
            print("-" * 20)

        except ValueError as e:
            print(f"Invalid Input: {e} Please try again.")

if __name__ == "__main__":
    run_app()