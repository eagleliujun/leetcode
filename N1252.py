"""

Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Example 1:

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:
Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
Constraints:
1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m
"""


def oddCells1(n, m, indices):
    matrix_initial = [[0 for _ in range(m)] for _ in range(n)]
    result = 0
    for i in indices:
        matrix_initial[i[0]] = [matrix_initial[i[0]][k] + 1 for k in range(m)]
        #  line +1
        for v in range(n):
            matrix_initial[v][i[1]] += 1  # row+1
    for i in matrix_initial:  # calculate the odd
        for j in i:
            if j % 2 == 1:
                result += 1
    return result


def oddCells2(n, m, indices):
    line_num = [0 for _ in range(n)]
    row_num = [0 for _ in range(m)]
    result = 0
    for i in indices:
        line_num[i[0]] += 1
        row_num[i[1]] += 1
    for j in line_num:
        for k in row_num:
            # if (j % 2 == 1 and k %2 != 1) or (j%2 !=1 and k %2 == 1):
            #    result +=1
            result += ((j % 2 == 1 and k % 2 != 1) or (j % 2 != 1 and k % 2 == 1))
    return result


n = 2
m = 3
indices = [[0, 1], [1, 1]]
print(oddCells1(n, m, indices))
print(oddCells2(n, m, indices))
