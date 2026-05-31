class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0], [0,1] , [-1,0] , [0,-1]]
        visited = set()
        result = 0
        def dfs(r, c):
            visited.add((r,c))


            if r not in range(ROW) or c not in range(COL) or (r,c) not in visited or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for rd,cd in directions:
                dfs(rd+r,cd+c)


        for r in range(ROW):
            for c in range(COL): 
                if grid[r][c] == "1":
                    dfs(r,c)
                    result+=1
        return result
