
def judgeCircle( moves: str) -> bool:
    lst = []
    for letter in moves:
        lst.append(letter)
    print(lst)
    if (lst.count('U') != lst.count('D')) or (lst.count('R') != lst.count('L')):
        return False
    else:
        return True

a = judgeCircle('LRU')
print(a)