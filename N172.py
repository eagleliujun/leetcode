"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

"""

def trailingZeroes1(n):
    sum = 0
    while n >= 1:
        n = n // 5
        sum += n
    return sum

def trailingZeroes2(n):
    if n==0:
        return 0
    return n//5 + trailingZeroes2(n//5)


print(trailingZeroes2(30))