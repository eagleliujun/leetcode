"""
Given an integer, write a function to determine if it is a power of three.
Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

"""
import math
class Solution:
    def isPowerOfThree1(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 3 != 0:
            return False
        else:
            return self.isPowerOfThree1(n/3)

    def isPowerOfThree2(self, n: int) -> bool:
        while n >=1:
            if n == 1:
                return True
            elif n %3 != 0:
                return False
            n = n/3

    def isPowerOfThree3(self, n: int) -> bool:
        n_set = {1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907,43046721,129140163,387420489,1162261467}
        if n in n_set:
            return True
        return False

    # def isPowerOfThree4(self, n: int) -> bool:
    #     return False if n == 0 else pow(3, math.log(n, 3)) == n


    # def isPowerOfThree3(self, n: int) -> bool:  #
    #     a = list(str(n))
    #     if a == 3 or a == 1 : return True
    #     if a[-1] not in ('1','3','7','9') or '0' in a:
    #         return False
    #     sumd = 0
    #     for i in a:
    #         sumd += int(i)
    #     if sumd % 9:
    #         return False
    #     else:
    #         return True


n=243

test = Solution()
print(test.isPowerOfThree1(n))
print(test.isPowerOfThree2(n))
print(test.isPowerOfThree4(n))