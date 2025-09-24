import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import pytest

try:
    import gevent
    from gevent.event import Event
    from gevent.lock import Semaphore
    from gevent.monkey import is_anything_patched
except ImportError:

    def is_anything_patched():
        return False


from blisswriter.utils import sync_utils


@pytest.mark.skipif(not is_anything_patched(), reason="Requires gevent patching")
def test_shared_lock_pool_gevent():
    """Test concurrent locking for the same key, locking the same key in the same greenlet
    and check that the lock pool does not leak.
    """
    keys = list(range(4))
    worker_keys = keys + keys  # one greenlet waiting for another for each key

    lockpool = sync_utils.SharedLockPool(timeout=3)
    barrier = _GeventBarrier(len(worker_keys))
    waited = []

    def worker(key):
        for _ in range(10):
            barrier.wait()
            t0 = time.perf_counter()
            with lockpool.acquire(key):
                waited.append(time.perf_counter() - t0)
                with lockpool.acquire(key):
                    gevent.sleep(0.001)

    glts = [gevent.spawn(worker, key) for key in worker_keys]
    try:
        glts_done = gevent.joinall(glts, raise_error=True, timeout=10)
        if len(glts) != len(glts_done):
            raise TimeoutError("test timed out")
    finally:
        gevent.killall(glts)

    assert len(lockpool) == 0, "pool leaks locks"
    print("Average wait time (expect ~=0.0005):", sum(waited) / len(waited))


class _GeventBarrier:
    """A simple barrier for greenlets, similar to threading.Barrier."""

    def __init__(self, max_count: int):
        self._max_count = max_count
        self._count = 0
        self._mutex = Semaphore()
        self._max_reached = Event()

    def wait(self):
        with self._mutex:
            max_reached = self._max_reached
            self._count += 1
            if self._count == self._max_count:
                max_reached.set()
                self._count = 0
                self._max_reached = Event()
        max_reached.wait()


@pytest.mark.skipif(is_anything_patched(), reason="Cannot test with gevent patching")
def test_shared_lock_pool_threading():
    """Test concurrent locking for the same key, locking the same key in the same thread
    and check that the lock pool does not leak.
    """
    # Use a sub-process so we can kill it on timeout.
    ctx = multiprocessing.get_context()
    p = ctx.Process(target=_test_shared_lock_pool_threading)
    p.start()
    try:
        p.join(timeout=10)
        if p.is_alive():
            raise TimeoutError("test timed out")
        if p.exitcode:
            raise RuntimeError("test failed")
    finally:
        p.kill()


def _test_shared_lock_pool_threading():
    assert not is_anything_patched()

    keys = list(range(4))
    worker_keys = keys + keys  # one thread waiting for another for each key

    barrier = threading.Barrier(len(worker_keys))
    lockpool = sync_utils.SharedLockPool(timeout=3)
    waited = []

    def worker(key):
        for _ in range(10):
            barrier.wait()
            t0 = time.perf_counter()
            with lockpool.acquire(key):
                waited.append(time.perf_counter() - t0)
                with lockpool.acquire(key):
                    time.sleep(0.001)

    with ThreadPoolExecutor(len(worker_keys)) as pool:
        list(pool.map(worker, worker_keys))

    assert len(lockpool) == 0, "pool leaks locks"
    print("Average wait time (expect ~=0.0005):", sum(waited) / len(waited))
