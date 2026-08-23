class Solution:
    def trap(self, height: List[int]) -> int:
        trap, l, r = 0, 1, len(height) - 2
        leftMax, rightMax = height[0], height[-1]
        while l <= r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax <= rightMax:
                trap += leftMax - height[l]
                l += 1
            else:
                trap += rightMax - height[r]
                r -= 1
        return trap