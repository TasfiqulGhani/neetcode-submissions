class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        numbers = 0
        row , col = len(grid), len(grid[0])

        def dfs(grid,r,c):
            if  r not in range(row) or c not in range(col) or grid[r][c] == '0' or (r,c) in visited:
                return

            visited.append((r,c))
            directions = [
                (0,1),(0,-1),
                (1,0),(-1,0)
            ]
            for direction in directions:
                dr, dc = direction
                x , y = dr+r , dc +c 
                dfs(grid=grid,r=x,c=y)


    
        for r in range(row):
            for c in range(col): 
                if grid[r][c] == '1' and  (r,c) not in visited:
                    numbers=numbers+1
                    dfs(grid,r,c)
        return numbers