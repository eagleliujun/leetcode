"""
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:
Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""

def ugly_number1(num):  # 32ms  12.5M
    if num <= 0:
        return False
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
    if num == 1:
        return True
    else:
        return False

def ugly_number2(num):  #没有成功。
    if num <= 0:
        return False
    dec = True
    if num % 2 == 0 and dec == True:
        num /= 2
        dec = ugly_number2(num)
    if num % 3 == 0 and dec == True:
        num /= 3
        dec =ugly_number2(num)
    if num % 3 == 0 and dec == True:
        num /= 5
        dec =ugly_number2(num)
    if num != 1 and dec == False:
        return False
    else:
        return True


x = 1023
print(ugly_number2(x))
