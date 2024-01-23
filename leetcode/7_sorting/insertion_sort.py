"""
Not a challenge, just fun
"""
from typing import List


def sortArray(self, nums: List[int]) -> List[int]:
    duplicate_nums = nums.copy()
    for i in range(1, len(duplicate_nums)):
        j = i - 1
        while j >= 0 and duplicate_nums[j + 1] < duplicate_nums[j]:
            duplicate_nums[j + 1], duplicate_nums[j] = duplicate_nums[j], duplicate_nums[j + 1]
            j -= 1
        return duplicate_nums
