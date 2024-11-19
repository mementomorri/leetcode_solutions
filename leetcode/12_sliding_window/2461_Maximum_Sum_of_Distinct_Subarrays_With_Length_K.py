class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res, cur_sum, left = 0, 0, 0
        prev_idx = dict()

        for right in range(len(nums)):
            cur_sum += nums[right]
            i = prev_idx.get(nums[right], -1)

            while left <= i or right - left + 1 > k:
                cur_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                res = max(res, cur_sum)

            prev_idx[nums[right]] = right
        return res
