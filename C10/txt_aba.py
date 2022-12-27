#!/usr/bin/env python

import os
import pathlib
import text_aba


class TxtFile(text_aba.TextFile):
    def __init__(self, path: str):
        super().__init__(path)
        if not self._exist:
            raise Exception(f"File {path} does not exist!")
        if self._suffix != ".txt":
            raise Exception(f"File {path} is not a text file!")

    def __repr__(self):
        return f'TxtFile({self._path})'

    def get_content(self) -> str:
        self._open()
        st = self._file_handle.read()
        self._file_handle.close()
        return st

    def suffix() -> str:
        return self._suffix

    def __add__(self, toadd):
        st = self.get_content() + toadd.get_content()
        fname = self._dir_path + self.filename + '_' + toadd.filename + '.txt'
        if os.path.exists(fname):
            raise Exception(f'File {fname} exists!')
        fh = open(fname, "wt")
        fh.write(st)
        fh.close()
        added = TxtFile(fname)
        return added

    def get_words_num(self) -> int:
        st = self.get_content()
        stsplit = st.split(' ')
        return len(stsplit)

    def get_avg_word_len(self) -> float:
        st = self.get_content()
        stsplit = st.split(' ')
        sum: float = 0
        for word in stsplit:
            sum += len(word)
        return (sum / len(stsplit))


aaa = TxtFile("/Users/noabelfer/Downloads/sample3.txt")
bbb = TxtFile("/Users/noabelfer/Downloads/alice_in_wonderland_sample3.txt")
print(aaa)
# print('file size aaa ', aaa.get_file_size(), ' bbb ', bbb.get_file_size())
# ccc = aaa + bbb
# print('type aaa ', type(aaa))
# print('type ccc ', type(ccc))
# print('file size ccc ', ccc.get_file_size())
# print('get_avg_word_len ', ccc.get_avg_word_len())
# print(ccc)
# print(repr(ccc))
# print('num words: ', ccc.get_words_num())
# # print(abc.get_content())
# ddd = abc.__add__('c:\\temp\\noa\\pythoncourse\\files\\bbb.txt')
# print('file size: ',ddd.get_file_size())