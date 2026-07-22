from enum import StrEnum

class BracketClass(StrEnum):
    ROUND = 'round'
    SQUARE = 'square'
    CURLY = 'curly'

class Solution:
    def is_open(self, c: str) -> bool:
        return c in '({['

    def is_close(self, c: str) -> bool:
        return c in ')}]'

    def bracket_class(self, c: str) -> BracketClass:
        if c in "()":
            return BracketClass.ROUND
        if c in "[]":
            return BracketClass.SQUARE
        if c in "{}":
            return BracketClass.CURLY
    
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if self.is_open(bracket):
                stack.append(bracket)
            elif self.is_close(bracket):
                if len(stack) == 0:
                    return False  # Too many close bracket
                last = stack.pop()
                if self.bracket_class(last) != self.bracket_class(bracket):
                    return False  # False close bracket

        if len(stack) > 0:
            return False  # Not all brackets closed
        return True