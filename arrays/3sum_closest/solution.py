from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        final_diff = 100000
        final_sum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    print(f"{i}: {nums[i]}, {j}: {nums[j]}, {k}: {nums[k]}")
                    sum = nums[i] + nums[j] + nums[k]
                    diff = abs(sum - target)
                    print(f"sum: {sum}, diff: {diff}")
                    if diff < final_diff :
                        final_diff = diff
                        final_sum = sum
        
        return final_sum