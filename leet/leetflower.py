# class Solution:
# def canPlaceFlowers( flowerbed: list[int], n: int) -> bool:
#     num_1 = flowerbed.count(1)
#     print(num_1)
#     for i in flowerbed:
#         if (len(flowerbed)%2) == 0:
#             if n +num_1 < (((len(flowerbed)/2)-2)):
#                 return True
#             return False
#         if (len(flowerbed)%2) != 0:
#             if n+num_1 < ((((len(flowerbed)+1)/2)-2)):
#                 return True
#             return False
#
# a = canPlaceFlowers(flowerbed=(1,0,0,0,0,0,1), n=3)
#
# print(a)



def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    a = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i ==0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
            a+=1
    if n <= a:
        return True
    else:
        return False

a = canPlaceFlowers(flowerbed=[0,1,0,0,1], n=0)

print(a)




