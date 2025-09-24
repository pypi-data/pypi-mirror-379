from types import FunctionType, LambdaType
import time as t
import os
from datetime import datetime
from typing import Any, Callable, List, Optional
from warnings import deprecated

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


@deprecated("Use for loop instead")
def loop(times: int, func: Callable, params: Optional[List[Any]] = None) -> None:
    """Execute a function multiple times with optional parameters."""
    for _ in range(times):
        if params is None:
            func()
        elif isinstance(params, list):
            func(*params)
        else:
            func(params)


def wait(seconds: float) -> None:
    """Pause execution for a specified number of seconds."""
    t.sleep(seconds)


@deprecated("Use regular print instead")
def printstr(text: str) -> None:
    """Print text, evaluating it first if it's a valid Python expression."""
    try:
        if any(char in text for char in "=+-*/()[]{}"):
            print(eval(text))
        else:
            print(text)
    except (NameError, SyntaxError, TypeError):
        print(text)


def wait_until(condition: Callable[..., Any] | bool) -> None:
    if isinstance(condition, bool):
        while not condition:
            t.sleep(00000000000000000000.1)
        return
    else:
        while not condition():
            t.sleep(00000000000000000000.1)
        return


class Stopwatch:
    """A simple stopwatch class with pause/resume functionality."""

    def __init__(self, start=False):
        self.elasped: float = 0
        self.paused = start
        self.start_time = t.time()
        self.pause_time = 0
        if self.paused:
            self.last_pause_time = self.start_time

        else:
            self.last_pause_time = 0

    def pause(self) -> float:
        self.elasped = t.time() - self.start_time - self.pause_time
        if not self.paused:
            self.paused = True
            self.last_pause_time = t.time()
            return self.elasped

        else:
            return self.elasped

    def resume(self) -> float:
        if self.paused:
            self.paused = False
            self.pause_time += t.time() - self.last_pause_time
            return t.time() - self.start_time - self.pause_time

        else:
            return t.time() - self.start_time - self.pause_time

    def reset(self, start=False) -> float:
        self.elasped = 0
        self.paused = start
        self.start_time = t.time()
        self.pause_time = 0
        return self.elasped

    def get_elasped_time(self):
        return self.elasped

    def get_pause_time(self):
        return self.pause_time

    def get_start_time(self):
        return self.start_time

    def get_last_pause_time(self):
        return self.last_pause_time

    def get_paused_flag(self):
        return self.paused

    def __repr__(self) -> str:
        return str(self.elasped)


class Timer:
    """One-shot timer with pause, resume, reset, and terminate."""

    def __init__(self, delay: float, callback: Callable, start: bool = True) -> None:
        import threading
        self.delay = float(delay)
        self.callback = callback

        self._lock = threading.RLock()
        self._terminate = threading.Event()
        self._run_event = threading.Event()  # set = running, clear = paused
        self._thread: Optional[threading.Thread] = None

        self._start_time = t.time()
        self._total_paused = 0.0
        self._paused = not start
        self._pause_started: Optional[float] = self._start_time if self._paused else None
        self._done = False

        if start:
            self._run_event.set()
        else:
            self._run_event.clear()

        self._start_thread()

    # ---------- internal ----------

    def _start_thread(self) -> None:
        with self._lock:
            if self._thread and self._thread.is_alive():
                return
            self._thread = threading.Thread(  # type: ignore
                target=self._run, name="Timer", daemon=True)
            self._thread.start()  # type: ignore

    def _run(self) -> None:
        while not self._terminate.is_set():
            # if paused, wait in small chunks so terminate can break promptly
            if self._paused:
                self._run_event.wait(timeout=0.1)
                continue

            remaining = self.delay - self.get_elapsed()
            if remaining <= 0:
                try:
                    self.callback()
                finally:
                    with self._lock:
                        self._done = True
                return

            # sleep cooperatively without busy-wait
            self._run_event.wait(timeout=min(0.1, remaining))

    # ---------- controls ----------

    def pause(self) -> float:
        with self._lock:
            if not self._paused and not self._done:
                self._paused = True
                self._pause_started = t.time()
                self._run_event.clear()
            return self.get_elapsed()

    def resume(self) -> float:
        with self._lock:
            if self._paused and not self._done:
                now = t.time()
                if self._pause_started is not None:
                    self._total_paused += now - self._pause_started
                self._pause_started = None
                self._paused = False
                self._run_event.set()
            return self.get_elapsed()

    def reset(self, start: bool = True, delay: Optional[float] = None) -> float:
        with self._lock:
            if delay is not None:
                self.delay = float(delay)
            self._start_time = t.time()
            self._total_paused = 0.0
            self._done = False

            self._paused = not start
            self._pause_started = self._start_time if self._paused else None

            if start:
                self._run_event.set()
            else:
                self._run_event.clear()

            # if previous thread exited after firing, start a new one
            if not (self._thread and self._thread.is_alive()):
                self._start_thread()

            return 0.0

    def terminate(self) -> None:
        with self._lock:
            self._terminate.set()
            self._run_event.set()  # release any waits

    # ---------- info ----------

    def get_elapsed(self) -> float:
        with self._lock:
            now = t.time()
            paused_now = 0.0
            if self._paused and self._pause_started is not None:
                paused_now = now - self._pause_started
            return max(0.0, now - self._start_time - self._total_paused - paused_now)

    def is_paused(self) -> bool:
        with self._lock:
            return self._paused

    def is_done(self) -> bool:
        with self._lock:
            return self._done

    # ---------- dunder ----------

    def __repr__(self) -> str:
        return f"Timer(elapsed={self.get_elapsed():.3f}, delay={self.delay}, paused={self.is_paused()}, done={self.is_done()})"

    def __float__(self) -> float:
        return self.get_elapsed()

    def __int__(self) -> int:
        return int(self.get_elapsed())

    def __bool__(self) -> bool:
        return self.is_done()
