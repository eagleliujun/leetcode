"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""

class Solution:
    def firstUniqChar1(self, s: str) -> int:   # str
        if s == '':
            return -1
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return -1

    def firstUniqChar2(self, s: str) -> int:  # str
        if s == '':
            return -1
        for index,element in enumerate(s):
            if s.count(element)==1:
                return index
        return -1

    def firstUniqChar3(self, s: str) -> int:  # list
        s_list = list(s)
        s_dic = {}
        for i in s_list:
            if i in s_dic.keys():   # s_dic[i] = s_dic.get(i, 0 ) + 1
                s_dic[i] += 1
            else:
                s_dic[i] = 1
        for key, item in s_dic.items():
            if item == 1:
                return s.index(key)
        return -1

    def firstUniqChar4(self, s: str) -> int:  # list   overtime
        if s == '':
            return -1
        if len(s) == 1:
            return 0
        for index, element in enumerate(s):
            if len(s.split(element)) == 2:
                return index
        return -1






test = Solution()
s = 'leetcode'
s2 = "loveleetcode"
print(test.firstUniqChar3(s))
print(test.firstUniqChar4(s))
print(test.firstUniqChar5(s2))