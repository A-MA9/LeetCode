class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        n.sort()
        a=len(nums1);b=len(nums2)
        c=a+b
        if c%2==1:
            return n[(a+b)//2]
        else:
            return (n[(a+b)//2]+n[((a+b)//2)-1])/2