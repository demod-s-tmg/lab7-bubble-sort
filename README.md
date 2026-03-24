# Bubble Sort Learning App

A Python command-line app for learning Bubble Sort with two existing output styles:
- verbose text mode (prints list state after each pass)
- ANSI terminal animation mode (in-place redraw)

This project also includes a Pygame-based 2D visualizer.

## Features

- Strict parsing for comma-separated integers, for example: `8, 3, 1, 7`
- Clear validation errors for malformed input like `1,,2` or `3, x, 5`
- Bubble Sort with early-exit optimization
- Interactive retry loop until `exit` is entered
- Pytest suite with 5 tests

## Project Structure

- `main.py`: CLI flow, parsing, Bubble Sort, and animation rendering
- `pygame_visualizer.py`: Pygame 2D visualization
- `tests/test_main.py`: unit tests for parsing and core sort logic
- `pytest.ini`: pytest discovery configuration
- `REPORT.md`: report file

## Requirements

- Python 3.10+
- pytest
- pygame (for the 2D visualizer)

## Setup (Local Virtual Environment)

Create a local virtual environment in the project root:

```bash
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

If PowerShell execution policy blocks activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

## Requirements File

The project dependencies are listed in `requirements.txt`.

Current pinned libraries:
- pygame==2.6.1
- pytest==9.0.2

## Running The App

From the project root:

```bash
.venv\Scripts\python.exe main.py
```

Windows alternative:

```powershell
python main.py
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
.venv\Scripts\python.exe -m pytest -q
```

Windows alternative:

```powershell
python -m pytest -q
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

## Pygame Visualization

Run the visualizer directly:

```bash
.venv\Scripts\python.exe pygame_visualizer.py
```

Controls:
- Space: pause/resume
- N: single-step when paused
- R: restart animation
- Esc or Q: quit window
