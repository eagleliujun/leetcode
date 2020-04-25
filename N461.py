"""
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

class Solution:
    def hammingDistance0(self, x: int, y: int) -> int:
        a, b = list(str(bin(x))), list(str(bin(y)))
        if len(a) > len(b):
            a,b = b,a
        a.reverse()
        b.reverse()
        sum = 0
        for i in range(len(a)-2):
            if a[i] != b [i]:
                sum += 1
        for j in range(len(a)-2,len(b)-2):
            if b[j] == '1':
                sum +=1
        return  sum

    def hammingDistance1(self, x: int, y: int) -> int:
        dis = 0
        res =[]
        while x != 0 or y != 0:
            res.append((x%2, y %2))
            x, y = x//2, y //2
        for x in res:
            if x[0] != x[1]:
                dis +=1
        return dis

    def hammingDistance2(self, x: int, y: int) -> int:
        # print(x^y)
        return bin(x^y).count('1')

x =93
y =73
test =Solution()
print(test.hammingDistance0(x,y))
print(test.hammingDistance1(x,y))
print(test.hammingDistance2(x,y))

