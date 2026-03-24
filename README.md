# Bubble Sort Learning App

A Python command-line app for learning Bubble Sort with two existing output styles:
- verbose text mode (prints list state after each pass)
- ANSI terminal animation mode (in-place redraw)

## Features

- Strict parsing for comma-separated integers, for example: `8, 3, 1, 7`
- Clear validation errors for malformed input like `1,,2` or `3, x, 5`
- Bubble Sort with early-exit optimization
- Interactive retry loop until `exit` is entered
- Pytest suite with 5 tests

## Project Structure

- `main.py`: CLI flow, parsing, Bubble Sort, and animation rendering
- `tests/test_main.py`: unit tests for parsing and core sort logic
- `pytest.ini`: pytest discovery configuration
- `REPORT.md`: report file

## Requirements

- Python 3.10+
- pytest

Install test dependency:

```bash
python -m pip install pytest
```

## Running The App

From the project root:

```bash
python main.py
```

Windows alternative:

```powershell
py main.py
```

## CLI Flow

1. Enter numbers or type `exit`.
2. Choose mode:
	- `a` for animation
	- any other input for verbose text mode
3. If animation is selected, choose speed:
	- `1` slow
	- `2` medium
	- `3` fast

## Running Tests

```bash
python -m pytest -q
```

Windows alternative:

```powershell
py -m pytest -q
```

Current tests cover:
- valid parsing
- empty token validation
- non-integer validation
- sorting correctness
- non-mutation of input list

## Bubble Sort Summary

Bubble Sort repeatedly compares adjacent elements and swaps them when needed.
After each pass, the largest remaining unsorted value moves to the end.

Complexity:
- worst and average time: O(n^2)
- best time with early exit: O(n)
- space: O(1)
