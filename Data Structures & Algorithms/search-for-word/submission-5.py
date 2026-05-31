class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r >= len(board)
                or r < 0
                or c < 0
                or c >= len(board[0])
                or board[r][c] != word[i]
            ):
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            board[r][c] = tmp

            return found

        row = len(board)
        column = len(board[0])
        for r in range(row):
            for c in range(column):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False