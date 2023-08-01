class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=min(strs)
        while s!="":
            c=0
            for i in strs:
                if s in i[:len(s)]:
                    c+=1
            if c==len(strs):
                return s
                break
            else:
                s=s[:len(s)-1]
        return s