# rules: return true if
# every open bracket `(,[,{` is closed by the same type of close bracket `},],)`
# open brackets are closed in the correct order
# every close bracket has a corresponding open bracket of the same type

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'{': '}', '[': ']', '(': ')'}
        for i in s:
            if not stack:
                if i in brackets.values():
                    return False
                stack.append(i)
            else:
                if i == brackets[stack[-1]]:
                    stack.pop()
                elif i in brackets.keys():
                    stack.append(i)
                else:
                    return False
        if stack:
            return False
        return True