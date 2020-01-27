
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
You can do so recursively, in other words from the previous member read off the digits,
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.


Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1",
"2" can be read as "12" which means frequency = 1 and value = 2,
the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
"""


def countAndSay1(n):
    if n == 1:
        return '1'
    i = 2
    result2 = '1'
    result1 = []
    while i <= n:
        len1 = len(result2)
        app2 = result2[0]
        result2 = result2.lstrip(result2[0])
        app1 = str(len1 - len(result2))
        result1.extend([app1, app2])
        if len(result2) == 0:
            i += 1
            result2 = ''.join(result1)
            result1 = []
    return result2


def countAndSay2(n):
    if n == 1:
        return '1'
    else:
        result2 = countAndSay2(n-1)
        result1 = []
        while result2:
            len1 = len(result2)
            app2 = result2[0]
            result2 = result2.lstrip(result2[0])
            app1 = str(len1 - len(result2))
            result1.extend([app1, app2])
            if len(result2) == 0:
                return ''.join(result1)


def countAndSay3(n):   # optimize the code for item2
    if n == 1:
        return '1'
    else:
        result2 = countAndSay2(n-1)
        result1 = []
        while result2:
            len1 = len(result2)
            app2 = result2[0]
            result2 = result2.lstrip(result2[0])
            app1 = str(len1 - len(result2))
            result1.extend([app1, app2])
    return ''.join(result1)


print(countAndSay1(5))
print(countAndSay2(5))
print(countAndSay3(5))
