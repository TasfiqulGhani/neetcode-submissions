class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
     
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        map = {}
        for n in range(n):
            map[n] = []
        
        for node1, node2 in edges:
            map[node1].append(node2)
            map[node2].append(node1)
        
        visited = set()
        counter = 0
        def dfs(x):
            for a in map[x]:
                    if a not in visited:
                        visited.add(a)
                        dfs(a)

        for x in map: 
            if x not in visited:
                dfs(x)
                visited.add(x)
                counter+=1
        return counter

        