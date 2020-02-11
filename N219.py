"""
Given an array of integers and an integer k, find out whether there are two distinct
indices i and j in the array such that nums[i] = nums[j] and the absolute difference
between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

def containsNearbyDuplicate1(nums, k):  #over time
    for i in range(len(nums)-1):
        for j in range(i+1, min(len(nums),i+k+1)):
            if nums[i] == nums[j]:
                return True
    return False

def containsNearbyDuplicate2(nums, k):
    if len(nums) < k:
        k = len(nums)-1
    for i in range(k, len(nums)):
        for j in range(i-k, i):
            if nums[i] == nums[j]:
                return True
    return False

nums1 = [1,0,1,1]
k1 = 1
nums2 = [1,2,3,1,2,3]
k2 = 2
nums3 = [99,99]
k3 = 2


print(containsNearbyDuplicate1(nums1, k1))
print(containsNearbyDuplicate2(nums1, k1))
print(containsNearbyDuplicate1(nums2, k2))
print(containsNearbyDuplicate2(nums2, k2))
print(containsNearbyDuplicate1(nums3, k3))
print(containsNearbyDuplicate2(nums3, k3))