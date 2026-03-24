# Bubble Sort Lab (Python)

Small command-line Bubble Sort app with two modes:

- `normal`: sorts and prints results
- `visual`: sorts with in-place ASCII redraw in the terminal

## Project Structure

- `main.py`: application entry point and sorting logic
- `visualizer_pygame.py`: Pygame 2D visualization scaffold (stubs + TODOs)
- `tests/test_main.py`: pytest test suite (5 tests)
- `pytest.ini`: pytest discovery settings

## Requirements

- Python 3.10+
- pytest

## Setup

Install test dependency:

```bash
python -m pip install pytest
```

## Run the Application

```bash
python main.py
```

Flow:

1. Enter integers separated by spaces.
2. Choose mode: `normal` or `visual`.
3. View sorted output and swap count.

## Pygame Visualization Scaffold

A starter scaffold is provided in `visualizer_pygame.py`.
It contains structured stubs and numbered TODOs for building a real-time 2D bubble sort visualization.

When you are ready to implement and run it:

```bash
python visualizer_pygame.py
```

Suggested implementation order:

1. `generate_values`
2. `bubble_sort_events`
3. Drawing functions (`draw_background`, `draw_bars`, `draw_hud`)
4. Input handling (`handle_keydown`)
5. Main loop (`run_visualizer`, `main`)

## Run Tests

```bash
python -m pytest -q
```

Windows launcher alternative:

```bash
py -m pytest -q
```

## Behavior Notes

- Sorting is in ascending order.
- Bubble sort uses early exit when no swaps occur in a pass.
- The input list is not mutated by sorting functions.

## Complexity

- Worst case: O(n^2)
- Average case: O(n^2)
- Best case (already sorted with early exit): O(n)
- Extra space: O(1) for in-place sorting of the copied list
