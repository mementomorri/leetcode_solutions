class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]

        result = []
        self.backtrack(nums, result, [], 0)
        return result

    def backtrack(self, nums, result, path, start):
        subset_copy = path[:]
        result.append(subset_copy)

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, result, path, i + 1)
            path.pop()


if __name__ == '__main__':
    test_case1 = [1, 2, 3]
    test_case2 = [1, 2]
    test_case3 = [0]

    print(Solution().subsets(test_case1))
    print(Solution().subsets(test_case2))
    print(Solution().subsets(test_case3))
