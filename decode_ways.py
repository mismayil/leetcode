class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0': return 0

        decodings = [0] * len(s)
        decodings[0] = 1

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] != '0' and s[i-1:i+1] < '27':
                    decodings[i] = 1 if i-2 < 0 else decodings[i-2]
                else:
                    decodings[i] = 0
            else:
                decodings[i] = decodings[i-1]
                if s[i-1] != '0' and s[i-1:i+1] < '27':
                    decodings[i] += 1 if i-2 < 0 else decodings[i-2]

        return decodings[len(s)-1]
