"""
Bubble Sort Learning App - Upgraded Version
Implements strict validation, retry loops, and verbose learning mode.
"""

def show_intro() -> None:
    print("\n" + "="*35)
    print("=== Bubble Sort Learning App Pro ===")
    print("="*35)
    print("Type 'exit' at any time to quit.\n")


def parse_numbers(raw_text: str) -> list[int]:
    """
    Converts text to integers with strict comma validation.
    Raises ValueError with a specific message if format is wrong.
    """
    if not raw_text.strip():
        raise ValueError("Input cannot be empty.")
    
    parts = raw_text.split(",")
    processed_numbers = []
    
    for item in parts:
        clean_item = item.strip()
        if not clean_item:
            raise ValueError("Empty token detected (e.g., '1,,2'). Use strict comma format.")
        try:
            processed_numbers.append(int(clean_item))
        except ValueError:
            raise ValueError(f"'{clean_item}' is not a valid integer.")
            
    return processed_numbers


def needs_swap(left: int, right: int) -> bool:
    return left > right


def bubble_sort(values: list[int], verbose: bool = True) -> list[int]:
    """
    Sorts values and shows each pass if verbose is True.
    """
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
            if verbose: print("No swaps this pass. List is sorted early!")
            break

    return sorted_values


def run_tests():
    """Basic tests for validation and sorting logic."""
    print("\n--- Running Internal Tests ---")
    test_cases = [
        ([], "Empty list"),
        ([1], "Single element"),
        ([1, 2, 3], "Already sorted"),
        ([3, 2, 1], "Reverse sorted"),
        ([2, 1, 2], "Duplicates")
    ]
    for case, label in test_cases:
        result = bubble_sort(case, verbose=False)
        print(f"Test {label}: {'Passed' if result == sorted(case) else 'Failed'}")
    print("--- Tests Complete ---\n")


def run_app() -> None:
    show_intro()
    
    # Run tests automatically once on startup (Optional)
    # run_tests()

    while True:
        user_input = input("Enter numbers (e.g., 8, 3, 1) or 'exit': ").lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break
            
        try:
            # 1, 2 & 3: Strict parse and error handling
            numbers = parse_numbers(user_input)
            
            # 4: Verbose mode enabled by default
            print("\nStarting Sort...")
            sorted_numbers = bubble_sort(numbers, verbose=True)
            
            print(f"\nFinal Result: {sorted_numbers}\n" + "-"*20)
            
        except ValueError as e:
            # Catching the error and allowing the loop to continue (Retry Loop)
            print(f"Invalid Input: {e} Please try again.")


if __name__ == "__main__":
    run_app()