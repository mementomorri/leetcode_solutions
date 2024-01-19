"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step



Constraints:

    1 <= n <= 45
"""

class Solution:
    def __init__(self):
        self.cache = {
            1 : 1,
            2 : 2,
            3 : 3,
            4 : 5
        }

    def initial_climbStairs(self, n: int) -> int:
        m=n
        while n not in self.cache:
            if m-2 in self.cache and not self.cache.get(m-1, False):
                self.cache[m-1] = self.cache[m-3] + self.cache[m-2]
            if m-1 in self.cache:
                self.cache[m] = self.cache[m-2] + self.cache[m-1]
                m += 1
            else:
                m -= 1

        return self.cache[n

    def dumb_but_fast_climbStairs(self, n: int) -> int:
        prev_prev = 1
        prev = 2
        for i in range(2, n + 1):
            prev, prev_prev = prev + prev_prev, prev
        return prev_prev
