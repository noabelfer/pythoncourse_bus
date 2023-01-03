def countBinarySubstrings(s: str) -> int:
    counter = 0
    zero = 0
    one = 0

    for c in s:
        while int(len(s)) > len(c) > 1:
            if c.count('1') == c.count('0'):
                counter +=1
        # if c == '0':
        #     zero += 1
        # else:
        #     one += 1
        # if zero == one:
        #     counter += zero + one
    return counter

# class Solution:
# def countBinarySubstrings(s: str) -> int:
#     search = '01'
#     count  = 0
#     while len(search) <= len(s):
#         n1 = s.count(search)
#         n2 = s.count(search[::-1])
#         if((n1+n2) == 0):
#             break
#         count += (n1+n2)
#         search = '0'+search+'1'
#     return count

a = countBinarySubstrings("10101")
print(a)