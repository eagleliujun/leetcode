"""
Given an integer, write an algorithm to convert it to hexadecimal.
For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s.
If the number is zero, it is represented by a single zero character '0';
otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

"""
class Solution:
    def toHex1(self, num: int) -> str:
        if num == 0:
            return '0'
        dic = {'10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}
        result = []
        max_int = 0xffffffff + 0x00000001
        if num < 0:
            num += max_int
        while num != 0:
            num, temp = divmod(num, 16)
            result.append(str(temp))
        result.reverse()
        for index, value in enumerate(result):
            if value in dic:
                result[index] = dic[value]
        return ''.join(result)

    def toHex2(self, num: int) -> str:
        if num == 0:
            return '0'
        dic = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
        result = []
        max_int = 0xffffffff + 0x00000001
        if num < 0:
            num += max_int
        while num != 0:
            num, temp = divmod(num, 16)
            temp = str(temp)
            if temp in dic:
                temp = dic[temp]
            result.append(temp)
        result.reverse()
        return ''.join(result)



test = Solution()
num = -151
print(test.toHex1(num))
print(test.toHex2(num))