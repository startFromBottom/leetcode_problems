from collections import deque
from typing import List

"""

problem link : https://leetcode.com/problems/word-search/
submission detail : https://leetcode.com/submissions/detail/310470728/


"""


class Solution:
    """

    Time Complexity: O(?)

    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        N, M = len(board), len(board[0])
        visited = [[False for _ in range(M)] for _ in range(N)]

        # helper
        def check(i, j):
            return 0 <= i <= N - 1 and 0 <= j <= M - 1

        def backtrack(string, i, j):
            if "".join(string) == word:
                return True

            dirns = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for dirn in dirns:
                i, j = dirn
                next_char = word[len(string)]

                if check(i, j) and board[i][j] == next_char and not visited[i][j]:
                    string.append(next_char)
                    visited[i][j] = True
                    # move to next solution
                    # terminate recursive call stack when word is found
                    if backtrack(string, i, j):
                        return True
                    # backtrack to previous partial state
                    string.pop()
                    visited[i][j] = False

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if backtrack([word[0]], i, j):
                        return True
                    visited[i][j] = False

        return False


class NotSolution:
    """
    BFS 알고리즘을 통해 접근하려함
    -> failed ..

    BFS로는 불가능한 지점에 마주쳤을 때, 이전 지점으로 backtracking 하는 방법이 떠오르지 않음

    """

    def word_bfs(self, board: List[List[str]], point: tuple, word: str) -> bool:

        if len(word) == 1 and word[0] == board[point[0]][point[1]]:
            return True

        w = len(board[0])
        h = len(board)

        visited_points = set()
        visited_points.add((point[0], point[1]))

        next_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([point])
        while q:
            print(q)
            x, y, idx = q.pop()
            for next_move in next_moves:
                m_x, m_y = next_move
                if 0 <= x + m_x < h and 0 <= y + m_y < w:
                    if (x + m_x, y + m_y) not in visited_points:
                        try:
                            if board[x + m_x][y + m_y] == word[idx + 1]:
                                if idx + 1 == len(word) - 1:
                                    return True
                                q.appendleft((x + m_x, y + m_y, idx + 1))
                                visited_points.add((x + m_x, y + m_y))
                        except IndexError:
                            # word[idx+1] -> error
                            break
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word:
            return False

        w = len(board[0])
        h = len(board)

        starts = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    starts.append((i, j, 0))

        if not starts:
            return False

        for start in starts:
            if self.word_bfs(board, start, word):
                return True

        return False

