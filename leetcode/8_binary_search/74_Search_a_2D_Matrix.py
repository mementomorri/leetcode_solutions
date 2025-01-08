class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fisrsts = [row[0] for row in matrix]
        targetRow = self.binarySearch(fisrsts, target, True)
        return self.binarySearch(matrix[targetRow], target, False) >= 0

    def binarySearch(self, nums: List[int], target: int, returnLast: bool) -> int:
        l, r = 0, len(nums) - 1
        mid = 0

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        if returnLast:
            if nums[mid] > target and mid > 0:
                mid -= 1
            return mid
        else:
            return -1
