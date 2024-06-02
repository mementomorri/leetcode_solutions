"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""


class Solution:
    def __init__(self):
        self._combinations = {
            1: ["()"],
            3: ["((()))", "(()())", "(())()", "()(())", "()()()"],
        }

    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(open, close,s):
            if len(s)==n * 2:
                self._combinations[n].append(s)
                return
            
            if open<n:
                dfs(open + 1,close, s + "(")
            if close<open:
                dfs(open, close + 1, s + ")")
        
        if n not in self._combinations:
            self._combinations[n] = []
            dfs(0, 0, "")

        return self._combinations[n]
