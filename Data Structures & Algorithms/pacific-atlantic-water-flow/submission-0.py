class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        ATL, PAC = set(), set()

        def dfs(r, c, visited, last):
            if (r,c) in visited or r not in range(ROW) or c not in range(COL) or heights[r][c] < last:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            

        for c in range(COL):
            dfs(0, c, PAC, heights[0][c])
            dfs(ROW-1, c, ATL, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, PAC, heights[r][0])
            dfs(r, COL-1, ATL, heights[r][COL-1])
        f = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in PAC and (r,c) in ATL:
                    f.append((r,c))
        return f







        