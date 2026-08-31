class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L, R = 0, n - 1
        while L < R:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[R]:
                R = M
        if target >= nums[L] and target <= nums[n - 1]:
            return self.binarySearch(nums, target, L, n - 1)
        else:
            return self.binarySearch(nums, target, 0, L - 1)

    def binarySearch(self, arr: List[int], target: int, L: int, R: int) -> int:
        while L <= R:
            M = (L + R) // 2
            if arr[M] == target:
                return M
            elif arr[M] > target:
                R = M - 1
            else:
                L = M + 1
        return -1