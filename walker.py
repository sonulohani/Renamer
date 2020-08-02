import os
from enum import Flag, auto


class Walker:
    class Filter(Flag):
        FILE = auto()
        DIRECTORY = auto()
        FILE_AND_DIRECTORY = FILE & DIRECTORY

    def __init__(self, path, filter_=Filter.FILE_AND_DIRECTORY) -> None:
        self._path = path
        self._filter = filter_

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, p):
        self._path = p

    @property
    def filter_(self):
        return self._filter

    @filter_.setter
    def filter_(self, f):
        self._filter = f

    def walk():
        pass

