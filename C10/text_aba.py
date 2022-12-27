#!/usr/bin/env python

import os
import pathlib


class TextFile:
    def __init__(self, path: str):
        self._path: str = path
        self._exist: bool = os.path.exists(path)
        self._suffix: str = pathlib.Path(path).suffix
        self._filename = os.path.basename(path)
        self._dir_path: str = self._path.replace(self._filename, '')
        self.filename = self._filename.replace(".txt", "").replace(".csv", "").replace(".json", "")

    def __str__(self):
        return f'path: {self._path},exist: {self._exist},suffix: {self._suffix},dirpath: {self._dir_path},filename {self.filename}'

    def __repr__(self):
        return f'TextFile({self._path})'

    def get_file_size(self) -> int:
        if not self._exist:
            return -1
        file_stats = os.stat(self._path)
        return file_stats.st_size

    def _open(self):
        if not self._exist:
            return -1
        self._file_handle = open(self._path, "rt")


