import os

if "NO_HMR_DAEMON" not in os.environ:
    from threading import enumerate

    if any(t.name == "hmr-daemon" for t in enumerate()):
        if os.name == "nt":
            from . import windows
        else:
            from . import posix
