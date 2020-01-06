"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""
def lengthOfLastWord(s):
    return len((s.rstrip(' ')).rpartition(' ')[-1])

def lengthOfLastWord2(s):
    s1 = filter(list(s), ' ')
    s2 = find
    return





s = 'hello world '
print(lengthOfLastWord(s))
