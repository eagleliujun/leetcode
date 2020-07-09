"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

Example 1:
Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

Example 2:
Input: 5
Output: 2
Explanation:
5 in binary is 0b101.

Example 3:
Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

"""

class Solution:
    def binaryGap1(self, N):
        res,temp = 0,0
        mark = 0
        while N:
            if N%2:
                if mark == 0:
                    mark, temp = 1, 0
                else:
                    res = max(res,temp + 1)
                    temp = 0
            elif mark ==1:
                temp+=1
            N //=2
        return res

    def binaryGap2(self, N):
        if N == 1:
            return 0
        Nbin=bin(N)[2:]
        if Nbin[0] == '0':
            Nbin =Nbin.partition('1')[2]
        if Nbin[-1] == '0':
            Nbin = Nbin.rpartition('1')[0]
        if Nbin == '':
            return 0
        return max(list(map(len,Nbin.split('1'))))+1


n=1
test = Solution()
print(test.binaryGap1(n))
print(test.binaryGap2(n))