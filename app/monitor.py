# Monitoring For Code Changes.
# https://modwsgi.readthedocs.io/en/develop/user-guides/reloading-source-code.html

from __future__ import print_function
import os
import sys
import time
import signal
import threading
import atexit
import queue

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


base_dir = os.path.dirname(os.path.abspath(__file__))

_interval = 1.0
_times = {}
_files = []

for file in find_all_files(base_dir):
    if (".pyd" not in file and ".pyo" not in file and ".pyc" not in file and ".py" in file) or ".html" in file:
        _files.append(file)

_running = False
_queue = queue.Queue()
_lock = threading.Lock()


def _restart(path):
    _queue.put(True)
    prefix = 'monitor (pid=%d):' % os.getpid()
    print('%s Change detected to \'%s\'.' % (prefix, path), file=sys.stderr)
    print('%s Triggering process restart.' % prefix, file=sys.stderr)
    os.kill(os.getpid(), signal.SIGINT)


def _modified(path):
    try:
        # If path doesn't denote a file and were previously
        # tracking it, then it has been removed or the file type
        # has changed so force a restart. If not previously
        # tracking the file then we can ignore it as probably
        # pseudo reference such as when file extracted from a
        # collection of modules contained in a zip file.

        if not os.path.isfile(path):
            return path in _times

        # Check for when file last modified.

        mtime = os.stat(path).st_mtime
        if path not in _times:
            _times[path] = mtime

        # Force restart when modification time has changed, even
        # if time now older, as that could indicate older file
        # has been restored.

        if mtime != _times[path]:
            return True
    except:
        # If any exception occured, likely that file has been
        # been removed just before stat(), so force a restart.

        return True

    return False


def _monitor():
    while 1:
        # Check modification times on all files in sys.modules.
        modules = sys.modules.copy()
        for module in modules:
            if not hasattr(module, '__file__'):
                continue
            path = getattr(module, '__file__')
            if not path:
                continue
            if os.path.splitext(path)[1] in ['.pyc', '.pyo', '.pyd']:
                path = path[:-1]
            if _modified(path):
                return _restart(path)

        # Check modification times on files which have
        # specifically been registered for monitoring.

        for path in _files:
            if _modified(path):
                return _restart(path)

        # Go to sleep for specified interval.

        try:
            return _queue.get(timeout=_interval)
        except:
            pass


_thread = threading.Thread(target=_monitor)
_thread.setDaemon(True)


def _exiting():
    try:
        _queue.put(True)
    except:
        pass
    _thread.join()


atexit.register(_exiting)


def track(path):
    if not path in _files:
        _files.append(path)


def start(interval=1.0):
    global _interval
    if interval < _interval:
        _interval = interval

    global _running
    _lock.acquire()
    if not _running:
        prefix = 'monitor (pid=%d):' % os.getpid()
        print("%s Reloading %s files, under the \"%s\"" %
              (prefix, len(_files), base_dir))
        print('%s Starting change monitor.' % prefix, file=sys.stderr)
        _running = True
        _thread.start()
    _lock.release()
