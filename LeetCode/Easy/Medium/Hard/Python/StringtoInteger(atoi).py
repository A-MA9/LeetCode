class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]        
        n=0
        for i in s:
            if not i.isdigit():
                break
            n = n*10+int(i)
        n=sign*n
        n=max(-2**31, min(n, 2**31 - 1))
        return n