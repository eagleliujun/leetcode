"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
import re

class Solution:
    def reverseVowels1(self, s: str) -> str:
        vowels = {'a', 'i', 'e', 'o', 'u','A', 'I', 'E', 'O', 'U'}
        vowel_list = []
        for element in s:
            if element in vowels:
                vowel_list.append(element)
        # vowel_str = str(vowel_list)
        # vowel_list.reverse()
        # vowel_revstr = str(vowel_list)
        # vowel_map = str.maketrans(vowel_str, vowel_revstr)
        # s_result = s.translate(vowel_map)
        vowel_revlist = vowel_list.copy()
        vowel_revlist.reverse()
        s_list = list(s)
        i=0
        for index, element in enumerate(s_list):
            if element in vowels:
                s_list[index]=vowel_revlist[i]
                i += 1
        s_result = ''.join(s_list)
        return s_result

    def reverseVowels2(self, s: str) -> str:
        vowels = {'a', 'i', 'e', 'o', 'u','A', 'I', 'E', 'O', 'U'}
        vowel_list = []
        vowel_index =[]
        for index, element in enumerate(s):
            if element in vowels:
                vowel_list.append(element)
                vowel_index.append(index)
        s_list = list(s)
        j = len(vowel_list)
        for index, element in enumerate(s_list):
            if element in vowels:
                s_list[index] = vowel_list[j-1]
                j -= 1
        s_result = ''.join(s_list)
        return s_result

    def reverseVowels3(self, s: str) -> str:
        vowels = {'a', 'i', 'e', 'o', 'u','A', 'I', 'E', 'O', 'U'}
        vowel_list = []
        vowel_index =[]
        for index, element in enumerate(s):
            if element in vowels:
                vowel_list.append(element)
                vowel_index.append(index)
        s_list = list(s)
        vowel_list.reverse()
        j=0
        for index, element in enumerate(s_list):
            if element in vowels:
                s_list[index] = vowel_list[j]
                j += 1
        s_result = ''.join(s_list)
        return s_result

    def reverseVowels4(self, s: str) -> str:
        vowel = '[aieouAIEOU]'
        com = re.compile(vowel)
        t = com.findall(s)
        t.reverse()
        k = re.sub(vowel, '9', s)
        # t2=com.finditer(s)
        for i in t:
            k = re.sub('9', i, k, 1)
            print(k)
        return k

s = "leetcodeaae"
s2 = "A mEn, I plOn, U canel: Pinomu"
test = Solution()
print(test.reverseVowels1(s))
print(test.reverseVowels2(s))
print(test.reverseVowels3(s))
print(test.reverseVowels4(s2))
print(s2)
