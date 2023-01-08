# # class Solution:
# def isPalindrome(x: int) :
#     mylist = list(str(x))
#     print(mylist)
#     list1 = mylist[::-1]
#     if mylist == list1:
#         return True

# a = isPalindrome(121)
# print(a)

# class Solution:
def intToRoman(num: int) -> str:
    rom_dict = {'I':1,'V':5,'X':10,'L':50 ,'C':100,'D':500,'M':1000}
    mylist = list(num)
    romlist = []
    for c in mylist:
        val = rom_dict.get(c)
        romlist.append(val)
    print(romlist)
    sum = 0
    for v,i in romlist:
        if v[i] >= v[i+1]:
            sum +=v[i]
        else:
            sum += v[i+1]-v[i]
    return sum


    # print(mylist)

a = intToRoman('LVIII')