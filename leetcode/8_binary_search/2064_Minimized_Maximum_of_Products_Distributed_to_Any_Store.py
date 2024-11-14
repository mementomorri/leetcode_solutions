import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def can_distribute(x):
            stories = 0
            for q in quantities:
                stories += math.ceil(q / x)
            return stories <= n

        left, right = 1, max(quantities)
        res = 0
        while left <= right:
            x = (left + right) // 2  # l + (r - l) // 2
            if can_distribute(x):
                res = x
                right = x - 1
            else:
                left = x + 1

        return res
