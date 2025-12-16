from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [seen[complement], i]

            seen[value] = i
