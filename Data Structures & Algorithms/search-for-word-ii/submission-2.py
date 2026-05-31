class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_word = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            root.add_word(word)
        
        ROW, COL = len(board), len(board[0])
        visited, result = set(), set()
        def dfs(r, c, node, word):

            if r not in range(ROW) or c not in range(COL) or board[r][c] not in node.children or (r,c) in visited:
                return
            
            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                result.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, root, "")

        return list(result)




            















