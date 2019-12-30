# Leetcode.num = 35. Search Insert Position
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
"""


def search_insert1(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return i + 1


def search_insert2(nums, target):
    return nums.index(target) if target in nums else search_insert2_sub(nums, target)


def search_insert2_sub(nums, target):
    for i in range(len(nums)):
        if nums[i] > target:
            return i
    return i + 1


'''
We know the array is sorted, so we can reduce the search to O(logN) via binary search. 
If not found, i>=j then we need to compare target with the nums[i], 
return i + 1 if the target is bigger (insert after) or i otherwise (insert before).
'''

import math


def search_insert3(nums, target):
    # we set start_ndx and end_ndx the starting and ending index of a string
    # remember these two indices will get changed when the iteration runs
    start_ndx, end_ndx = 0, len(nums) - 1

    # the iteration condition is end_ndx is greater than the start_ndx
    while start_ndx < end_ndx:
        # select an index in the middle
        mid = int(start_ndx + (end_ndx - start_ndx) / 2)

        # we have already found the value in the middle
        if target == nums[mid]:
            return mid

        # in the case where target is bigger than the middle value
        # in order to accelerate searching speed, end_ndx now walks for the distance of int((mid-start_ndx)/2),
        # instead of the previous constant 1, however, we should consider the cases when int((mid-start_ndx)/2) == 0
        # in this situation, endless iteration may happen

        if target > nums[mid]:
            # right_moves = math.floor((mid-start_ndx)/2)
            # start_ndx = mid + 1 if right_moves <= 1 else mid + right_moves - 1
            start_ndx = mid + 1

        # if target is smaller than or equal to the middle value
        # in order to accelerate searching speed, end_ndx now walks for the distance of int((end_ndx-mid)/2),
        # instead of the previous constant 1, however, we should consider the cases when int((end_ndx-mid)/2) == 0
        # in this situation, endless iteration may happen
        else:
            # left_moves = math.floor((end_ndx-mid)/2)
            # end_ndx = mid - 1 if left_moves <= 1 else mid - left_moves + 1
            end_ndx = mid - 1

    return start_ndx + 1 if target > nums[start_ndx] else start_ndx


def search_insert4_recur_body(nums, target, start_ndx=0, end_ndx=1):
    mid = int(start_ndx + (end_ndx - start_ndx) / 2)
    if target == nums[mid]:
        return mid
    if start_ndx >= end_ndx:
        return start_ndx + 1 if target > nums[start_ndx] else start_ndx
    else:
        mid = int(start_ndx + (end_ndx - start_ndx) / 2)
        if target > nums[mid]:
            start_ndx = mid + 1
        else:
            end_ndx = mid - 1
        return search_insert4_recur_body(nums, target, start_ndx, end_ndx)


# just a line to call the recursion body function
def search_insert4(nums, target):
    return search_insert4_recur_body(nums, target, 0, len(nums) - 1)


nums1 = [1, 3, 5, 6]
target1 = 4

# print(search_insert3(nums1, target1))

print(search_insert2(nums1, target1))
