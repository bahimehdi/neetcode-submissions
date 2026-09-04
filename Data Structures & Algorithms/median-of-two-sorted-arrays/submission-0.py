# - Input:
# two int arrays, sorted in asc
# nums1 of size n
# nums2 of size m
# - Output:
# median value among all element of the two arrays
# if len(n + m) % 2 == 0: it's the sum of the two middle elements / 2
# else: it's the middle element
# - Brute Force:
# It'd be O(n+mlogn+m), nums = sorted(nums1.extend(nums2))
# then if len(n + m) % 2 == 0: return (nums[n+m]) + nums[n+m-1]) / 2
# else: return nums[n+m]
# - Binary Search:
# We cannot construct the sorted array
# Left = first x elements of nums1 + first y elements of nums2
# with x + y = K (max elements we could have to the left before we reach the median)
# we need the subsets nums1: [..A] [B..] and nums2: [..C] [D..], representing last element picked and first element not picked, respectivally, from nums1 and nums2
# we can derive: A <= C and B <= D

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        mn = n + m
        K = (mn + 1) // 2

        # L and R are minimum/maximum legal counts for x
        L = max(0, K - m)
        R = min(K, n)

        while L <= R:
            x = (L + R) // 2
            y = K - x
            
            if x == 0:
                A = float("-inf")
            else:
                A = nums1[x - 1]

            if x == n:
                B = float("inf")
            else:
                B = nums1[x]

            if y == 0:
                C = float("-inf")
            else:
                C = nums2[y - 1]

            if y == m:
                D = float("inf")
            else:
                D = nums2[y]
            
            if A > D:
                R = x - 1
            elif C > B:
                L = x + 1
            else:
                break
        if mn % 2 == 1:
            return max(A, C)
        else:
            return (max(A, C) + min(B, D)) / 2