"""

problem link : https://leetcode.com/problems/subsets/
submission detail : https://leetcode.com/submissions/detail/310779469/

good discussion link : https://leetcode.com/problems/subsets/discuss/527606/Several-python-solution-w-Explanation-and-Demo

"""
from itertools import combinations
from typing import List


class MySolution:
    """

    use itertools.combinations ..

    time complexity : O(2^n)

    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            ans += list(map(list, combinations(nums, i)))
        return ans


class BitSerialSolution:
    """

    link : https://leetcode.com/problems/subsets/discuss/527606/Several-python-solution-w-Explanation-and-Demo

    #1 : Use bit serial mapping

    The bit serial from 0 to 2^n - 1 can be mapped to element selction for subset generation.

    Take nums = [1,2,3] for example.

    size of input = 3.
    Thus, we go through bit serial from 0 to 2^3 -1 = ( 1 << 3 ) - 1 = 7, then getting corresponding subset on the fly.

    0 = 0b 000 = empty set = [ ]
    1 = 0b 001 = select first element = [ 1 ]
    2 = 0b 010 = select second element = [ 2 ]
    3 = 0b 011 = select first and second elements = [ 1, 2 ]
    4 = 0b 100 = select third element = [ 3 ]
    5 = 0b 101 = select first and third elements = [ 1, 3 ]
    6 = 0b 110 = select second and third elements = [ 2, 3 ]
    7 = 0b 111 = select all elements = [ 1, 2, 3 ]

    """

    def subsets(self, nums: List[int]):
        size = len(nums)
        upper_bound = 1 << size
        all_subsets = []
        for bits_sn in range(upper_bound):
            cur_subset = []
            for i in range(size):
                if bits_sn & (1 << i) != 0:
                    cur_subset.append(nums[i])
                print(f"bits_sn: {bits_sn}, i: {i} ===", cur_subset)
            all_subsets.append(cur_subset)

        return all_subsets


class ElementAddingSolution:
    """
    link : https://leetcode.com/problems/subsets/discuss/527606/Several-python-solution-w-Explanation-and-Demo

    #2: Element adding

    Base case is empty set: [ [ ] ]
    Build all subsets from base-case in bottom-up, add one element for each iteration.

    Take nums = [1,2,3] for example.

    Initialization of solution = [ [ ] ] # empty set

    1st iteration, add [ 1 ] to current solution
    solution = [ [ ], [ 1 ] ]

    2nd iteration, add [ 2 ] to current solution
    solution = [ [ ], [ 1 ], [ 2 ], [ 1, 2 ] ]

    3rd iteration, add [ 3 ] to current solution
    solution = [ [ ], [ 1 ], [ 2 ], [ 1, 2 ], [ 3 ], [ 1, 3 ], [ 2, 3 ], [ 1, 2, 3 ] ]

    Completed.

    All subsets = [ [ ], [ 1 ], [ 2 ], [ 1, 2 ], [ 3 ], [ 1, 3 ], [ 2, 3 ], [ 1, 2, 3 ] ]

    """

    def subsets(self, nums: List[int]):
        # Base case
        solution = [[]]

        # General Solution
        # Generate subset by element adding
        for num in nums:
            solution += ([current + [num] for current in solution])

        return solution


class DFSSolution:
    """
    link : https://leetcode.com/problems/subsets/discuss/527606/Several-python-solution-w-Explanation-and-Demo

    #3: Concise DFS

    Base case for solution is empty set [ ]
    size = length of input array.
    grow_index = 0

    Generate all subset by DFS, append current DFS path to solution during each traversal.

    Iterate index i from grow_index to size
    then update grow_index to next forward direction(i+1), and update path as current path + [ nums[ i ] ].

    """

    def subsets(self, nums):

        # Base case
        solution = []
        size = len(nums)

        # Generate all subsets in DFS
        def dfs_helper(grow_index: int, path: List[int], all_subsets: List[List[int]]):
            all_subsets.append(path)
            for i in range(grow_index, size):
                dfs_helper(i+1, path+[nums[i]], all_subsets)

        dfs_helper(grow_index=0, path=[], all_subsets=solution)
        return solution

class MySolution2:
    """

    simple recursion

    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        N = len(nums)
        ans = []
        def recursion(case: List[int], idx: int):
            if idx == N:
                ans.append(case)
                return
            recursion(case, idx + 1)
            recursion(case + [nums[idx]], idx + 1)

        recursion([], 0)

        return ans