"""

On an 8 x 8 chessboard, there is one white rook.
There also may be empty squares, white bishops, and black pawns.
These are given as characters 'R', '.', 'B', and 'p' respectively.
Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
 then moves in that direction until it chooses to stop, reaches the edge of the board,
 or captures an opposite colored pawn by moving to the same square it occupies.
 Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:
Input:
[[".",".",".",".",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 [".",".",".","R",".",".",".","p"],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.

Example 2:

Input:
[[".",".",".",".",".",".",".","."],
 [".","p","p","p","p","p",".","."],
 [".","p","p","B","p","p",".","."],
 [".","p","B","R","B","p",".","."],
 [".","p","p","B","p","p",".","."],
 [".","p","p","p","p","p",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
Bishops are blocking the rook to capture any pawn.

Example 3:

Input:
[[".",".",".",".",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 ["p","p",".","R",".","p","B","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".","B",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 [".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook can capture the pawns at positions b5, d6 and f5.

Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""


def numRookCaptures1(board):
    mark = [0, 0, 0, 0]
    a, b, c = 0, 0, 0
    for index2, value2 in enumerate(board):
        for index3, value3 in enumerate(value2):
            if value3 == 'R':
                a, b, c = index2, index3, 1
                break
        if c == 1:
            break
    for index, value in enumerate(board):
        if index < a:
            if value[b] == 'p':
                mark[0] = 1
            elif value[b] == 'B':
                mark[0] = 0
        elif index == a:
            for i in range(len(value)):
                if i < b:
                    if value[i] == 'p':
                        mark[1] = 1
                    elif value[i] == 'B':
                        mark[1] = 0
                elif i > b:
                    if value[i] == 'p':
                        mark[2] = 1
                        break
                    elif value[i] == 'B':
                        mark[2] = 0
                        break
        else:
            if value[b] == 'p':
                mark[3] = 1
                break
            elif value[b] == 'B':
                mark[3] = 0
                break
    return sum(mark)


def numRookCaptures2(board):
    mark = [0 for _ in range(len(board[0]))]
    mark1, mark2, mark3 = 0, 0, 0
    result = 0
    for index1, value1 in enumerate(board):
        for index2, value2 in enumerate(value1):
            if value2 == 'R':
                mark1, mark2, mark3 = index1, index2, 1
                result += mark[index2]  # up
            elif mark1 == 0 and mark3 == 0:
                if value2 == 'B':
                    mark[index2] = 0
                elif value2 == 'p':
                    mark[index2] = 1
            else:
                break
        if mark3 != 0:
            if value1[mark2] == 'B':
                break
            elif value1[mark2] == 'p':
                result += 1
                break  # dn
    for value in range(mark2 - 1, -1, -1):
        if board[mark1][value] == 'p':  # left
            result += 1
            break
        elif board[mark1][value] == 'B':
            break
    for value in range(mark1 + 1, len(board[0])):
        if board[mark1][value] == 'p':
            result += 1
            break
        elif board[mark1][value] == 'B':
            break
    return result


def numRookCapturer3(board):
    lens_b = len(board[0])
    lens_a = len(board)
    result = 0
    mark = [0 for _ in range(lens_b)]
    mark1, mark2 = 0, 0
    for index, value in enumerate(board):
        mark[index] = ''.join(value)
        if mark[index].find('R') != -1:
            mark2 = mark[index].find('R')
            mark1 = index
    # print(mark,mark1,mark2)
    for i in range(mark1 - 1, -1, -1):  # up
        if mark[i][mark2] == 'B':
            break
        elif mark[i][mark2] == 'p':
            result += 1
            break
    for i in range(mark1 + 1, lens_b, 1):  # down
        if mark[i][mark2] == 'B':
            break
        elif mark[i][mark2] == 'p':
            result += 1
            break
    for i in range(mark2 - 1, -1, -1):  # left
        if mark[mark1][i] == 'B':
            break
        elif mark[mark1][i] == 'p':
            result += 1
            break
    for i in range(mark2 + 1, lens_a, 1):  # right
        if mark[mark1][i] == 'B':
            break
        elif mark[mark1][i] == 'p':
            result += 1
            break
    return result


def numRookCapturer4(board):
    mark1, mark2 = 0, 0
    result = 0
    lens_b = len(board[0])
    lens_a = len(board)
    for index1, value1 in enumerate(board):
        # try:
        #     mark2 = value1.index('R')
        #     mark1 = index1
        #     break
        # except ValueError:
        #     continue

        if 'R' in value1:
            mark2 = value1.index('R')
            mark1 = index1
            break
        else:
            continue



    for i in range(mark1 - 1, -1, -1):  # up
        if board[i][mark2] == 'B':
            break
        elif board[i][mark2] == 'p':
            result += 1
            break
    for i in range(mark1 + 1, lens_b, 1):  # down
        if board[i][mark2] == 'B':
            break
        elif board[i][mark2] == 'p':
            result += 1
            break
    for i in range(mark2 - 1, -1, -1):  # left
        if board[mark1][i] == 'B':
            break
        elif board[mark1][i] == 'p':
            result += 1
            break
    for i in range(mark2 + 1, lens_a, 1):  # right
        if board[mark1][i] == 'B':
            break
        elif board[mark1][i] == 'p':
            result += 1
            break
    return result


# def numRookCapturer5(board): # dict version can not work, more complexity ,give up
#     lens_b = len(board[0])
#     lens_a = len(board)
#     result = 0
#     mark3 = 0
#     mark = {i: -1 for i in range(lens_b)}
#     mark1, mark2 = 0, 0
#     for index1, value1 in enumerate(board):
#         for index2, value2 in enumerate(value1):
#             if value2 == 'p':
#                 mark[index2] = 1
#             elif value2 == 'B':
#                 mark[index2] = 0
#             elif value2 == 'R':
#                 result = 0 if mark[index2] == -1 else mark[index2]  # up
#                 mark1, mark2, mark3 = index1, index2, 1
#             else:
#                 mark[index2] =
#         if mark3 == 1:
#             break
#     # print(mark1,mark2,mark)
#     for i in range(mark1 + 1, lens_a, 1):  # down
#         if board[i][mark2] == 'B':
#             break
#         elif board[i][mark2] == 'p':
#             result += 1
#             break
#     for i in range(mark2 - 1, -1, -1):  # left
#         if mark[i] == 0:
#             break
#         elif mark[i] == 1:
#             result += 1
#             break
#     for i in range(mark2 + 1, lens_b, 1):  # right
#         if mark[i] == 0:
#             break
#         elif mark[i] == 1:
#             result += 1
#             break
#     return result


class Solution:
    def helper(self, board, x, y, di):       # ref from solution
        if (x < 0 or y < 0 or x >= 8 or y >= 8):
            return 0
        if (board[x][y] == '.' or board[x][y] == "R"):
            if (di == 0):
                return self.helper(board, x + 1, y, di)
            elif (di == 1):
                return self.helper(board, x - 1, y, di)
            elif (di == 2):
                return self.helper(board, x, y + 1, di)
            else:
                return self.helper(board, x, y - 1, di)
        elif (board[x][y] == "B"):
            return 0
        elif (board[x][y] == "p"):
            return 1

    def numRookCaptures(self, board) -> int:
        for i in range(8):
            for j in range(8):
                if (board[i][j] == "R"):
                    break
            if (board[i][j] == "R"):
                break
        su = 0
        su += self.helper(board, i, j, 0)
        su += self.helper(board, i, j, 1)
        su += self.helper(board, i, j, 2)
        su += self.helper(board, i, j, 3)
        return su

board = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]

board2 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", "p", "p", "p", "p", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."],
          [".", "p", "B", "R", "B", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."],
          [".", "p", "p", "p", "p", "p", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]

board3 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", "p", "p", ".", ".", ".", "."],
          [".", "p", "p", "R", ".", "p", ".", "p"],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "p", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]
board4 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", "R", ".", ".", ".", "p"],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]
board5 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", "p", "p", ".", "p", "p", "."],
          [".", "p", ".", ".", ".", ".", ".", "p"],
          [".", ".", ".", ".", "R", ".", ".", "."],
          [".", "p", ".", ".", ".", ".", ".", "p"],
          [".", ".", "p", "p", ".", "p", "p", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]

print(numRookCaptures1(board2))
print(numRookCaptures2(board2))
print(numRookCapturer3(board4))
print(numRookCapturer4(board4))
