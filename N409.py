"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:

    def longestPalindrome1(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        count = 0
        for j in d:
            count += d[j] // 2 * 2
            if d[j] % 2 == 1 and count % 2 == 0:
                count += 1
        return count

    def longestPalindrome2(self, s: str) -> int:
        d = {}
        count = 0
        for i in s:
            if (i not in d) or d[i] == 0 :
                d[i] = 1
            else:
                count += 2
                d[i] = 0
        for j in d.values():
            if j == 1 :
                count +=1
                break
        return count

    def longestPalindrome3(self, s: str) -> int:
        res = 0

        for each in set(s):
            res += (s.count(each)//2)*2

        if res <len(s):
            return res+1
        else:
            return res