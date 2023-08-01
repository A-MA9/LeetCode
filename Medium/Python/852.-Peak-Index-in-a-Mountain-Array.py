class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        c=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                if arr[i-1]==max(arr[:i]) and arr[i+1]==max(arr[i+1:]):
                    return i