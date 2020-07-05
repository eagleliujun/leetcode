"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""

class Solution:
    def peakIndexInMountainArray1(self, A):
        loc = 0
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                loc = i
        return loc

    def peakIndexInMountainArray2(self, A):
        start, mid, end = 0, len(A)//2, len(A)
        while start != end:
            if A[mid] >A[mid+1]:
                end = mid
            else:
                start = mid+1
            mid = (end + start) // 2
        return mid

    def peakIndexInMountainArray3(self, A):
        i = 0
        while A[i]<A[i+1] or i+1 == len(A):
            i +=1
        return i




a = [0, 2, 1, 0]
test=Solution()
print(test.peakIndexInMountainArray1(a))
print(test.peakIndexInMountainArray2(a))