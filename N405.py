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

    def toHex3(self, num: int) -> str:
        if num < 0:
            num = 2 ** 32 + num
        s = ''

        mp = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
              13: 'd', 14: 'e', 15: 'f', 16: '10'}

        while num > 16:
            bit = num % 16
            s = mp[bit] + s
            num = num // 16

        s = mp[num] + s
        return s

    def toHex4(self, num: int) -> str:
        max_int = 0xffffffff + 0x00000001
        if num == 0:
            return '0'
        if num < 0:
            num += max_int
        s = ''
        mp = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: '10'}
        while num > 0:
            bit = num % 16
            bit_str = str(bit) if bit not in mp else mp[bit]
            # if bit in mp:
            #     bit = mp[bit]
            # else:
            #     bit = str(bit)
            s = bit_str +s
            num = num // 16
        return s



test = Solution()
num = -151
print(test.toHex1(num))
print(test.toHex2(num))
print(test.toHex3(num))
print(test.toHex4(num))