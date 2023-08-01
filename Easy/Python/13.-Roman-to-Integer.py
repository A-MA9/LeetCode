class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l=len(s)
        r=0
        i=0
        while i<l-1:
            if d[s[i+1]]<=d[s[i]]:
                r+=d[s[i]]
                i+=1
            else:
                r+=d[s[i+1]]-d[s[i]]
                i+=2
        if i==l-1:
            r+=d[s[i]]
        return r