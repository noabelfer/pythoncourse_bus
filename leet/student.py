# class Solution:
#     def checkRecord(self, s: str) -> bool:
#         mylist = []
#         for c in s:
#             mylist.append(c)
#         if mylist.count('A') < 2 and s.count('LLL') < 1:
#             return True

#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) -> list:
        n1 = int(''.join(map(str,l1))[::-1])
        n2 = int(''.join(map(str,l2))[::-1])
        s = n1+n2
        print(s)
        mylist = []
        for digit in list(str(s)):
            mylist.append(str(digit))
        return mylist[::-1]


a = Solution()
print(a.addTwoNumbers([2,4,3], [5,6,4]))
