class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, ans, curr = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            if curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
