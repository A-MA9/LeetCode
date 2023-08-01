class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        s=nums.count(target)
        d=nums.index(target)
        return [d,d+s-1]