import os


class DirEnv:
    """Environment to execute command in dir safely"""

    def __init__(self, dir_pth):
        self._cwd = os.getcwd()
        self._dir_pth = dir_pth

    def __enter__(self):
        os.chdir(self._dir_pth)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._cwd)
