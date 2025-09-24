from time import sleep

from touch_cache import touch_cache, set_cache_dir, clean_cache
from pathlib import Path

INPUT_FILE ="/tmp/foo.txt"

_global_val = 1
_unused_global = 1
call_count=0


def setup_module():
    print("Init tests")
    set_cache_dir("/tmp/tst-cache/")
    clean_cache()
    create_input_file()


def create_input_file():
    with open(INPUT_FILE, "w") as f:
        f.write("foo")

def touch_input_file() :
    Path(INPUT_FILE).touch()

@touch_cache
def cached_add(a) :
    """Adds a and global_a. Increments _count"""

    # Fake opening of a file
    with open(INPUT_FILE, "rt") as f:
        pass

    global call_count, _global_val
    call_count += 1

    return a + _global_val

@touch_cache
def nested_add(a) :
    return _nested_add(a)

def _nested_add(a) :
    """Adds a and global_a. Increments _count"""

    # Fake opening of a file
    with open(INPUT_FILE, "rt") as f:
        pass

    global call_count, _global_val
    call_count += 1

    return a + _global_val

def call_add(a, global_val, nested=False) :
    """Call a function and returns wether is was called or not"""
    global _global_val, call_count
    call_count = 0
    _global_val = global_val
    if nested:
        res = nested_add(a)
    else:
        res = cached_add(a)
    return (call_count == 1), res



def test_should_use_cache():

    call_add(1, 1)

    called, res = call_add(1, 1)
    assert not called
    assert res == 2

def test_shouldnot_invalidate_cache_when_unused_global_changes():
    global _unused_global

    call_add(1, 1)

    _unused_global = 2

    called, res = call_add(1, 1)
    assert not called
    assert res == 2


def test_invalidate_cache_when_global_changes():

    call_add(1, 1)

    called, res = call_add(1, 2)
    assert called
    assert res == 3


def test_invalidate_cache_when_input_file_touched():

    call_add(1, 1)

    sleep(0.01)
    touch_input_file()

    called, res = call_add(1, 1)
    assert called
    assert res == 2

def test_nested() :

    assert call_add(1, 1, nested=True) == (True, 2)
    assert call_add(1, 1, nested=True) == (False, 2)
    assert call_add(1, 2, nested=True) == (True, 3)