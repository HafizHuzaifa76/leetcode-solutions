class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        
        stack = []
        for char in s:
            if len(stack) > 0 :
                if char in par:
                    stack.append(char)
                else:
                    last = stack[-1]
                    if char == par[last]:
                        stack.pop()
                    else:
                        return False
            else:
                if char in par:
                    stack.append(char)
                else:
                    return False
        
        return not stack