"""
problem link : https://leetcode.com/problems/container-with-most-water/
submission detail : https://leetcode.com/submissions/detail/301060689/
"""

from typing import List


class Solution:
    """
    O(n**2) Solution -> time exceed
    brute force

    """

    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                area = abs(j - i) * min(height[i], height[j])
                ans = max(ans, area)
        return ans


class Solution:
    """
    O(n) solution

    Two Pointers Approach

    Ref) https://leetcode.com/problems/container-with-most-water/solution/

    """
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        while right > left:
            ans = max(ans, (right-left) * min(height[left], height[right]))
            # 높이가 낮은 쪽의 line의 index를 변경
            # (높이가 높은 쪽의 line을 변경하면, width는 무조건 줄어드는데 height는 더 커질 수 없기 때문)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return ans