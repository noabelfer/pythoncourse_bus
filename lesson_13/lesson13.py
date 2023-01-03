import string

class AlphabetIterator:
    def __init__(self, character):
        self.character = character
        self.my_list = None
        if self.character not in string.ascii_letters:
            raise Exception("not abc letter")

    def __next__(self) -> str:
        self.i +=1
        if self.i == 26:
            raise StopIteration()
        return self.my_list[self.i]


    def __iter__(self):
        if self.character in string.ascii_lowercase:
            self.my_list = string.ascii_lowercase
            self.i = self.my_list.find(self.character)
            return self
        if self.character in string.ascii_uppercase:
            self.my_list = string.ascii_uppercase
            self.i = self.my_list.find(self.character)
            return self

try:
    character = input("insert character")
    for c in AlphabetIterator(character):
        print(c)
except Exception:
    print(" ")



