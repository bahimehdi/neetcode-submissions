# Floyd's cycle detection algorithm

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # cycle detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # meeting point
                met = True
                break
        # since it's guaranteed, no need for if not met: return None
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow