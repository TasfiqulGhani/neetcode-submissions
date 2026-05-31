class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True


    def search(self, word: str) -> bool:
        return self.dfs(self.root,word,0)
    
    def dfs(self,curr, word , index):
        if index == len(word):
            return curr.end

        c = word[index]

        if c == '.':
            for node in curr.children.values():
                if self.dfs(node, word , index+1):
                    return True
            return False
        else:
            if c in curr.children:
                return self.dfs(curr.children[c], word , index+1)
            else:
                return False

        
