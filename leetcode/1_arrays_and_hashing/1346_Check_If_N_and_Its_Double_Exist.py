class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if 2 * arr[i] in arr[:i] + arr[i + 1 :]:
                return True
        return False