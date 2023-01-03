# def fibo(indx):
#     if indx <= 1:
#         return indx
#     else:
#         return fibo(indx-1)+fibo(indx-2)
#
# a = fibo(8)
# print(a)

# class Solution:
def countBinarySubstrings(s: str) -> int:
    counter = 0
    for i in s:
        if (i.count('1') == i.count('0')):
            counter += 1
        else:
            return counter

a = countBinarySubstrings("00110011")
print(a)

