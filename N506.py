"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

"""

class Solution:
    def findRelativeRanks(self, nums: list[int]) -> list[str]:
        for i in range(len(nums)-3):
            result[i] = '0'
        result["Gold Medal"]
        result = {0 for i in range(len(nums))]
        j =0
        result[0] = 'Gold Medal'
        for index,data in enumerate(nums):
            while j != index:
                if data > index[j]:
