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
    if len(x) == 1:
        return 1
    list_lens = int(len(x) / 4 + 1)
    i = 1
    while i < len(x):
        if x.count(x[i]) < list_lens:
            i += list_lens
        else:
            return x[i]

arr1 = [1,2,3,3]
arr = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr1))
print('fkjaslfkjlaf')