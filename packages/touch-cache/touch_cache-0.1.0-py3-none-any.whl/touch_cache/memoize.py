import os
import json
import hashlib
import functools
import cloudpickle
import inspect
from .open_track import track_open
import logging
import glob
logger  = logging.getLogger("touch_cache")

CACHE_DIR = ".cache"


def set_cache_dir(cache_dir) :
    global CACHE_DIR
    CACHE_DIR = cache_dir

def _ensure_cache_dir() :
    os.makedirs(CACHE_DIR, exist_ok=True)
    return CACHE_DIR


def clean_cache():
    files = glob.glob(f'{CACHE_DIR}/*')
    for f in files:
        os.remove(f)

def get_bound_args(func, *args, **kwargs):
    sig = inspect.signature(func)
    bound = sig.bind(*args, **kwargs)
    bound.apply_defaults()  # remplit les valeurs par défaut si non fournies
    return bound.arguments  # OrderedDict : param_name -> value

def _mtime(file) :
    return os.stat(file).st_mtime_ns

def _get_globals_rec(func) :

    """List globals used by a function, recursively"""
    seen_funcs = set()
    globals_used = {}

    def _rec(func):

        # Avoid infinite recursion
        if func in seen_funcs :
            return
        seen_funcs.add(func)

        # Look for globals in code
        code = func.__code__
        for name in code.co_names:
            if name in func.__globals__ and name != "__builtins__":
                obj = func.__globals__[name]

                # Function ? => recurse
                if hasattr(obj, "__code__") :
                    _rec(obj)
                    continue

                try:
                    globals_used[name] = func.__globals__[name]
                except Exception:
                    globals_used[name] = "<unrepresentable>"

    _rec(func)
    return globals_used



def touch_cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        cache_dir = _ensure_cache_dir()
        func_name = func.__name__

        # 1) Hash of the function itself
        func_bytes = cloudpickle.dumps(func)
        func_hash = hashlib.sha256(func_bytes).hexdigest()

        # 2) Collect globals used
        globals_used= _get_globals_rec(func)

        # 3) Hash of arguments + globals
        bound_args = get_bound_args(func, *args, **kwargs)
        data_to_hash = {"bound_args": bound_args, "globals": globals_used}
        param_bytes = cloudpickle.dumps(data_to_hash)
        param_hash = hashlib.sha256(param_bytes).hexdigest()

        # 4) Cache file paths
        base_name = f"{func_name}-{param_hash}"
        pickle_path = os.path.join(cache_dir, base_name + ".pickle")
        json_path = os.path.join(cache_dir, base_name + ".json")

        # 5) Try loading from cache if exists
        if os.path.exists(pickle_path) and os.path.exists(json_path):
            try:
                with open(json_path, "r") as f:
                    meta = json.load(f)
                files_used = meta.get("files_used", [])

                # Check if any file is newer than the pickle
                pickle_mtime = _mtime(pickle_path)
                invalid = False
                for file_path in files_used:

                    if not os.path.exists(file_path):
                        logger.warning(f"[{func_name}] Should not happend : File {file_path} not found")
                        invalid = True
                        break

                    if _mtime(file_path) > pickle_mtime:
                        logger.info(f"[{func_name}] File {file_path} changed. Recomputing")
                        invalid = True
                        break

                if not invalid:
                    logger.info(f"[{func_name}] Already in cache. Loading pickle")
                    with open(pickle_path, "rb") as f:
                        return cloudpickle.load(f)

            except Exception:
                pass  # fallback: recompute

        # 6) Call the function with file tracking
        with track_open() as file_tracker:
            result = func(*args, **kwargs)
            files_used = list(file_tracker.files)

        # 7) Save result and metadata
        try:
            with open(pickle_path, "wb") as f:
                cloudpickle.dump(result, f)
        except Exception as e:
            logger.error(f"[{func_name}] Error saving pickle cache: {e}")

        metadata = {
            "function_hash": func_hash,
            "parameter_hash": param_hash,
            "bound_args": {k: repr(v) for k, v in bound_args.items()},
            "globals_used": {k: repr(v) for k, v in globals_used.items()},
            "files_used": files_used,
        }
        try:
            with open(json_path, "w") as f:
                json.dump(metadata, f, indent=2)
        except Exception as e:
            logger.error(f"[{func_name}] Error saving JSON metadata: {e}")

        return result

    return wrapper
