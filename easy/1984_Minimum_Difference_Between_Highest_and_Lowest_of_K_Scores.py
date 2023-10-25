class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        differences = []
        if len(nums) == 1:
            return 0
        elif len(nums) == k:
            
        else:
            sorted_nums = sorted(nums)
            for n in range(len(nums) - k):
                differences.append(nums[n:k+n])
            
            
            
            
            
            # for n1 in range(len(nums)):
            #     for n2 in range(n1+1,len(nums)):
            #         current_difference = nums[n1]-nums[n2]
            #         if current_difference >=0:
            #             differences.append(current_difference)
            # return min(differences)
