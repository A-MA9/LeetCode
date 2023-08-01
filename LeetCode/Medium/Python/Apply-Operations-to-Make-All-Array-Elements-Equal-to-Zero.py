class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k==1:
            return 1==1
        c=0;n=len(nums)
        for i in range(k):
            nums[i]-=c
            c+=nums[i]
        for i in range(k,n):
            c-=nums[i-k]
            nums[i]-=c
            c+=nums[i]
        print(nums)
        if nums[n-1]!=0:
            return 1==0
        nums.sort()
        if nums[0]<0:
            return 1==0
        return 1==1