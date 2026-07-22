import math

class Solution:
    def is_operator(self, c: str):
        return c in "+-*/"

    def is_operand(self, c: str):
        return not self.is_operator(c)

    def value(self, c: str):
        return int(c)  # Parse integer in base ten

    def compute(self, op: str, a: int, b: int):
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                res = a / b
                res = int((1 if res > 0 else -1 if res < 0 else 0) * math.floor(abs(res)))
                return res
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Operands stack

        for i, tok in enumerate(tokens):
            print(f"stack: {stack}, tok: {tok}, remaining inputs: {tokens[i+1:]}")
            if self.is_operator(tok):
                # Pop two operands in reverse and perform operation
                b, a = self.value(stack.pop()), self.value(stack.pop())
                print(f"> pop {b}\n> pop {a}")
                y = self.compute(tok, a, b)
                print(f"> y = {a} {tok} {b}")
                stack.append(y)
                print(f"> push {y}")
            else:
                # Simply push value
                print(f"> push {tok}")
                stack.append(tok)

        print(f"Final stack: {stack}")

        return self.value(stack.pop())