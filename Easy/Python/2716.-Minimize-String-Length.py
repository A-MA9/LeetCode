class Solution:
    def minimizedStringLength(self, s: str) -> int:
        l=len(set(list(s)))
        return l