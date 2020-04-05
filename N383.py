"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""

import re
class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool: # str
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i,'?',1)
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool: # list
        ran_list , mag_list = list(ransomNote),list(magazine)
        for i in ran_list:
            if i not in mag_list:
                return False
            mag_list.remove(i)
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:  # dic
        mag_dic = {}
        for i in magazine:
            mag_dic.update({i:mag_dic.setdefault(i,0)+1})
        for j in ransomNote:
            if j not in mag_dic.keys() or mag_dic[j] == 0:
                return False
            else:
                mag_dic[j] -= 1
        return True
    def canConstruct4(self, ransomNote: str, magazine: str) -> bool:  # str
        for each in ransomNote:
            if each not in magazine:
                return False
            elif ransomNote.count(each) > magazine.count(each):
                return False
        return True

    def canConstruct5(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteSet = set(ransomNote)
        for char in ransomNoteSet:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True


r = 'aa'
m = 'aab'
test = Solution()
print(test.canConstruct5(r,m))
