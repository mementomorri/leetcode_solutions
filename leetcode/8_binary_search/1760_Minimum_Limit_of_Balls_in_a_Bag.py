class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def _can_divide(max_balls):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls) - 1
                if ops > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = left + ((right - left) // 2)
            if _can_divide(mid):
                right = mid
            else:
                left = mid + 1
        return left
