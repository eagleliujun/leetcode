"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twosum1(nums, target):
    for index, value in enumerate(nums):
        value2 = target - value
        if value2 in nums:
            if index != nums.index(value2):
                return [index, nums.index(value2)]


def twosum2(nums, target):
    for index, value in enumerate(nums):
        try:
            index2 = nums.index(target - value, index + 1, len(nums))
            return [index, index2]
        except ValueError:
            continue


def twosum3(nums, target):
    nums_dic = {}
    for index, value in enumerate(nums):
        if nums_dic.get(value, -1) == -1:
            nums_dic[target - value] = index
        else:
            return [nums_dic[value], index]


nums = [3, 4, 5, 2]
target = 6
print(twosum3(nums, target))
