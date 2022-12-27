import os

from C10.text import TextFile


class Txt(TextFile):
    def __init__(self, path):
        super().__init__(path)
        if not self._file_exist:
            raise Exception(f"file {path} does not exist")
        if self._type != "txt":
            raise Exception ("file is not text")

    # def get_content(self):
    #     self.open()

    def get_content(self) -> str:
        self._open()
        st = self._file_handle.read()
        self._file_handle.close()
        return st

    def get_words_num(self):
        spaces = self.get_content().split(' ')
        return len(spaces)

    def get_avg_word_len(self):
        spaces = self.get_content().split(' ')
        charecters = len(self.get_content())
        alpha_c = charecters - len(spaces)
        avg = alpha_c / len(spaces)
        return avg



    def __add__(self, toadd):
        st = self.get_content() + toadd.get_content()
        fname = self._dir_path + '/' + self.basename + '_' + toadd.basename + '.txt'
        if os.path.exists(fname):
            raise Exception(f'File {fname} exists!')
        fh = open(fname, "wt")
        fh.write(st)
        fh.close()
        added = Txt(fname)
        return added



a = Txt("/Users/noabelfer/Downloads/alice_in_wonderland.txt")
print(a)
print(a.get_avg_word_len())
# print(a.get_size())
# aaa = Txt("/Users/noabelfer/Downloads/alice_in_wonderland.txt")
# bbb = Txt("/Users/noabelfer/Downloads/sample3.txt")
# d = (aaa + bbb)