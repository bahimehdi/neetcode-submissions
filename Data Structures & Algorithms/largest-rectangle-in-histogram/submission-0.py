# heights = array of ints (histogram)
# return maxArea = largest rectangle that can be formed among the bars
# another use of monotonic stacks
# if currentElement is lesser than the one before it, we pop the one before it
# left fixed, right

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right = left = maxArea = 0
        while left < len(heights):
            start = right
            while stack and heights[right] < stack[-1][1]:
                maxArea = max(maxArea, (right - stack[-1][0]) * stack[-1][1])
                start = stack.pop()[0]
            stack.append((start, heights[right]))
            left += 1
            right = left
        while stack:
            start, height = stack.pop()
            width = len(heights) - start
            maxArea = max(maxArea, width * height)
        return maxArea