"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""

import math
class Solution:
    def arrangeCoins1(self, n: int) -> int:
        start, end = int(math.sqrt(n)),n
        mid = start + (end - start) // 2
        while start <= end:
            if mid*(mid+1) //2 > n:
                end = mid -1
            elif mid*(mid+1) //2 < n:
                start = mid +1
            else:
                return mid
            mid = start + (end - start) // 2
        return mid

    def arrangeCoins2(self, n: int) -> int:
        start, end = int(math.sqrt(n)) , n
        mid = start + (end - start) // 2
        while start <= end:
            # mid = start + (end - start) // 2
            if mid*(mid+1) //2 > n:
                end = mid -1
                mid = start + (end - start) // 2
            elif mid*(mid+1) //2 < n:
                start = mid +1
                mid = start + (end - start) // 2
            else:
                return mid
        return mid

    def arrangeCoins3(self, n: int) -> int:
        start, end = int(math.sqrt(n)), int(math.sqrt(2*n))
        mid = start + (end - start) // 2
        while start <= end:
            if mid*(mid+1) //2 > n:
                end = mid -1
            elif mid*(mid+1) //2 < n:
                start = mid +1
            else:
                return mid
            mid = start + (end - start) // 2
        return mid

n =800
test = Solution()
print(test.arrangeCoins1(n))
print(test.arrangeCoins2(n))
print(test.arrangeCoins3(n))