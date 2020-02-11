"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""


def missingNumber1(nums):  # overtime
    k = len(nums)
    for i in range(0, k):
        if i not in nums:
            return i
    return k

def missingNumber2(nums):
    k = set([i for i in range(len(nums)+1)])
    return (k-set(nums)).pop()

def missingNumber3(nums):
    # return sum([x for x in range(len(nums)+1)])-sum(nums)
    return len(nums) * (1 + len(nums)) // 2 - sum(nums)

def missingNumber4(nums):
    sum_l = len(nums)
    for i in range(sum_l):
        sum_l = sum_l - nums[i] + i
    return sum_l


l1 = [9,6,4,2,3,5,7,0,1]
l2 = [0]
print(missingNumber4(l1))