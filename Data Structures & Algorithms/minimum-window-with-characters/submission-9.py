class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        lenNeed = len(need)
            
        window = {}
        minLen = float("inf")
        minStr = ""
        currStr = ""
        satisfied = 0
        L = 0
        for R, c in enumerate(s):
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1

            if c in need and window[c] == need[c]:
                    satisfied += 1

            while satisfied == lenNeed:
                if R - L + 1 < minLen:
                    minStr = s[L: R + 1]
                    minLen = len(minStr)
                if s[L] in need and window[s[L]] == need[s[L]]:
                    satisfied -= 1
                window[s[L]] -= 1
                L += 1
        return minStr