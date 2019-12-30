#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Leetcode.num = 1002. Find Common Characters
"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
 
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

def Find_Common_Characters1(A):
    A_set, res = [], []
    '''先求出A0和A1的交集，这个为最大集，也是模板'''
    A1_list = list(A[1])
    for i in range(len(A[0])):
        if (A[0][i] in A1_list):
            A_set.append(A[0][i])
            A1_list.remove(A[0][i])
    '''遍历后续列表，剔除模板中不在后续列表中的元素'''
    for each in A[2:]:
        each_list = list(each)
        res = A_set.copy()
        for i in range(0, len(res)):
            if res[i] not in each_list:
                A_set.remove(res[i])
            else:
                each_list.remove(res[i])
    return A_set


"""
'''#2： 利用Counter方法统计元素出现次数，并输出元素与其出现次数的字典，字典相交（&操作），获取到元素的最小出现次数'''
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(A[0])
        for i in range(1, len(A)):
            res &= Counter(A[i])
        return list(res.elements())
"""

'''#3 大体思路同#2，但没有使用collections库'''
def Find_Common_Characters3(A):
    ans = {}
    #将第一个字符串中所有元素及其出现的次数做成字典，作为模板存入ans中
    for each in A[0]:
        ans[each] = A[0].count(each)
    for each in A[1:]:
        ans_temp = {}
        for i in each:  #遍历字符串，并将每个字符串中的元素和出现次数做成字典，存入ans_temp
            ans_temp[i] = each.count(i)
        for j in list(ans.keys()):  #遍历模板ans字典
            if (j not in ans_temp): #对于在后面没有出现的元素进行删除
                del ans[j]
            else:   #对于在后面出现的元素，比较其出现次数的大小，将最小的value更新到模板ans字典中
                if (ans.get(j) > ans_temp.get(j)):
                    ans[j] = ans_temp.get(j)
    res = []
    for each in list(ans.keys()): #将ans中的元素按照其value值的数量还原至返回列表res中
        while (ans[each] != 0):
            res.append(each)
            ans[each] -= 1
    return res
"""
#大神的代码，思路一样，但及其简练，收藏学习！
"""
def Find_Common_Characters4(A):
    if not A:
        return []

    res = []
    for each in set(A[0]):
        count = [w.count(each) for w in A]
        s = each * min(count)
        print("s", s)
        for i in s:
            res.append(i)

    return res

A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
A1 = ["bella","label","roller"]
A2 = ["cool","lock","cook"]
print(Find_Common_Characters4(A2))