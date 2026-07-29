class Solution:

    def encode(self, strs: List[str]) -> str:
        strx = ""
        for s in strs:
                strx+= str(len(s)) + "#" + s
                
        return strx

    def decode(self, s: str) -> List[str]:
        left,right = 0,0
        result = []
        #5#Hello5#World
        while right < len(s):
                if s[right] == '#':
                    size = s[left:right]
                    print(size)
                    size = int(size)
                    right+=1
                    result.append(s[right: right + size  ])
                    left = right + size
                    right = right + size
                right+=1
        return result