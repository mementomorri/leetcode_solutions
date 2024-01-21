"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
"""

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        result = nums
        while len(result) > k:
            result.remove(min(result))
        return result


if __name__ == '__main__':
    sol = Solution()
    print('Input: nums = [2,1,3,3], k = 2')
    test_call = sol.maxSubsequence(nums = [1,1,3,3], k = 2)
    print('Output:', test_call, test_call == [3,3])
    print('Input: nums = [-1,-2,3,4], k = 3')
    test_call= sol.maxSubsequence([-1,-2,3,4], 3)
    print('Output:', test_call, test_call == [-1,3,4])
    print('Input: nums = [3,4,3,3], k = 2')
    test_call = sol.maxSubsequence([3,4,3,3], 2) 
    print('Output:', test_call, test_call == [3,4])
    print('Input: nums = [50,-75] k = 2')
    test_call = sol.maxSubsequence([50,-75], 2)
    print('Output:', test_call, test_call == [50, -75])

