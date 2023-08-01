class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        runningSum=[]
        for i in range(n):
            runningSum.append(sum(nums[:i+1]))
        return runningSum
# OR
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        c=0
        for i in nums:
            runningSum.append(c+i)
            c+=i
        return runningSum
            