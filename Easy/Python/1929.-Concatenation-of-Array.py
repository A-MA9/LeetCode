class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums);a=[0]*(2*n)
        for i in range(2*n):
            if i<n:
                a[i]=nums[i]
            else:
                a[i]=nums[i-n]
        return a