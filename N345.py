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
        vowel = '[aieouAIEOU]'   # 任意一个符合就Ok
        com = re.compile(vowel)    #创建规则
        t = com.findall(s)        # 找到所有符合规则的字符
        t.reverse()               # 反转找到的结果
        k = re.sub(vowel, '9', s)  # 替代原始字符串中的元音字符
        # t2=com.finditer(s)
        for i in t:
            k = re.sub('9', i, k, 1)  #利用反转的结果，每次替代一个原始字符串中已经被替换的字符
            print(k)                  # 存在问题： '9'这个字符，被错误替换了
        return k

s = "leetcodeaae"
s2 = "A mEn, I plOn, U canel: Pinomu"
test = Solution()
print(test.reverseVowels1(s))
print(test.reverseVowels2(s))
print(test.reverseVowels3(s))
print(test.reverseVowels4(s2))
print(s2)
