

class Ebook:
    def __init__(self, _book_path:str, num_words_page, bookmarks:dict = None):
        self._book_path = _book_path
        self.num_words_page = num_words_page
        self.pages = {int:str}
        self.bookmarks = {}
        # self.page_read = 1
        self.current_page = 1
        self.current_page_words = []

        with open(_book_path, 'r') as fh:
            content = fh.read()
            word_list = content.split()
            current_page = 1
            current_page_words = []
            for i, word in enumerate(word_list):
                current_page_words.append(word)
                if (i + 1) % num_words_page == 0:
                    # reached the end of a page, store it in the pages dictionary
                    self.pages[self.current_page] = current_page_words
                    self.current_page += 1
                    current_page_words = []
            # handle the case where there are remaining words on the last page
            if current_page_words:
                self.pages[current_page] = current_page_words

    def __str__(self):
        return f'content:{self.get_page_content(self.current_page)}'

    def __iter__(self):
        self.iter_page = 1
        return self

    def __next__(self):
        if self.iter_page > len(self.pages):
            raise StopIteration
        content = self.get_page_content(self.iter_page)
        # if self.pages == len(self.pages.keys()):
        self.iter_page += 1
        return content


    def get_page_content(self,page_num):
        value = self.pages.get(page_num, None)
        print(value)

    def pages_amnt(self):
        a = self.pages.keys()
        pages_amnt = len(a)
        return pages_amnt

    def store_bookmarks(self,page_number:int, bookmark_name:str) -> dict:
        try:
            if page_number not in self.pages.keys():
                raise Exception("out of range")
            if page_number not in self.bookmarks.keys():
                self.bookmarks[page_number] = bookmark_name
            else:
                self.bookmarks[page_number].append(bookmark_name)
        except Exception as e:
            print(e)


    def delete_bookmark(self, bookmark_name):
        if bookmark_name in self.bookmarks.values():
            self.bookmarks = {key:val for key, val in self.bookmarks.items() if val != bookmark_name}
        else:
            print("not an existing bookmark")



    # def pages(self,num_words_page):
    #     for
if __name__ == '__main__':
    i = 20
    try:
        ebook = Ebook("/Users/noabelfer/Downloads/alice_in_wonderland (1).txt", 300)
        # pages = ebook.pages_amnt()
        # ebook.get_page_content(1)
        ebook.store_bookmarks(2,'noa')
        # print(ebook.bookmarks)
        # ebook.store_bookmarks(2,'noggg')
        ebook.delete_bookmark('dsda')
        print(ebook.bookmarks)
        # next(ebook)
    #     for page in ebook:
    #         print(next)
    #         i+=1
    except Exception as e:
        print(e)

