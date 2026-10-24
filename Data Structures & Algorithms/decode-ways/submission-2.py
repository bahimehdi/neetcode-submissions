# dp[i] means: number of valid ways we can decode s[:i+1]
# base cases: dp[0], dp[1]
# how state is calculated: ..
# the answer: dp[-1]
# a decode function would take the element to decode
# we would also feed it the element to decode and the number after it

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        def decode(x):
            return x[0] != '0' and 1 <= int(x) <= 26
        
        n = len(s)
        dp = [0] * n
        s = dict(enumerate(char for char in s))
        dp[0] = 1
        if decode(s[1]):
            dp[1] = dp[0]
        if decode(s[0] + s[1]):
            dp[1] += 1
        

        for i in range(2, n):
            if decode(s[i]):
                dp[i] = dp[i-1]
            if decode(s[i-1] + s[i]):
                dp[i] += dp[i-2]

        return dp[-1]