"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""
def isHappy1(n):
    if n == 1:
        return True
    total = 0
    a = list(str(n))
    a_set ={n}
    a_lens_old = 1
    while total != 1:
        total = 0
        for i in a:
            total = eval(i)*eval(i)+total
        a = list(str(total))
        a_set.add(total)
        a_lens_new = len(a_set)
        if a_lens_old == a_lens_new:
            return False
        a_lens_old += 1
    return True


def isHappy2(n):
    if n == 1:
        return True
    a_set = {n}
    a_lens_old = 1
    while True:
        a, b = divmod(n, 10)
        n = b*b
        while a != 0:
            a, b = divmod(a, 10)
            n += b*b
        a_set.add(n)
        if n == 1:
            return True
        if a_lens_old == len(a_set):
            return False
        a_lens_old += 1



def isHappy3(n):
    n_set = {n}
    def defhappy(n,set_len):
        if n == 1:
            return True
        else:
            a, b = divmod(n, 10)
            n = b * b
            while a != 0:
                a, b = divmod(a, 10)
                n += b * b
            n_set.add(n)
            return defhappy(n, set_len+1) if set_len != len(n_set) else False
    return defhappy(n, 1)


print(isHappy1(7))
print(isHappy2(7))
print(isHappy3(7))