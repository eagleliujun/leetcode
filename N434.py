"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

"""

class Solution:
    def countSegments1(self, s: str) -> int:
        s_list = s.split(' ')
        count =0
        for i in s_list:
            if i != '':
                count +=1
        return count

    def countSegments2(self, s: str) -> int:
        mark = 0
        count = 0
        for i in s:
            if i != ' ' and mark == 0:
                mark = 1
                count += 1
            elif i == ' ' and mark == 1:
                mark =0
        return count if s != ' ' else 0

    def countSegments3(self, s: str):
        s_list = s.split(' ')
        count =0
        # s1=[]
        # print(count+1 for i in s_list if i != '')
        sum((1 for i in s_list if i!= '' ))

        return count


s = "Hello, my name is John"
s2 = '      '
s3 ="Of all the gin joints in all the towns in all the world,   "
test = Solution()
print(test.countSegments1(s3))
print(test.countSegments3(s3))
