"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

"""

class Solution:
    def buddyStrings(self, A: str, B: str):
        swap = 0
        tempA, tempB = '', ''
        for i in range(len(A)):
            if swap == 0 and A[i] != B[i]:
                tempA, tempB, swap =A[i], B[i], 1
            elif swap == 1 and A[i] != B[i]:
                if (tempA == A[i] and tempB != B[i]) or (tempA == B[i] and tempB != A[i]):
                    return False
        return True


A = "aaaaaaaba"
B = "aaaaaaacb"
test = Solution()
print(test.buddyStrings(A,B))