import builtins
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import List

_original_open = builtins.open
_recorders = []

@dataclass
class FileRecorder():
    files : List[str] = field(default_factory=set)


def using_file(path) :
    """Call this directly before builtin functions that don't use open() """
    for recorder in _recorders:
        recorder.files.add(path)

def _open_with_track(path, *args, **kwargs):
    using_file(path)
    return _original_open(path, *args, **kwargs)

# Setup open()
builtins.open = _open_with_track

@contextmanager
def track_open() :
    recorder = FileRecorder()
    _recorders.append(recorder)
    try:
        yield recorder
    finally:
        _recorders.remove(recorder)


