"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


"""

def titleToNumber1(s):
    s_list = list(s)
    lens = len(s_list)
    res = 0
    for i in s_list:
        asc = ord(i)
        lens -= 1
        res += (asc-64)*pow(26, lens)
    return res


def titleToNumber2(s):
    lens = len(s)
    res = 0
    for i in s:
        asc = ord(i)
        lens -= 1
        res += (asc-64)*pow(26, lens)
    return res



s = 'BA'
print(titleToNumber1(s))