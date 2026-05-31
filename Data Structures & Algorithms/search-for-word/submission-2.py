class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Dimensions of the board
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # Base case: if the current index matches the length of the word, the word is found
            if index == len(word):
                return True
            # If out of bounds or the current cell does not match the word character
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # Temporarily mark the current cell as visited by changing its value
            temp = board[r][c]
            board[r][c] = "#"

            # Explore in all 4 possible directions: up, down, left, right
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )

            # Restore the original value in the cell after exploring
            board[r][c] = temp

            return found

        # Traverse the board
        for i in range(rows):
            for j in range(cols):
                # Start the DFS if the first character matches
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
