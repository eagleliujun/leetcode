"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""


def shiftGrid1(grid, k):
    grid_new = shift_one(grid)
    for i in range(1,k):
        grid_new = shift_one(grid_new)
    return grid_new


def shift_one(grid):
    lens_element = len(grid[0])
    lens_grid = len(grid)
    # grid_new = [[1]*lens_element]*lens_grid
    # this can not work , change one element --》change all same postion
    # list * n—>n shallow copies of list concatenated
    grid_new = [[0]*lens_element for i in grid]
    x = 0
    y = 0
    for i in range(lens_grid):
        for j in range(lens_element):
            if j == lens_element-1 and i == lens_grid -1:
                y = 0
                x = 0
            elif j == lens_element-1:
                x = i+1
                y = 0
            else:
                x = i
                y = j + 1
            grid_new[x][y] = grid[i][j]
    return grid_new


def shiftGrid2(grid,k):
    lens_element = len(grid[0])
    lens_grid = len(grid)
    x = (k % (lens_grid*lens_element)) // lens_element
    # 选出需要初始移动的主list长度
    y = k % lens_element  # 选出初始需要移动的子list长度
    grid_new = [[0] * lens_element for i in grid]
    for i in range(lens_grid):
        for j in range(lens_element):    # x：新主list;  y：新子list; i:旧主list； j:旧子list
            if y >= lens_element:        # 超出子list长度
                y = y % lens_element     # 取出需要移动的子list：其实就是 y=0
                x += 1                   # 主list移动一位
            if x >= lens_grid:           # 超出主list长度
                x = x % lens_grid        # 主list 移动到下一位置 :其实就是x=0
            grid_new[x][y]=grid[i][j]
            y += 1                       # 子list移动一位
    return grid_new


def shiftGrid2b(grid, k):
    lens_element = len(grid[0])
    lens_grid = len(grid)
    x = (k % (lens_grid*lens_element)) // lens_element
    # 选出需要初始移动的主list长度
    y = k % lens_element  # 选出初始需要移动的子list长度
    grid_new = [[0] * lens_element for i in grid]
    for i in range(lens_grid):
        for j in range(lens_element):     # x：新主list;  y：新子list; i:旧主list； j:旧子list
            grid_new[x][y] = grid[i][j]
            y = (y+1) % lens_element      # 取出需要移动的子list
            if y == 0:
                x=(x+1)%lens_grid            # 主list 移动到下一位置
    return grid_new


def shiftGrid3(grid, k):
    m, n = len(grid), len(grid[0])
    k = k % (m * n)                 # 保证移动在本二维数组中
    res = [[None for _ in range(n)] for _ in range(m)]  # 生成空二维数组
    for i in range(m):
        for j in range(n):          # x：新主list;  y：新子list; i:旧主list； j:旧子list
            y = (j + k) % n         # 子list位置 = （原本子位置+移动位置）% 子list长度
            x = (i + (j + k) // n) % m
            # 主list位置 = （（原本主位置+（原本子位置+移动位置）//子list长度）%主list长度
            res[x][y] = grid[i][j]
    return res


grid = [[1,2,3],[4,5,6],[7,8,9]]
grid1 = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
grid2 = [[1]]
grid3 = [[1],[2],[3],[4],[7],[6],[5]]
print(shiftGrid1(grid1,23))
print(shiftGrid2b(grid1,23))
print(shiftGrid3(grid1,23))
