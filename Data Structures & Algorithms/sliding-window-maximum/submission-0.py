from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = curr = 0
        windowsMax = list()
        dq = deque()
        for R, i in enumerate(nums):
            curr += 1
            # monotonic deque
            while dq and nums[dq[-1]] <= i:
                dq.pop()
            dq.append(R)
            
            if curr == k:
                while dq and dq[0] < L:
                    dq.popleft()
                windowsMax.append(nums[dq[0]])
                L += 1
                curr -= 1
        return windowsMax