class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        freq = {}
        for s in s1:
            if s not in freq:
                freq[s] = 1
            else:
                freq[s] += 1
        L = 0
        freq2 = {}
        for R, s in enumerate(s2):
            if s in freq:
                if s not in freq2:
                    freq2[s] = 1
                else:
                    freq2[s] += 1
            if R - L + 1 == n:
                if freq2 == freq:
                    return True
                if s2[L] in freq2:
                    freq2[s2[L]] -= 1
                L += 1
        return False