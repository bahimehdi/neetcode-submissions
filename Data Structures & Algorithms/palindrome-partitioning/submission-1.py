# Base case -> sum(len(partition)) == len(s)
# Choices -> add substring to 
# Constraints -> .
# Backtracking step -> if current substring isPlandrome(substring) is True and it doesn't exist in res, we add it to current res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(start, end):
            if start == len(s):
                res.append(partition[:])
                return

            if end == len(s):
                return
            
            if isPalindrome(s[start: end + 1]):
                partition.append(s[start: end + 1])
                backtrack(end + 1, end + 1)
                partition.pop()
            backtrack(start, end + 1)
                

        def isPalindrome(string):
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        backtrack(0, 0)
        return res