"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
 and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

"""

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        centre = 5
        m= len(grid)
        standard = [[2,9,4],[7,5,3],[6,1,8]]
        result= 0
        index = []

        for i in grid:
            j = i.find(2)
            if j != -1 :
                index.append([i,j])
        for i in range(1,m-1):
            for j in range(1,m-1):
                if grid[i][j] == 5:
                    index1 = grid[i-1].index(2,i-1,j+1)
                    index2 = grid[i-1].index(4,i-1,j+1)
                    index3 = grid[i+1].index(2,i+1,j+1)
                    index4 = grid[i + 1].index(4, i + 1, j + 1)



