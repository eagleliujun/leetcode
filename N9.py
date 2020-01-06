"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x):

    return 1 if len(str(x))%2 ==1 and str(x)[0:(len(str(x))-1)/2] == str(x).reverse()[(len(str(x))-1)/2+1 :] else 0

x = 12345654321
print(isPalindrome(x))