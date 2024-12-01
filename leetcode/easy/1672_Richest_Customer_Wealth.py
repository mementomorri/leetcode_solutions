class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 1
        for c in accounts:
            res = max(sum(c), res)
        return res
