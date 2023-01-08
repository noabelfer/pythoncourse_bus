# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         myset = set(nums)
#         mylist = list(range(1, len(nums) + 1))
#
#         a = 0
#         b = 0
#
#         a = sum(nums) - sum(myset)
#         b = sum(mylist) - sum(myset)
#
#         return (a, b)




# def findLongestChain( pairs: list[list[int]]):
#     counter = 0
#     max_chain = 0
#     pairs.sort(key=lambda x:x[0])
#
#     for i in range(len(pairs)):
#         if pairs[i][0] > pairs[counter][1]:
#             counter = i
#             max_chain +=1
#     return max_chain

    # for i,l in pairs:
    #     if sum(l[i]) is max():

# a = findLongestChain(pairs = [[1,2],[3,4],[5,6]])
# print(a)
# a = findLongestChain.([1,2],[3,4],[5,6]])


def countSubstrings(s: str) -> int:
    my_list = []
    len_1 = len(s)
    counter = 0
    print(len_1)
    for c in s:
        my_list.append(c)
    print(my_list)
    for i, v in range(1, len(my_list)):
        if v[i] == v[i+1]:
            print('a')
        #     counter+=1
        # return counter+ len_1

a = countSubstrings("aaa")
print(a)
