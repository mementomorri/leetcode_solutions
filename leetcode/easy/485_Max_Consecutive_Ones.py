class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, counter = 0, 0
        nums.append(0)

        for n in nums:
            if n == 1:
                counter += 1
            elif n == 0:
                cnt = max(counter, cnt)
                counter = 0

        return cnt
