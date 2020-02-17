"""

problem link : https://leetcode.com/problems/zigzag-conversion/
submission detail : https://leetcode.com/submissions/detail/300121862/

"""


class Solution:
    """
    Time Complexity : O(n) , n : length of s

    """
    def convert(self, s: str, numRows: int) -> str:

        # exceptions
        if s == "" or numRows == 1:
            return s
        ans = ""
        n = len(s)
        unit_num = 2 * (numRows - 1)
        # step 1) slice s by unit_num
        # Time Complexity : O(n)
        slice_by_unit_num = []
        i = 0
        while i < n:
            slice_by_unit_num.append(s[i:i + unit_num] + "0")  # add dummy value "0"
            i += unit_num
        each_length = unit_num + 1
        if len(slice_by_unit_num[-1]) < each_length:  # last value : length can be less than the other -> fit
            slice_by_unit_num[-1] += "0" * (each_length - len(slice_by_unit_num[-1]))
        n = len(slice_by_unit_num)
        # example) slice_by_unit_num : ['PAYP0', 'ALIS0', 'HIRI0', 'NG000']
        # step 2) slice_by_unit_num의 각 원소에서 양 끝 값씩 ans에 더해줌
        # Time Complexity : O(n)
        for i in range(each_length // 2 + 1):
            for j in range(n):
                ans += slice_by_unit_num[j][i]
                if i == each_length // 2:
                    continue
                ans += slice_by_unit_num[j][each_length - 1 - i]
        return ans.replace("0", "")
