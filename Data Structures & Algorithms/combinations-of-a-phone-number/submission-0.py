# example walkthrough: 34
# -> 3 is d or e or f, 4 is g or h or i
# meaning we need to return all possible combinations onto res
# Base case -> len(letters) == len(digits)
# Choices -> we choose next char in digit i until exhausted, .. len(digits)-1
# Constraints -> .
# Backtracking step -> .

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        dtl = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def backtrack(currStr, currIndex):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            if currIndex == len(digits):
                return
            
            for i in range(len(dtl[digits[currIndex]])):
                backtrack(currStr + dtl[digits[currIndex]][i], currIndex + 1)
            

        backtrack("", 0)
        return res