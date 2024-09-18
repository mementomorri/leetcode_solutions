"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 109
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        _compare = lambda n1, n2: -1 if n1 + n2 > n2 + n1 else 1

        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(_compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)
