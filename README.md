# Bubble Sort Learning App

A small Python command-line project to learn Bubble Sort step by step.

The app includes:
- strict input validation for comma-separated integers
- verbose mode showing each Bubble Sort pass
- retry loop for invalid input
- basic pytest test suite

## Features

- Parse and validate integer input like `8, 3, 1, 7`
- Reject malformed inputs like `1,,2` and non-integers like `3, x, 5`
- Sort using Bubble Sort with early-exit optimization
- Show intermediate sorting passes for learning
- Exit cleanly with `exit`

## Project Structure

- `main.py`: CLI app and sorting logic
- `tests/test_main.py`: pytest unit tests
- `pytest.ini`: pytest configuration
- `REPORT.md`: report file

## Requirements

- Python 3.10+
- pytest (for running tests)

Install pytest:

```bash
python -m pip install pytest
```

## Run The App

From the project root:

```bash
python main.py
```

On Windows, if needed:

```powershell
py main.py
```

### Example Session

```text
=== Bubble Sort Learning App Pro ===
Type 'exit' at any time to quit.

Enter numbers (e.g., 8, 3, 1) or 'exit': 8, 3, 1, 7

Starting Sort...
Pass 1: [3, 1, 7, 8]
Pass 2: [1, 3, 7, 8]
Pass 3: [1, 3, 7, 8]
No swaps this pass. List is sorted early!

Final Result: [1, 3, 7, 8]
```

## Run Tests

From the project root:

```bash
python -m pytest -q
```

On Windows, if needed:

```powershell
py -m pytest -q
```

Current suite contains 5 tests covering:
- valid parsing
- empty token validation
- non-integer validation
- sorting correctness
- preserving original input list

## How Bubble Sort Works

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
After each full pass, the largest unsorted element moves to the end.

Complexity:
- worst/average time: O(n^2)
- best time (already sorted with early exit): O(n)
- space: O(1)

## Notes

In `main.py`, `run_tests()` is available as a small internal demo helper but is not automatically executed.
For regular validation, prefer the pytest suite in `tests/test_main.py`.
