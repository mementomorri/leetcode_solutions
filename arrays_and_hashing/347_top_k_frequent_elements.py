from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [n[0] for n in Counter(nums).most_common(k)]
        count_common = Counter(nums).most_common(k)
        result, _ = zip(*count_common)
        return list(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    # print(sol.topKFrequent(nums = [1], k = 1))
    # print(sol.topKFrequent(nums = [3,0,1,0], k = 1))
