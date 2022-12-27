import json
import text
from C10.text import TextFile

class Json(TextFile):
    def __init__(self, path):
        super().__init__(path)
        if not self._file_exist:
            raise Exception(f"file {path} does not exist")
        if self._type != "json":
            raise Exception ("file is not json")

    def is_list(self):
        self._open()
        data = json.load(self._file_handle)
        if type(data) == list:
            return True

    # def is_object(self):




a = Json("/Users/noabelfer/Downloads/sample2.json")
a.is_list()

