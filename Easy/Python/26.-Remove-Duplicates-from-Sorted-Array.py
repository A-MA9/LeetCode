class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        nums[:len(s)]=s
        return len(s)