# class Solution:
def findErrorNums( nums: list[int]) -> list[int]:
    for i in nums:
        if nums.count(i) > 1:
            return (i, i+1)


a= findErrorNums(nums = [1,2,2,4])
print(a)
nums = [1,2,2,4]
# Output: [2,3]