from typing import Typing

"""

problem link : https://leetcode.com/problems/unique-paths-ii/
submission detail : https://leetcode.com/submissions/detail/310491109/


"""


class Solution:
    """

    Time Complexity: O(N * M)

    N * M matrix

    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        N = len(obstacleGrid)
        M = len(obstacleGrid[0])

        try:
            if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
                return 0
        except IndexError:  # obstacleGrid = [[]]
            return 1

        num_paths = [[0 for _ in range(M)] for _ in range(N)]

        # 경계에 있을 때 경로 수 처리
        for i in range(N):
            if obstacleGrid[i][0] == 1:
                break
            num_paths[i][0] = 1

        for j in range(M):
            if obstacleGrid[0][j] == 1:
                break
            num_paths[0][j] = 1

        #
        for i in range(1, N):
            for j in range(1, M):
                if obstacleGrid[i][j] == 1:
                    continue
                num_paths[i][j] = num_paths[i - 1][j] + num_paths[i][j - 1]

        print(num_paths)

        return num_paths[N - 1][M - 1]
