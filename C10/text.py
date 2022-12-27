import os
import pathlib


class TextFile:
    def __init__(self, path:str):
        self._file_name = os.path.basename(path)
        self._path = path
        self._file_exist = os.path.exists(path)
        self._dir_path:str = os.path.dirname(path)
        self._suffix: str = pathlib.Path(path).suffix
        self._type = path.split('.')[-1]
        self.basename = self._file_name.replace(".txt", "").replace(".csv", "").replace(".json", "")


    def __str__(self):
        return f'_file_name:{self._file_name} path: {self._path},exist: {self._file_exist},suffix: {self._suffix}, type: {self._type}, dir: {self._dir_path}, base_name: {self.basename}'

    def get_size(self):
        file_size = os.path.getsize(self._path)
        return file_size

    def _open(self):
        if not self._file_exist:
            return -1
        self._file_handle = open(self._path,"rt")




    # def get_content(self):
    #     with open(self._path) as fh:
    #         content = self.get_content()




a = TextFile("/Users/noabelfer/Downloads/alice_in_wonderland.txt")




