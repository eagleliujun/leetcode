"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z
"""
# def longestCommonPrefix1(strs):
#     k=0
#     for i in len(strs[0]):
#         for index, value  in enumerate(strs):
#             if strs[0][i] == j[i]
#                 k = i
#             else:
#                 break

def longestCommonPrefix1(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    if len(strs[0]) == 0:
        return ""
    k = len(strs[0])
    min_index = 0
    for i in range(1, len(strs)):
        if k > len(strs[i]):
            k = len(strs[i])
            min_index = i
    for i in range(0, k):
        for j in range(0, (len(strs[1:]) + 1)):
            if strs[min_index][i] != strs[j][i]:
                k = i
                break
        if k < len(strs[min_index]):
            break
    return strs[0][:k]


def longestCommonPrefix2(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    if len(strs[0]) == 0:
        return ""
    k = 0
    result = list(zip(*(list(str2) for str2 in strs)))
    res = ''
    for i in range(len(result)):
        if len(set(result[i])) != 1:
            break
        else:
            res = res + result[i][0]
    return res


x4 = ["",""]
x1 = ["dog","racecar","car"]
x2 = ["flower","flow","flight"]
x3 = ["cc","c"]
x4 = ["c","c"]
print(longestCommonPrefix2(x2))