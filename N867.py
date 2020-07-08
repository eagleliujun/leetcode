"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000

"""
class Solution:
    def transpose1(self, A):
        lenv=len(A)
        lenh=len(A[0])
        res = [[] for _ in range(lenh)]
        for i in range(lenh):
            for j in range(lenv):
                res[i].append(A[j][i])
        return res

    def transpose2(self, A:list):
        lenv2 = len(A)
        lenh3 = len(A[0])
        lenA = min(len(A),len(A[0]))
        dt = lenh3-lenv2
        for i in range(lenA-1):
            for j in range(lenA-1):
                A[i][j+1],A[j][i+1] =A[j][i+1], A[i][j+1]
        if dt >0:
            for i in range(dt-1):
                A.append([])
                for j in range(dt-1):
                    A[lenv2+i][j]=A[lenh3+j][i+lenv2]
                del A[lenh3+j][i+lenv2:-1]
        elif dt < 0:
            for i in range(-dt-1):
                A[lenh3+i].append([])
                for j in range(-dt-1):
                    A[lenv2+j][i]=A[lenh3+i][j+lenv2]
            del A[lenh3:-1]
        return A






a= [[1,2,3],[4,5,6],[7,8,9]]
b= [[1,2,3],[4,5,6]]
test = Solution()
# print(test.transpose(a))
print(test.transpose2(b))