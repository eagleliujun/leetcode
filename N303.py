class NumArray:

    def __init__(self, nums):
        sub_sum = 0
        self.sumidx=[]
        self.sumidx.append(0)
        for num in nums:
            sub_sum += num
            self.sumidx.append(sub_sum)

    def sumRange(self, i: int, j: int) -> int:
        if i > j:
            return -1
        else:
            return self.sumidx[j+1]-self.sumidx[i]

class NumArray2:

    def __init__(self, nums):
        self.sumidx=[]
        self.sumidx.append(0)
        for num in nums:
            self.sumidx.append(self.sumidx[-1]+num)

    def sumRange(self, i: int, j: int) -> int:
        if i > j:
            return -1
        else:
            return self.sumidx[j+1]-self.sumidx[i]



nums = [1,2,3,4,5,6,7,8,9]

test = NumArray2(nums)
print(test.sumidx)
print(test.sumRange(3,5))