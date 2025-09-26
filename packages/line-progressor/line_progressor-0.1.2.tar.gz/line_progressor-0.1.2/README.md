# line-progressor

Color progress bar for terminal loops.  
Single-file module. Handles noisy iterables that print. Dynamic width. ETA. Green done, red remaining.

---

## Install

```bash
pip install line-progressor
# dependency: colorama
```

## Quick start

```python
from time import sleep
from line_progressor import wrap

for _ in wrap(range(100)):  # intercepts stdout by default
    sleep(0.02)
```
Example output:

```
[══════════════════──────────────]  50% Processing... ETA 00:01
```

---

## Noisy iterables that print

```python
from line_progressor import wrap
import time

class Talker:
    def __init__(self, n): self.n = n
    def __len__(self): return self.n
    def __iter__(self):
        for i in range(self.n):
            print(f"line {i}")   # stdout noise
            yield i

for _ in wrap(Talker(20)):
    time.sleep(0.05)
```
`wrap` captures `stdout`, writes user lines **above** a stable one-line bar, then re-renders the bar.

---

## Choose output stream

- Keep your `print()` on stdout, bar on **stderr** (default):
```python
for _ in wrap(range(100), stream=sys.stderr):
    ...
```
- Put bar on **stdout**:
```python
for _ in wrap(range(100), stream=sys.stdout):
    ...
```

---

## Customize text and style

```python
for _ in wrap(
    range(100),
    running_text="Crunching...",
    done_text="All finished!",
    fill_char="═",
    empty_char="─",
    width=50,
):
    ...
```
- Bar: green filled, red remaining
- Percent: red while running, green when done
- Status: gray while running, green when done

---

## Disable interception

```python
for _ in wrap(range(100), intercept_stdout=False):
    ...
```

---

## Manual control

```python
from line_progressor import ProgressBar
pb = ProgressBar(total=5)

with pb.patch_stdout():
    for i in range(5):
        print("log line")
        pb.update(1)

pb.finish()
```

---

## API

### `wrap(iterable, total=None, *, intercept_stdout=True, enabled=None, stream=sys.stderr, **kwargs) -> iterator`
- Wraps any iterable and renders progress.
- `total` inferred via `len(iterable)` if omitted.
- `intercept_stdout=True` captures `print()` and keeps the bar stable.
- `enabled` defaults to `stream.isatty()`. When `intercept_stdout=True` and `enabled is None`, it is forced to `True`.
- `stream` is where the bar renders.
- `**kwargs` are forwarded to `ProgressBar(...)`.

### `ProgressBar(total, *, width=40, stream=sys.stderr, enabled=None, fmt="[{bar}] {pct} {status}{eta}", fill_char="═", empty_char="─", time_fn=time.time, running_text="Processing...", done_text="Done!")`
- Methods: `update(n=1)`, `finish()`, `patch_stdout()`

---

## Behavior notes

- **Dynamic width**: bar shrinks to avoid wrapping; ETA is dropped first if the line would wrap.
- **TTY detection**: set `enabled=True` to force rendering when piping or in non-TTY environments.
- **Windows**: requires `colorama` (this module calls `colorama.init()`).
- **Performance**: renders are throttled to ~60 FPS.

---

## Troubleshooting

- Bar not visible: pass `enabled=True` or choose a visible `stream`.
- Bar moves down on prints: use default interception or `with pb.patch_stdout():`.
- Jupyter/IDE consoles: ANSI behavior varies. Prefer a real terminal.

---

## License

MIT
