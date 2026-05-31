class Solution:
    def isValid(self, s: str) -> bool:
         closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
         stack = []

         for i in range(len(s)):
            bracket = s[i]
            if bracket in closeToOpen:
                if stack and closeToOpen[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(bracket)
         return False if stack else True
