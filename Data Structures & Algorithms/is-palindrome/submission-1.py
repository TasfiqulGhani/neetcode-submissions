class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s)-1

        def isAlpha(char):
            if ord('A') <= ord(char) <= ord('Z') or  ord('a') <= ord(char) <= ord('z') or  ord('0') <= ord(char) <= ord('9'):
                return True
            return False

        while start<end:
            if not isAlpha(s[start]):
                start+=1
            elif  not isAlpha(s[end]):
                end-=1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start+=1
                end-=1
        return True


        