class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if answerKey.count("F") <= k:
            return len(answerKey)
        n = len(answerKey)
        l= 0
        m= 0
        t= 0
        f= 0

        for r in range(n):
            if answerKey[r] == 'T':
                t += 1
            else:
                f += 1

            if (r - l + 1 - max(t,f)) > k:
                if answerKey[l] == 'T':
                    t-= 1
                else:
                    f -= 1
                l+= 1

            m = max(m, r - l + 1)

        return m

        