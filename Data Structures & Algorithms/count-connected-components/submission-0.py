class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0 :
            return 0
        
        if n == 1:
            return 1

        my_map = {node:[] for node in range(n)}

        for node1, node2 in edges:
            my_map[node1].append(node2)
            my_map[node2].append(node1)

        visited = set()
        def dfs(node):
            for child in my_map[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        counter = 0
        for node in my_map:
            if node not in visited:
                dfs(node)
                visited.add(node)
                counter+=1


        return counter
        