"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans, carry = 0, 0
        result =''
        n1, n2 = num1[::-1], num2[::-1]
        if len(num1) < len(num2):     # n1 long
            n1, n2 = n2, n1
        for i in range(len(n2), len(n1)):
            n2 += '0'
        for j in range(len(n1)):
            ans = int(n1[j]) + int(n2[j]) + carry
            carry = ans // 10
            result += str(ans%10)
        if carry:
            result += '1'
        return result[::-1]

    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(map(int, num1[::-1])), list(map(int, num2[::-1]))
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        for i in range(len(num1)):
            if i < len(num2):
                n = num2[i]
            else:
                n = 0
            tmp = n + carry + num1[i]
            num1[i] = tmp % 10
            carry = tmp // 10
        if carry:
            num1.append(1)
        return ''.join(map(str, num1))[::-1]

test= Solution()
n1='9'
n2 ='99'
print(test.addStrings(n1,n2))

