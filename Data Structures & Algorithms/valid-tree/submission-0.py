class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()
        map = {}
        if not n:
            return True
        for i in range(n):
            map[i] = []

        for n1, n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)
        

        def dfs(i,parent):
            if i in visited:
                return False
            visited.add(i)
            for e in map[i]:
                if e == parent:
                    continue
                if not dfs(e,i): 
                    return False
            return True
        return dfs(0,-1) and len(visited) ==n


            




