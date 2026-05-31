class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        map = {}
        
        for node in range(n):
            map[node] = []
        
        for node1, node2 in edges:
            map[node1].append(node2)
            map[node2].append(node1)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for a in map[node]:
                if a==parent:
                    continue
                if not dfs(a,node):
                    return False
            return True

        return dfs(0,-1) and n == len(visited)

            




