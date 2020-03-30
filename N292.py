"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table,
each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner.
You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.

"""

class Solution:
    def canWinNim1(self, n: int):
        if n % 4 == 0:
            return False
        else:
            return True

    def canWinNim2(self, n: int):
        return n%4 != 0

    def canWinNim3(self, n: int):
        if n < 3 :
            return True
        elif n == 4:
            return False
        else:
            return self.canWinNim3(n-4)


n = 200

test = Solution()

print(test.canWinNim1(n))
print(test.canWinNim2(n))
print(test.canWinNim3(n))