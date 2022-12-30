class Solution:
    def checkRecord(self, s: str) -> bool:
        mylist = []
        for c in s:
            mylist.append(c)
        if mylist.count('A') < 2 and s.count('LLL') < 1:
            return True