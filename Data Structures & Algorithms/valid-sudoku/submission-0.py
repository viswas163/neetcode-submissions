class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        boxes = [set() for _ in range(len(board))]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue

                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                boxi = (i // 3) * 3
                boxj = (j // 3) + 1
                boxIndex = boxi + boxj - 1
                if val in boxes[boxIndex]:
                    return False
                boxes[boxIndex].add(val)

        return True