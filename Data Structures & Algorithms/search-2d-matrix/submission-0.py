# find row (check row[0], row[-1]), then find target

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        L = 0
        R = N - 1
        while L <= R:
            M = (L + R) // 2
            if matrix[M][0] <= target and matrix[M][-1] >= target:
                return self.binarySearch(matrix[M], target)
            elif matrix[M][-1] < target:
                L = M + 1
            elif matrix[M][0] > target:
                R = M - 1
        return False

    def binarySearch(self, arr: List[int], target: int) -> bool:
        N = len(arr)
        L = 0
        R = N - 1
        while L <= R:
            M = (L + R) // 2
            if arr[M] == target:
                return True
            elif arr[M] < target:
                L = M + 1
            else:
                R = M - 1
        return False