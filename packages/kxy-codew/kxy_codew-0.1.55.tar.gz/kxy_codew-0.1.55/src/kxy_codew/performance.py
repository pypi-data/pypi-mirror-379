import cProfile
import io
import marshal
import tempfile
import requests
import threading
import atexit
import time

from .config import CODEW_API_URL
from .state import KXYState

__profiler = cProfile.Profile()
kxy_state = KXYState()


def push_results(profiler):
    try:
        upload_url = CODEW_API_URL + "/kxy/upload"
        buf = io.BytesIO()
        profiler.create_stats()
        marshal.dump(profiler.stats, buf)
        buf.seek(0)
        files = {"file": ("profile.prof", buf, "application/octet-stream")}
        response = requests.post(upload_url, files=files, headers={"secret": kxy_state.get_secret()}, timeout=5, verify=False)
        if response.status_code != 200:
            print(f"Failed to send profile: {response.status_code} - {response.text}")
            return None
        return response.json().get("id")
    except requests.RequestException as e:
        print("Error connecting to 7176")


def profile(func):
    def wrapper(*args, **kwargs):
        print(f"Profiling {func.__name__}...")
        if kxy_state.performance_enabled:
            _profiler = cProfile.Profile()
            _profiler.enable()
            try:
                result = func(*args, **kwargs)
                _profiler.disable()
            except Exception as e:
                _profiler.disable()
                raise e
            finally:
                print("Profiling complete.")
                push_results(_profiler)
            return result
        else:
            return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


def end_kxy(_time=None):
    global __profiler
    if _time:
        time.sleep(_time)
    __profiler.disable()
    push_results(__profiler)


def pause_profiling():
    global __profiler
    __profiler.disable()


def resume_profiling():
    global __profiler
    __profiler.enable()


def init_kxy(_time=None):
    global __profiler
    __profiler.enable()
    if _time:
        end_thread = threading.Thread(target=end_kxy, args=(_time,), daemon=True)
        end_thread.start()
    atexit.register(end_kxy, None)
