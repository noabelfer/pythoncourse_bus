# class Solution:
def longestCommonPrefix( strs: list[str]) -> str:
    strs = sorted(strs, key = len)
    i = 0
    while strs[0][i] == strs[-1][i]:
        i += 1
    while True:
        for j in range(len(strs)-1):
            if strs[j][i] == strs[j+1][i]:
                return i
                # return strs[0][i]

        for k, v in enumerate(strs):
            print(strs[0][k])




a = longestCommonPrefix(["flower","flow","flight"])
print(a)




