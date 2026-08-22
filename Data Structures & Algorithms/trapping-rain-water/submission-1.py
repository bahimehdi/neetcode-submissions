class Solution:
    def trap(self, height: List[int]) -> int:
        trap, leftMax, rightMax = 0, height[0], [0] * len(height)
        for i in range(len(height) - 1, 0, -1):
            rightMax[i-1] = max(height[i], rightMax[i])
        for i in range(1, len(height) - 1):
            while leftMax > height[i] and rightMax[i] > height[i]:
                maxWater = min(leftMax, rightMax[i])
                if (maxWater > height[i]):
                    trap += maxWater - height[i]
                    break
            leftMax = max(leftMax, height[i])
        return trap