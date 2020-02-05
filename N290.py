"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

"""
def wordPattern1(pattern, str1):
    str_list = str1.split(' ')      # dog dog
    pattern_list = list(pattern)    # a  b
    if len(str_list) != len(pattern_list):
        return False
    comp_dict = {}           # {a: dog, b: egg}
    for i, value in enumerate(pattern_list):     # a b
        if value in comp_dict:
            if comp_dict[value] != str_list[i]:
                return False
        elif str_list[i] in comp_dict.values():
            return False
        else:
            comp_dict[value] = str_list[i]
    return True

def wordPattern2(pattern, str1):
    pattern_list = [*map(pattern.index, pattern)]   # a ,b [0,1]
    str_list = str1.split(' ')                      # dog egg
    str_list2 = [*map(str_list.index, str_list)]
    return pattern_list == str_list2

def wordPattern3(pattern, str1):   # graph and deque







pattern1 = "abba"
str1 = "dog cat cat dog"
pattern2 = "abba"
str2 = "dog dog dog dog"
print(wordPattern1(pattern2,str2))
print(wordPattern2(pattern2,str2))


print(wordPattern1(pattern1,str1))
print(wordPattern2(pattern1,str1))