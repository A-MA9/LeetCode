class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0;s=0;m=len(nums)
        for end in range(len(nums)):
            s+=nums[end]
            while s>=target:
                m=min(m,end-start+1)
                s-=nums[start]
                start+=1
        if m!=len(nums):
            return m
        else:
            if sum(nums)>=target:
                return m
            else:
                return 0