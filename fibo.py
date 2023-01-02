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
        if ('1' and '0' in i) and s.count(i) >1:
            counter += 1
            continue
        else:
            return counter

a = countBinarySubstrings("00110011")
print(a)

