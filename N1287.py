"""
Given an integer array sorted in non-decreasing order,
there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6


Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
def findSpecialInteger(x):
    list_lens = int(len(x) / 4 +1)
    sum = 0
    i =1
    while i < len(x):
        if x.count(x[i]) > list_lens:
            return x[i]
        else:
            i *= 4


arr = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr))
print('fkjaslfkjlaf')