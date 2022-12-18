import string


def letter_index(letter:str) ->int:

    if letter not in string.ascii_letters:
        raise Exception("not abc letter")
    if letter.islower():
        return string.ascii_lowercase.find(letter)+1
    return string.ascii_uppercase.find(letter)+1

a= ['e','s','h','a','p']

print(list(map(letter_index,a)))



