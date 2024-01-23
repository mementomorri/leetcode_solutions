"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.



Constraints:

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""
from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def __split_array(arr: List[int], start: int, end: int):
        if end - start +1 <= 1:
            return arr

        mid = (end + start) // 2
        __split_array(arr, start, mid)
        __split_array(arr, mid+1, end)

        __merge(arr, start, mid, end)
        return arr

    def __merge(arr, start, mid, end):
        left = arr[start: mid + 1]
        right = arr[mid + 1: end + 1]

        i = 0
        j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
    return __split_array(nums, 0, len(nums)-1)


if __name__ == '__main__':
    test1 = sortArray([5, 2, 3, 1])
    print('sortArray([5, 2, 3, 1]):', test1, '== [1,2,3,5] :', test1 == [1, 2, 3, 5])
    test2 = sortArray([5, 1, 1, 2, 0, 0])
    print('sortArray([5, 1, 1, 2, 0, 0]):', test2, '== [0,0,1,1,2,5] :', test2 == [0, 0, 1, 1, 2, 5])
