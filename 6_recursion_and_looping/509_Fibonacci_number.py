"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.



Constraints:

    0 <= n <= 30
"""

class Solution:
    def __init__(self):
        self.fibs = {
            0 : 0,
            1 : 1,
            2 : 1
        }

    def fib(self, n: int) -> int:
        m=n
        while n not in self.fibs:
            if m-2 in self.fibs and not self.fibs.get(m-1, False):
                self.fibs[m-1] = self.fibs[m-3] + self.fibs[m-2]
            if m-1 in self.fibs:
                self.fibs[m] = self.fibs[m-2] + self.fibs[m-1]
                m += 1
            else:
                m -= 1

        return self.fibs[n]
