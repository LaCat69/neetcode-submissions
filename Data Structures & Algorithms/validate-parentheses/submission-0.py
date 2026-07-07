class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if not stack or char not in pairs:
                stack.append(char)
            else:
                if stack.pop() != pairs[char]:
                    return False
        
        return not stack 