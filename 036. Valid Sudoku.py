"""

problem link : https://leetcode.com/problems/valid-sudoku/
submission detail : https://leetcode.com/submissions/detail/307650459/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(3 * m * n) = O(m*n)

    m * n matrix

    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        w = len(board[0])
        h = len(board)

        if w != h:
            return False

        # possible_nums = set(list(range(1, sub_row * sub_col + 1)) + ["."])

        # validate row
        for i in range(h):
            nums = set()
            for j in range(w):
                if board[i][j] in nums and board[i][j] != ".":
                    return False
                nums.add(board[i][j])

        # validate column
        for i in range(w):
            nums = set()
            for j in range(h):
                if board[j][i] in nums and board[j][i] != ".":
                    return False
                nums.add(board[j][i])

        # validate sub boxes of grid
        for i in range(h // 3):
            for j in range(w // 3):
                nums = set()
                for m in range(3 * i, 3 * i + 3):
                    for n in range(3 * j, 3 * j + 3):
                        if board[m][n] in nums and board[m][n] != ".":
                            return False
                        nums.add(board[m][n])

        return True


class Solution2:
    """
    Time Complexity : O(m * n)

    m * n matrix

    better solution than solution1

    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                if x in rows[i] or x in cols[j] or x in grids[3 * (i // 3) + j // 3]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                grids[3 * (i // 3) + j // 3].add(x)

        return True
