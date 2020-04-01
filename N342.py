"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

"""
import math
class Solution:
    def isPowerOfFour1(self, num: int) -> bool:
        if num == 1:
            return True
        elif num % 4 != 0:
            return False
        else:
            return self.isPowerOfFour1(num / 4)

    def isPowerOfFour2(self, num: int) -> bool:
        while num >= 1:
            if num == 1:
                return True
            elif num % 4 != 0:
                return False
            num = num / 4

    def isPowerOfFour3(self, num: int) -> bool:
        return False if num == 0 else math.log(num, 4) == int(math.log(num, 4))

    def isPowerOfFour4(self, num: int) -> bool:
        return False if num == 0 else num in map(lambda x:pow(4,x),range(0,10))


n=1023

test = Solution()
print(test.isPowerOfFour1(n))
print(test.isPowerOfFour2(n))
print(test.isPowerOfFour3(n))
print(test.isPowerOfFour4(n))