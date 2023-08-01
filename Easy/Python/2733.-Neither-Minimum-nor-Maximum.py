class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a=set(nums)
        if len(nums)==1:
            return -1

        if len(a)==2:
            return -1
        d=list(a)
        d.sort()
        return d[1]
# OR
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        nums.sort()
        return nums[1]