class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                a[nums[i]]+=1
        for j,k in a.items():
            if k==1:
                return j