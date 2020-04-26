"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

"""


class Solution:
    def islandPerimeter1(self, grid) -> int:
        # mark = [0 for i in range(len(grid[0]))]
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # up down left right
                        row, col = i + x, j + y
                        if not (0 <= row < len(grid) and 0 <= col < len(grid[i])):
                            sum += 1
                        elif grid[row][col] == 0:
                            sum += 1
        return sum

    def islandPerimeter2(self, grid) -> int:
        #r = c = 0
        def dfs(grid, r, c):
            if not ((0 <= r < len(grid) and 0 <= c < len(grid[0]))):
                return 1                    # out of range
            if (grid[r][c] == 0):
                return 1                    # water ,can add 1
            if (grid[r][c] != 1):
                return 0                    # travelled
            grid[r][c] = 2                  # travelled mark
            return dfs(grid, r - 1, c) + dfs(grid, r + 1, c) + dfs(grid, r, c - 1) + dfs(grid, r, c + 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (grid[r][c] == 1):
                    return dfs(grid, r, c)
        return 0

        #
        # return sum(sum(map(lambda x, y: x!=y, row + [0], [0] + row))
        #            for row in itertools.chain(grid, map(list, zip(*grid))))


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
test = Solution()
print(test.islandPerimeter1(grid))
print(test.islandPerimeter2(grid))
