class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = R = longest = 0
        count = {}
        for i in s:
            if i not in count:
                count[s[R]] = 1
            else:
                count[s[R]] += 1
            R += 1
            while count[i] > 1:
                count[s[L]] -= 1
                L += 1
            longest = max(longest, R - L)
        return longest