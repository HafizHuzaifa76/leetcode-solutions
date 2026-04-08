# my solution :
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i, val in enumerate(nums):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        values = sorted([nums[i], nums[j], nums[k]])
                        if not values in result:
                            result.append(values)
        
        return result