class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
            if each in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()
                if each == "+":
                    result = left + right
                elif each == "-":
                    result = left - right
                elif each == "*":
                    result = left * right
                elif each == "/":
                    result = int(left / right)
                stack.append(result)
            else:
                stack.append(int(each))
        return stack[-1]