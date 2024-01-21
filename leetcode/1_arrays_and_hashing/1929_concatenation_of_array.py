"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.



Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]



Constraints:

    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000
"""
from time import perf_counter
from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums

def getConcatenation2(nums: List[int]) -> List[int]:
    return nums * 2

def getConcatenation3(nums: List[int]) -> List[int]:
    nums.extend(nums)
    return nums


if __name__ == '__main__':
    perf = perf_counter()
    print(getConcatenation(nums=[1, 2, 1]))
    print(getConcatenation(nums=[1, 3, 2, 1]))
    print(getConcatenation(nums=[1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1]))
    print(perf)

    perf2 = perf_counter()
    print(getConcatenation2(nums=[1, 2, 1]))
    print(getConcatenation2(nums=[1, 3, 2, 1]))
    print(getConcatenation2(nums=[1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1]))
    print(perf2)

    perf3 = perf_counter()
    print(getConcatenation3(nums=[1, 2, 1]))
    print(getConcatenation3(nums=[1, 3, 2, 1]))
    print(getConcatenation3(nums=[1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1,1, 3, 2, 1]))
    print(perf3)
