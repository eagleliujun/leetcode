"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in {1, 0}:
            return True
        start = 2
        end = num
        while start <= end:
            mid = (start + end) // 2
            if num / mid < mid:
                end = mid -1
            elif num / mid > mid:
                start = mid+1
            else:
                return True
        return False

test = Solution()
n=1024
print(test.isPerfectSquare(n))