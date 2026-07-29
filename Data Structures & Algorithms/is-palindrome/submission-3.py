class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        def ischar(c):
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
                return True
            return False

        while L <= R:
            print(f'L : {s[L]} R {s[R]}')
            if not ischar(s[L]):
                L+=1
            elif not ischar(s[R]):
                R-=1
            elif s[L].lower() == s[R].lower():
                L+=1
                R-=1
            else:
                return False
        return True
        