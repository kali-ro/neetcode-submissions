class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for item in tokens:
            if item == "+" or item == "-" or item == "/" or item == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                res = 0
                if item == "+":
                    res = num1 + num2
                elif item == "-":
                    res = num2 - num1
                elif item == "/":
                    res = int(num2 / num1)
                elif item == "*":
                    res = num1 * num2
                stack.append(res)
            else:
                stack.append(int(item))
        return stack[0]