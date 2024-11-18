class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N
        left, cur_sum = 0, 0

        for r in range(N + abs(k)):
            cur_sum += code[r % N]
            if r - left + 1 > abs(k):
                cur_sum -= code[left % N]
                left = (left + 1) % N
            if r - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % N] = cur_sum
                elif k < 0:
                    res[(r + 1) % N] = cur_sum
        return res
