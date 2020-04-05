"""

problem link : https://leetcode.com/problems/happy-number/
submission detail : https://leetcode.com/submissions/detail/318595425/

"""

class MySolution:
    """
    정석적인 방법은 아님..
    Time Complexity : O(?)
    """
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(n):
            digits = []
            l = len(str(n)) - 1
            while l >= 0:
                m = n // (10 ** l)
                digits.append(m)
                n -= m * (10 ** l)
                l -= 1
            s_sum = 0
            for d in digits:
                s_sum += d ** 2
            return s_sum

        while True:
            n = sum_of_squares(n)
            if n == 1 or n == 7:
                return True
            elif n in range(2, 10):
                return False


class Solution2:
    """
    other solution
    Time Complexity : O(?)
    """
    def isHappy(self, n: int) -> bool:
        cases = set()
        result = 0
        while result != 1:
            result = 0
            while n > 0:
                result += (n % 10) * (n % 10)
                n = n // 10
            if result == 1:
                return True
            elif result in cases:
                return False
            else:
                cases.add(result)
                n = result