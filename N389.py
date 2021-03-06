"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""


class Solution:
    def findTheDifference1(self, s: str, t: str) -> str:  # str
        for i in t:
            if t.count(i) != s.count(i):
                return i

    def findTheDifference2(self, s: str, t: str) -> str:  # list
        s_list, t_list = list(s), list(t)
        for i in s_list:
            if i in t_list:
                t_list.remove(i)
        return t_list[0]

    def findTheDifference3(self, s: str, t: str) -> str:  # list
        s_list, t_list = list(s), list(t)
        s_list.sort()
        t_list.sort()
        for index, value in enumerate(s_list):
            if value != t_list[index]:
                return t_list[index]
        return t_list[-1]

    def findTheDifference4(self, s: str, t: str) -> str:  # set
        s_set, t_set = set(s), set(t)
        if len(s_set) != len(t_set):
            t_set.difference_update(set(s))
            return t_set.pop()
        else:
            for i in s:
                if len(s.split(i)) != len(t.split(i)):
                    return i

    def findTheDifference5(self, s: str, t: str) -> str:  # dict
        target = {}
        for i in t:
            target[i] = target.get(i, 0) + 1
        for j in s:
            target[j] = target.get(j) - 1
        for k in target:
            if target[k] != 0:
                return k


    def findTheDifference6(self, s: str, t: str) -> str:  # str
        for i in s:
            t = t.replace(i, '', 1)
        return t

    def findTheDifference7(self, s: str, t: str) -> str:  # ascii
        return chr(sum(map(ord,t))-sum(map(ord,s)))

    def findTheDifference8(self, s: str, t: str) -> str:  # asc-xor
        ans = 0
        for i in s:
            ans ^= ord(i)
        for i in t:
            ans ^= ord(i)
        return chr(ans)


s1 = "abcd"
t2 = "abcde"
s = 'ae'
t = 'aea'

test = Solution()
# print(test.findTheDifference1(s,t))
# print(test.findTheDifference2(s,t))
print(test.findTheDifference3(s, t))
print(test.findTheDifference4(s, t))
print(test.findTheDifference5(s, t))
print(test.findTheDifference6(s, t))
print(test.findTheDifference7(s, t))
print(test.findTheDifference8(s, t))