class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()
        brackets = list(s)
        open_brackets = { "[" : "]" , "(" : ")" , "{" : "}"}
        close_brackets = {"]", ")", "}"}

        if brackets[0] not in open_brackets or len(s) ==1:
            return False

        for i in range(len(brackets)):
            print("we got here")

            if brackets[i] in open_brackets:
                stack.append(brackets[i])
            else:
                if not stack:
                    return False
                if open_brackets[stack[-1]] == brackets[i]:
                    stack.pop()
                else:
                    return False

            
        return True if not stack else False 

            