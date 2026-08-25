# tokens = array of strings
# return int = the evaluation of the expression
# rules:
# operands = integers or results of other operations
# operators = +, -, *, /
# division between integers always truncates toward zero

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(self.calculator(operand1, operand2, i))
        return stack[-1]

    def calculator(self, a, b, op):
        match op:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return int(a / b)