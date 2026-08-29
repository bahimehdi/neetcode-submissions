class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        nextGreater = {}
        i = j = 0
        while i < len(nums2):
            while stack and stack[-1] < nums2[i]:
                popped = stack.pop()
                nextGreater[popped] = nums2[i]
            stack.append(nums2[i])
            i += 1
        for i in nums1:
            if i in nextGreater:
                result.append(nextGreater[i])
            else:
                result.append(-1)

        return result