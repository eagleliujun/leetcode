"""
Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr1(haystack, needle):
    nee_lens = len(needle)
    if nee_lens == 0:
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+nee_lens] == needle:
            return i
    return -1

# def strStr2(haystack, needle):


ha = "hello"
needle = "ll"

print(strStr1(ha,needle))