class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)  
            elif not stack or (char == ")" and stack.pop() != "(") or (char == "}" and stack.pop() != "{") or (char == "]" and stack.pop() != "["):
                return False
        return not stack  