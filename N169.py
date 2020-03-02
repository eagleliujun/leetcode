"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
from functools import reduce
def majorityElement1(nums):   # normal
    summary = {}
    lens = len(nums)
    for index,value in enumerate(nums):
        summary[value]= summary.get(value,0)+1
    for key,item in summary.items():
        if item >= lens/2:
            return key
    return None

def majorityElement2(nums):   #best
    nums.sort()
    return nums[len(nums)//2]

def majorityElement3(nums):  # better
    candidate, res = nums[0], 1
    for i in nums[1:]:
        if i == candidate:
            res += 1
        else:
            res -= 1
        if res < 0:
            candidate = i
            res = 0
    return candidate

def majorityElement4(nums):  # better
    candidate, res = nums[0], 1
    for i in nums[1:]:
        res = res+1 if i == candidate else res-1
        if res < 0:
            candidate, res = i, 0
    return candidate


p1= [2,2,1,1,1,2,2]
print(majorityElement3(p1))
