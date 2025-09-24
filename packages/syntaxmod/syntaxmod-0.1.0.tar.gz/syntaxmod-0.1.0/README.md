# SyntaxMod

Utility helpers for quick scripting tasks: looping functions, timed waits, and stopwatch/timer primitives with pause/resume support.

## Installation

```bash
pip install .
```

## Usage

```python
from syntaxmod import loop, wait, Stopwatch, Timer

loop(3, print, ["hello"])
wait(0.5)

watch = Stopwatch()
# ... do work ...
print(f"Elapsed: {watch.pause():.2f}s")

Timer(2.0, lambda: print("done"))
```

### Timer controls

```python
from syntaxmod import Timer

def callback():
    print("Timer fired!")

timer = Timer(5, callback, start=False)
timer.resume()     # start counting down
wait(2)
elapsed = timer.pause()
print(elapsed)
timer.resume()
```

## Development

```bash
python -m build
pytest
```
