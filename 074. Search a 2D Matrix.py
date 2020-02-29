"""

problem link : https://leetcode.com/problems/search-a-2d-matrix/
submission detail : https://leetcode.com/submissions/detail/307935716/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(log(m) + log(n))

    m * n matrix

    """

    def search_list(self, arr: List[int], target: int) -> bool:
        lo = 0
        hi = len(arr) - 1
        while hi >= lo:
            mid = lo + (hi - lo) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix == [[]]:
            return False

        lo = 0
        hi = len(matrix) - 1
        while hi >= lo:
            mid = lo + (hi - lo) // 2
            min_v = matrix[mid][0]
            max_v = matrix[mid][-1]
            if min_v <= target <= max_v:
                return self.search_list(matrix[mid], target)
            elif target < min_v:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
