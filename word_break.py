class Solution:
    def wordBreakDP(self, s, wordDict, wordMap):
        if len(s) == 0 or (s in wordMap and not wordMap[s]): return False
        if s in wordDict or wordMap.get(s, False): return True
        if len(s) == 1: return False

        for i in range(1, len(s)):
            toi = self.wordBreakDP(s[:i], wordDict, wordMap)
            fromi = self.wordBreakDP(s[i:], wordDict, wordMap)
            wordMap[s[:i]] = toi
            wordMap[s[i:]] = fromi
            if toi and fromi: return True

        wordMap[s] = False
        return False

    def wordBreak(self, s: str, wordDict) -> bool:
        return self.wordBreakDP(s, wordDict, {})

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0: return True
        wordMap = [False] * (len(s)+1)

        for i in range(1, len(s)+1):
            if not wordMap[i] and s[:i] in wordDict:
                wordMap[i] = True

            if wordMap[i]:

                if i == len(s): return True

                for j in range(i+1, len(s)+1):
                    if not wordMap[j] and s[i:j] in wordDict:
                        wordMap[j] = True

                    if j == len(s) and wordMap[j]: return True

        return False
