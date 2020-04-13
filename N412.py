"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number
and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz1(self, n: int):
        result = []
        for i in range(1,n+1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 5 == 0 :
                result.append("Buzz")
            elif i % 3 == 0 :
                result.append("Fizz")
            else:
                result.append((str(i)))
        return result

    def fizzBuzz2(self, n: int):
        result = []
        for i in range(1,n+1):
            if i % 3:
                if i % 5:
                    result.append((str(i)))
                else:
                    result.append("Buzz")
            else:
                if i % 5:
                    result.append("Fizz")
                else:
                    result.append("FizzBuzz")
        return result

    def fizzBuzz3(self, n: int):
        result = [x+1 for x in range(n)]
        for index, i in enumerate(result) :
            if i % 5:
                if i % 3:
                    result[index]=str(i)
                else:
                    result[index] = "Fizz"
            else:
                if i % 3:
                    result[index] = "Buzz"
                else:
                    result[index] = "FizzBuzz"
        return result


test = Solution()
print(test.fizzBuzz1(15))
print(test.fizzBuzz2(15))
print(test.fizzBuzz3(15))
