def countBinarySubstrings(s: str) -> int:
    counter = 0
    for i in s:
        while len(i) >= 2:
            if s.count(len(i)) > 0:
                counter += 1
    return counter


a = countBinarySubstrings("00110011")
print(a)