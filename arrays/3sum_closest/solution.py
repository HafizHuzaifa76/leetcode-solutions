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



class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        final_sum = nums[0] + nums[1] + nums[2]
        final_diff = abs(final_sum - target)
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(sum - target)
                if diff < final_diff :
                    final_diff = diff
                    final_sum = sum

                if sum < target:
                    j += 1
                else:
                    k -= 1
        
        return final_sum