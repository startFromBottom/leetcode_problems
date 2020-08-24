"""

problem link : https://leetcode.com/problems/course-schedule/


"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        in_degree = defaultdict(int)  # 특정 node를 바라보고 있는 edge의 개수

        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1

        q = deque([n for n in range(numCourses) if in_degree[n] == 0])

        cnt = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                cnt += 1
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
        return cnt == numCourses

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조 -> False
            if i in traced:
                return False
            # 이미 방문한 노드 -> False
            if i in visited:
                return True

            traced.add(i)
            for next in graph[i]:
                if not dfs(next):
                    return False
            # 해당 node를 이용한 모든 탐색이 끝났을 때, 방문 내역 삭제
            traced.remove(i)
            # 방문 기록 추가
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True
