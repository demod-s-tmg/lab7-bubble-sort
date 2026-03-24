"""Pygame Bubble Sort visualizer scaffold.

Current CLI behavior in main.py remains unchanged.
"""

from dataclasses import dataclass
from typing import Any, Iterator


@dataclass(frozen=True)
class SortEvent:
    """Represents one step in Bubble Sort visualization state."""

    values: list[int]
    pass_index: int
    compare_index: int
    swapped: bool
    finished: bool = False


@dataclass(frozen=True)
class VisualConfig:
    """Holds window and timing parameters for rendering."""

    width: int = 960
    height: int = 540
    fps: int = 60
    step_delay_ms: int = 120
    margin: int = 40


BACKGROUND = (18, 22, 28)
BAR_DEFAULT = (90, 170, 255)
BAR_COMPARE = (255, 210, 70)
BAR_SWAP = (255, 120, 120)
TEXT_COLOR = (240, 244, 248)
GRID_COLOR = (40, 52, 64)


def _import_pygame() -> Any:
    """Import pygame lazily and raise a clear message if unavailable."""
    try:
        import pygame  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Pygame is not installed. Run: python -m pip install pygame"
        ) from exc
    return pygame


def generate_bubble_sort_events(values: list[int]) -> Iterator[SortEvent]:
    """Yield Bubble Sort states for animation."""
    working = values.copy()
    n = len(working)

    for i in range(n - 1):
        swapped_in_pass = False
        for j in range(n - 1 - i):
            # TODO: emit comparison frame first.
            yield SortEvent(working.copy(), i, j, swapped=False)

            if working[j] > working[j + 1]:
                working[j], working[j + 1] = working[j + 1], working[j]
                swapped_in_pass = True

                # TODO: emit post-swap frame.
                yield SortEvent(working.copy(), i, j, swapped=True)

        if not swapped_in_pass:
            break

    yield SortEvent(working.copy(), max(0, n - 1), -1, swapped=False, finished=True)


def build_bar_rects(values: list[int], cfg: VisualConfig) -> list[tuple[int, int, int, int]]:
    """Compute bar rectangles as (x, y, width, height)."""
    if not values:
        return []

    # Shift values so negatives can still be represented as positive-height bars.
    min_value = min(values)
    shift = -min_value if min_value < 0 else 0
    shifted_values = [value + shift for value in values]
    max_value = max(shifted_values) or 1

    chart_width = cfg.width - 2 * cfg.margin
    slot_width = max(1, chart_width // len(values))
    inner_width = max(1, slot_width - 4)
    available_height = cfg.height - 2 * cfg.margin

    rects: list[tuple[int, int, int, int]] = []
    for idx, value in enumerate(shifted_values):
        scaled = int((value / max_value) * available_height)
        x = cfg.margin + idx * slot_width + 2
        h = scaled
        y = cfg.height - cfg.margin - h
        rects.append((x, y, inner_width, h))

    return rects


def draw_frame(
    screen: Any,
    font: Any,
    event: SortEvent,
    cfg: VisualConfig,
) -> None:
    """Draw one frame for current sort event."""
    pygame = _import_pygame()

    screen.fill(BACKGROUND)

    # Subtle grid helps track bar movement.
    for y in range(cfg.margin, cfg.height - cfg.margin + 1, 50):
        pygame.draw.line(screen, GRID_COLOR, (cfg.margin, y), (cfg.width - cfg.margin, y), 1)

    rects = build_bar_rects(event.values, cfg)
    compare_left = event.compare_index
    compare_right = event.compare_index + 1

    for idx, (x, y, w, h) in enumerate(rects):
        color = BAR_DEFAULT
        if idx == compare_left or idx == compare_right:
            color = BAR_SWAP if event.swapped else BAR_COMPARE

        pygame.draw.rect(screen, color, (x, y, w, h), border_radius=3)

    status_text = "Finished" if event.finished else ("Swap" if event.swapped else "Compare")
    header = f"Pass {event.pass_index + 1} | Pair ({event.compare_index}, {event.compare_index + 1}) | {status_text}"
    if event.compare_index < 0:
        header = f"Pass {event.pass_index + 1} | Complete"

    help_line = "Space: pause/resume | N: step | R: restart | Esc/Q: quit"
    title_surface = font.render(header, True, TEXT_COLOR)
    help_surface = font.render(help_line, True, TEXT_COLOR)
    screen.blit(title_surface, (cfg.margin, 10))
    screen.blit(help_surface, (cfg.margin, cfg.height - cfg.margin + 8))

    pygame.display.flip()


def poll_user_actions() -> dict[str, bool]:
    """Collect input actions from pygame events."""
    pygame = _import_pygame()

    actions = {
        "quit": False,
        "pause_toggle": False,
        "step": False,
        "restart": False,
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            actions["quit"] = True
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                actions["quit"] = True
            elif event.key == pygame.K_SPACE:
                actions["pause_toggle"] = True
            elif event.key == pygame.K_n:
                actions["step"] = True
            elif event.key == pygame.K_r:
                actions["restart"] = True

    return actions


def run_visualizer(values: list[int], cfg: VisualConfig | None = None) -> None:
    """Entry point for the Pygame visualizer."""
    if cfg is None:
        cfg = VisualConfig()

    pygame = _import_pygame()
    pygame.init()

    screen = pygame.display.set_mode((cfg.width, cfg.height))
    pygame.display.set_caption("Bubble Sort Visualizer (Pygame)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)

    paused = False
    step_once = False
    running = True
    timer_ms = 0
    frame_interval = max(1, cfg.step_delay_ms)

    def reset_stream() -> tuple[Iterator[SortEvent], SortEvent]:
        stream = generate_bubble_sort_events(values)
        first = next(stream)
        return stream, first

    event_stream, current_event = reset_stream()

    try:
        while running:
            actions = poll_user_actions()
            if actions["quit"]:
                running = False
            if actions["pause_toggle"]:
                paused = not paused
            if actions["restart"]:
                event_stream, current_event = reset_stream()
                paused = False
                step_once = False
                timer_ms = 0
            if actions["step"]:
                step_once = True
                paused = True

            dt_ms = clock.tick(cfg.fps)
            timer_ms += dt_ms

            should_advance = (not paused and timer_ms >= frame_interval) or step_once
            if should_advance and not current_event.finished:
                timer_ms = 0
                step_once = False
                try:
                    current_event = next(event_stream)
                except StopIteration:
                    current_event = SortEvent(
                        values=current_event.values,
                        pass_index=current_event.pass_index,
                        compare_index=-1,
                        swapped=False,
                        finished=True,
                    )

            draw_frame(screen, font, current_event, cfg)
    finally:
        pygame.quit()


if __name__ == "__main__":
    # Learning launcher example. Replace with your own inputs if desired.
    demo_values = [8, 3, 1, 7, 4, 6, 2, 5]
    run_visualizer(demo_values)
