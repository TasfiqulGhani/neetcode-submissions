class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area=0
        row, col = len(grid), len(grid[0])


        def dfs(r,c):
            if r not in range(row) or c not in range(col) or grid[r][c] != 1 or (r,c) in visited:
                return 0
            
            visited.add((r,c))

            return 1+ dfs(r-1,c)+ dfs(r+1,c)+ dfs(r,c-1)+ dfs(r,c+1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area,dfs(r,c))
        return max_area