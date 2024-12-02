class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = filter(lambda n: len(str(n)) % 2 == 0, nums)
        return len(list(res))
