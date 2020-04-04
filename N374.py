"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber1(self, n: int) -> int:
        start = 0
        end = n
        while True:
            gus = (start+end )/2
            if guess(gus) == -1:
                end = gus
            elif guess(gus) == 1:
                start = gus
            else:
                return int(gus)

    def guessNumber2(self, n: int) -> int:
        start = 0
        end = n
        gus = (start+end )/2
        while guess(gus) != 0:
            if guess(gus) == -1:
                end = gus
            elif guess(gus) == 1:
                start = gus
            gus = (start+end )/2
        return int(gus)

    def guessNumber3(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:                     #  =
            gus = start+(end - start)//2
            if guess(gus) == -1:
                end = gus-1                     # -1
            elif guess(gus) == 1:
                start = gus+1                   # +1
            else:
                return gus