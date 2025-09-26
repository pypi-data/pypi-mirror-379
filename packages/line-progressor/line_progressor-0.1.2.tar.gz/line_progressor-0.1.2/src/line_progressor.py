from __future__ import annotations
import sys, time, shutil, re, threading
from contextlib import contextmanager
from typing import Iterable, Iterator, Optional, TypeVar, Callable
from colorama import init as _colorama_init

__version__ = "0.1.2"

T = TypeVar("T")

_RED   = "\033[91m"
_GREEN = "\033[92m"
_GRAY  = "\033[90m"
_RESET = "\033[0m"
_CLRLINE = "\033[2K"   # clear entire line

_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

_colorama_init()

class ProgressBar:
    def __init__(
        self,
        total: Optional[int],
        *,
        width: int = 40,
        stream = sys.stderr,             # <- default to stderr to avoid stdout prints
        enabled: Optional[bool] = None,
        fmt: str = "[{bar}] {pct} {status}{eta}",
        fill_char: str = "═",
        empty_char: str = "─",
        time_fn: Callable[[], float] = time.time,
        running_text: str = "Processing...",
        done_text: str = "Done!",
    ) -> None:
        self.total = total
        self.width = width
        self.stream = stream
        self.enabled = enabled if enabled is not None else stream.isatty()
        self.fmt = fmt
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.time = time_fn
        self.running_text = running_text
        self.done_text = done_text

        self.start_t = self.time()
        self.last_render = 0.0
        self.count = 0
        self.finished = False
        self._render_lock = threading.Lock()

    def _eta(self) -> str:
        if not self.total or self.count == 0:
            return ""
        elapsed = self.time() - self.start_t
        rate = self.count / max(elapsed, 1e-9)
        remain = max(self.total - self.count, 0) / max(rate, 1e-9)
        m, s = divmod(int(remain), 60)
        h, m = divmod(m, 60)
        txt = f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"
        return f" {_GRAY}ETA {txt}{_RESET}"

    def _render(self, done: bool = False) -> None:
        if not self.enabled:
            return
        with self._render_lock:
            cols = shutil.get_terminal_size(fallback=(80, 24)).columns
            reserve = 32  # room for pct/status/ETA without wrapping
            bar_w = max(1, min(self.width, max(1, cols - reserve)))

            pct_num = 0 if not self.total else int(self.count * 100 / max(self.total, 1))
            filled = bar_w if done else int(bar_w * pct_num / 100)

            bar = (
                f"{_GREEN}{self.fill_char * filled}"
                f"{_RED}{self.empty_char * (bar_w - filled)}{_RESET}"
            )
            pct = f"{_GREEN}{pct_num:>3}%{_RESET}" if done else f"{_RED}{pct_num:>3}%{_RESET}"
            status = f"{_GREEN}{self.done_text}{_RESET}" if done else f"{_GRAY}{self.running_text}{_RESET}"
            eta = "" if done else self._eta()

            line = self.fmt.format(bar=bar, pct=pct, status=status, eta=eta).rstrip()

            vis = _ANSI_RE.sub("", line)
            if len(vis) >= cols and eta:
                # drop ETA first if it would wrap
                line = self.fmt.format(bar=bar, pct=pct, status=status, eta="").rstrip()

            self.stream.write("\r" + _CLRLINE + line)
            self.stream.flush()

    def update(self, n: int = 1) -> None:
        if self.finished:
            return
        self.count += n
        now = self.time()
        if now - self.last_render >= 1/60 and (not self.total or self.count < self.total):
            self._render(done=False)
            self.last_render = now

    def finish(self) -> None:
        if self.finished:
            return
        self.finished = True
        if self.total is not None:
            self.count = self.total
        self._render(done=True)
        if self.enabled:
            self.stream.write("\n")
            self.stream.flush()

    # ----- stdout interception ------------------------------------------------
    @contextmanager
    def patch_stdout(self):
        """Temporarily route prints so they don't break the bar."""
        real = sys.stdout
        proxy = _StdoutProxy(self, real)
        sys.stdout = proxy
        try:
            yield
        finally:
            sys.stdout = real

class _StdoutProxy:
    def __init__(self, pb: ProgressBar, real):
        self.pb = pb
        self.real = real

    def write(self, data):
        if not data:
            return 0
        # 1) clear the bar line on its stream
        if self.pb.enabled:
            self.pb.stream.write("\r\033[2K")
            self.pb.stream.flush()

        # 2) write the user's output
        n = self.real.write(data)
        self.real.flush()

        # 3) move cursor back up by printed newlines, then re-render bar
        if self.pb.enabled and not self.pb.finished:
            up = data.count("\n")
            if up:
                self.pb.stream.write(f"\033[{up}A")  # move up 'up' lines
            self.pb._render(done=False)
        return n

    def flush(self): self.real.flush()
    def isatty(self): return self.real.isatty()
    def fileno(self): return self.real.fileno()


@contextmanager
def _noop():
    yield

def wrap(
    iterable: Iterable[T],
    total: Optional[int] = None,
    *,
    intercept_stdout: bool = True,
    enabled: Optional[bool] = None,
    stream = sys.stderr,
    **kwargs
) -> Iterator[T]:
    # infer total
    if total is None:
        try:
            total = len(iterable)  # type: ignore
        except Exception:
            total = None

    # force-enable if intercepting (otherwise user sees nothing)
    if enabled is None and intercept_stdout:
        enabled = True

    pb = ProgressBar(total, stream=stream, enabled=enabled, **kwargs)
    cm = pb.patch_stdout() if intercept_stdout else _noop()
    try:
        with cm:
            for item in iterable:
                yield item
                pb.update(1)
    finally:
        pb.finish()

def _demo():
    from time import sleep
    for _ in wrap(range(101), running_text="Crunching...", done_text="All finished!"):
        sleep(0.01)

if __name__ == "__main__":
    _demo()
