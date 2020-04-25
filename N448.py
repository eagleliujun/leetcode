"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""

class Solution:
    def findDisappearedNumbers2(self, nums):
        for i in nums:
            nums[abs(i)-1] = - abs(nums[abs(i)-1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]

    def findDisappearedNumbers1(self, nums):
        if len(nums) <= 1:
            return nums
        notIn = [0] * len(nums)
        for num in nums:
            notIn[num - 1] = 1

        for i in range(len(nums)):
            if notIn[i] == 0:
                notIn.append(i + 1)
        return notIn[len(nums):]

n = [4,3,2,7,8,2,3,1]
test = Solution()
print(test.findDisappearedNumbers2(n))
print(test.findDisappearedNumbers1(n))