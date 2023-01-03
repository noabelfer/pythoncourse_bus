# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

import matlab
from numpy import *


# class Solution:
def matrixReshape( mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    count = 0
    newlist = []
    newlist1 = []
    for element in mat:
        count += len(element)
    print(count)
    print(r*c)
    if count < r*c:
        print(mat)
        return mat
    else:
        for element in mat:
            for n in element:
                newlist.append(n)
        print(newlist)
        print(newlist1)
        newlist1 = reshape(newlist, r, c)

        print(newlist1)





a = matrixReshape( mat = [[1,2],[3,4]], r = 4, c = 1)
# Output: [[1,2],[3,4]]
print (a)




