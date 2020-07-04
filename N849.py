"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
 

Constraints:

2 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""

class Solution:
    def maxDistToClosest(self, seats):
        seat = 0
        last_length = 0
        left = 0 if seats[0] == 0 else 1
        right = 0 if seats[-1] == 0 else 1
        for i in seats:
            if i == 0:
                seat += 1
            elif left == 0:
                last_length = seat * 2
                left = 1
                seat = 0
            else:
                if last_length < seat:
                    last_length = seat
                seat = 0
        if right ==0:
            last_length = max(last_length, seat *2)
        return (last_length+1) // 2

    def maxDistToClosest2(self, seats):
        left0 = seats[0]
        left = right = res = 0
        for right in range(len(seats)):
            if seats[right] == 1:
                if left0 == 0:
                    res = (right - left) *2
                    left0 = 1
                elif (right-left-1) > res:
                    res = right-left-1
                left = right
        if seats[-1] == 0:
            res = max(res, (right - left) * 2)
        return (res+1)//2

a1 = [1,0,0,0,1,0,1]
a2 = [1,0,0,1]
a3 = [0,0,1,0,1,1]
a4=[0,0,0,0,0,0,1,0,0,0,0]
test =Solution()
print(test.maxDistToClosest(a1))
print(test.maxDistToClosest(a2))
print(test.maxDistToClosest(a4))
print(test.maxDistToClosest2(a1))
print(test.maxDistToClosest2(a2))
print(test.maxDistToClosest2(a4))