# array of integers
# return max of `min(x[i], x[j]) * 2`

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            currentArea = (r - l) * min(heights[r], heights[l])
            if currentArea > area:
                area = currentArea
            if heights[l] > heights[r] :
                r -= 1
            else:
                l += 1
        return area