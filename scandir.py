import os

def scandir(path, time, ignore_dirs=[], max_depth=None):
    """
    Scan a path for files edited since time where time is seconds since epoch
    Do not recursively check any directories in ignore_dirs if ignore_dirs is a list
    If ignore_dirs is True then do not check any subdirectories
    max_depth is an optional integer to specify recursion depth

    returns list of file paths edited since given time
    """
    paths = []
    for f in os.scandir(path):

        if f.is_file() and f.stat().st_mtime >= time:
            paths.append(f.path)

        elif f.is_dir() and (ignore_dirs == False or (type(ignore_dirs) == list and f.name not in ignore_dirs)) and max_depth is not None and max_depth > 0 :
            paths.extend(scandir(f.path, time, ignore_dirs, max_depth - 1))

    return paths
