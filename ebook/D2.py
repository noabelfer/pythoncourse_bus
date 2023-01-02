from ebook.Ebook_val import EBook


class MyeBook(EBook):
    def __init__(self, book_path: str, words_num: int, start_page=0):
        super().__init__(book_path, words_num)
        self.__page_number = start_page
        if (start_page >= self.get_total_pages()):
            raise Exception(f'Page {start_page} is out of range of 0 to {self.get_total_pages() - 1} ')

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__page_number >= self.get_total_pages()):
            raise StopIteration
        self.__page_number += 1
        return self

    #     return self

    def __str__(self):
        return self.get_page_content(self.__page_number)


if __name__ == '__main__':
    i = 22
    try:
        book = MyeBook("/Users/noabelfer/Downloads/alice_in_wonderland (1).txt", 1000, i)
        for page in book:
            print('=======================' + str(i) + '====================================')
            print(page)
            i += 1
    except Exception as e:
        print(e)
