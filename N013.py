"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"         Output: 3
Example 2:
Input: "IV"          Output: 4
Example 3:
Input: "IX"          Output: 9
Example 4:
Input: "LVIII"       Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:
Input: "MCMXCIV"     Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


def romanToInt1(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_dict2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    res = 0
    skip = 0
    for i in range(1, len(s)):
        if roman_dict[s[i-1]] < roman_dict[s[i]]:
            res = res + int(roman_dict2[s[i-1] + s[i]])
            skip = 1
        elif skip == 1:
            skip = 0
            continue
        else:
            res = res + int(roman_dict[s[i-1]])
            skip = 0
    # res = res + int(roman_dict[s[i - 1]])
    if skip == 0:
        res = res + int(roman_dict[s[-1]])
    return res


def romanToInt2(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_dict2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    roman_dict3 = {'A'}
    res = 0
    skip = 0
    first =s[0]
    s_list = list(s[1:])
    for key2, value2 in roman_dict2.items():
        if s.find(key2) != -1:
            s= s.split(key2)
            res = res + int(value2)
    for key1, value1 in roman_dict.items():
        if s.find(key1) != -1:
            mux = s.count(key1)
            s =s.split(key1)
            res = res + int(value1)*mux
    return res



s1 = 'MCMXCIV'
s2 = 'III'
s3 = 'LVIII'

print(romanToInt2(s1))
