class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        L = max(len(word) for word in words)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(max(0, i - L), i):
                if dp[j] and s[j:i] in words:
                    dp[i] = dp[j]
        
        return dp[-1]