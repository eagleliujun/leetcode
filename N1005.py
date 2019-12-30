"""Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
"""


def largest_sum(a, k):
    a.sort()
    for i in len(a):
        if k == 0:
            break
        elif i < 0 and k > 0 :
            a[i] *= -1
            k -= 1
        elif i == 0:
            break
        else:
            k = k % 2
            if k == 0:
                break
            elif a[i] > a[i-1]:
                a[i-1] *= -1
            else:
                a[i] *= -1
    return sum(a)



a = [2, -3, -1, 5, -4]

print(largest_sum(a, 2))
