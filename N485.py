"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""

class Solution:
    def findMaxConsecutiveOnes1(self, nums) -> int:
        sum1 = 0
        result = 0
        for i in nums:
            if i == 1:
                sum1 += 1
            else:
                sum1 =0
            if result < sum1:
                result = sum1
        return result

    def findMaxConsecutiveOnes2(self, nums) -> int:
        sum1 = 0
        result = 0
        for i in nums:
            if i == 1:
                sum1 += 1
                if result < sum1:
                    result = sum1
            else:
                sum1 =0

        return result

    def findMaxConsecutiveOnes3(self, nums) -> int:
        lista = ''.join(map(str,nums)).split('0')
        result = 0
        for i in lista:
            result = max(len(i),result)
        return result

    def findMaxConsecutiveOnes4(self, nums) -> int:
        for index,value in enumerate(nums):
            if value == 1 and index != 0:
                 nums[index] = nums[index-1]+1
        return max(nums)



x =[1,1,0,1,1,1]
test = Solution()
print(test.findMaxConsecutiveOnes1(x))
print(test.findMaxConsecutiveOnes2(x))
print(test.findMaxConsecutiveOnes3(x))
print(test.findMaxConsecutiveOnes4(x))
