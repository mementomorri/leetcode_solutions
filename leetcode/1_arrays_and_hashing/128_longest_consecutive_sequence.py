"""
128. Longest Consecutive Sequence
Medium
18.7K
862
Companies

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    sorted_nums = sorted(set(nums))
    consecutive_count = list()
    curr_count = 1
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i + 1] - sorted_nums[i] == 1:
            curr_count += 1
        else:
            if curr_count > 1:
                consecutive_count.append(curr_count)
                curr_count = 1
    consecutive_count.append(curr_count)
    return max(consecutive_count)


if __name__ == '__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
