class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==1:
            return "a"*n
        else:
            x="a"*(n-1)+"b"
            return x