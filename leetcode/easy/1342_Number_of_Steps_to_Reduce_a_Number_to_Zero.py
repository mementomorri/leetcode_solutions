class Solution:
    def numberOfSteps(self, num: int) -> int:
        curr_val = num
        cnt = 0
        while curr_val:
            cnt += 1
            if curr_val % 2 == 0:
                curr_val //= 2
            else:
                curr_val -= 1
        return cnt
