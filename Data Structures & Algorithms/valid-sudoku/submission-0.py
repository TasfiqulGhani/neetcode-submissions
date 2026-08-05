class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(list)
        col_set = collections.defaultdict(list)
        box_set = collections.defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]

                if value != '.':
                    if value in  row_set[r] \
                            or value in col_set[c] \
                                or value in box_set[(r//3,c//3)]:
                        return False
                    row_set[r].append(value)
                    col_set[c].append(value)
                    box_set[(r//3,c//3)].append(value)

        return True