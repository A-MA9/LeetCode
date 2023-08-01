class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex=heights.copy();s=0
        ex.sort()
        for i in range(len(ex)):
            if ex[i]!=heights[i]:
                s+=1
        return s