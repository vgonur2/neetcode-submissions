class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if (s[0] == ']') or (s[0] == '}') or (s[0] == ')'):
            return False
        for i in s:
            if (i == '{') or (i == '(') or (i == '['):
                stack.append(i)
            else:
                if (i == '}') and (stack != []) and  (stack[-1] == '{'):
                    stack.pop()
                elif (i == ']') and (stack != []) and (stack[-1] == '['):
                    stack.pop()
                elif (i == ')') and (stack != []) and (stack[-1] == '('):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

          