# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
import numpy as np
from numpy import reshape


# class Solution:
def matrixReshape( mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    count = 0
    newlist = []
    for element in mat:
        count += len(element)
    print(count)
    print(r*c)
    if count < r*c:
        print(mat)
        return mat
    else:
        mat = np.array(mat)
        print(mat)  # Output: [[1 2 3]
        #          [4 5 6]]

        # Reshape the matrix
        r = 2
        c = 3
        reshaped_mat = reshape(mat, r, c)


        for element in mat:
            for n in element:
                newlist.append(n)
                print(newlist)
                return newlist



a = matrixReshape( mat = [[1,2],[3,4]], r = 1, c = 4)
# Output: [[1,2],[3,4]]
print (a)




