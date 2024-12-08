class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, sq = 0, len(nums) - 1, 0
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                sq = nums[right]
                right -= 1
            else:
                sq = nums[left]
                left += 1
            res[i] = sq * sq
        return res
