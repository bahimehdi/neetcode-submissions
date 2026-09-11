class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {} # count of chars
        L = maxFrequency = target = 0
        for R, i in enumerate(s):
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
            maxFrequency = max(maxFrequency, freq[i])
            while (R - L + 1) - maxFrequency > k:
                freq[s[L]] -= 1
                L += 1
            target = max(target, R - L + 1)
        return target