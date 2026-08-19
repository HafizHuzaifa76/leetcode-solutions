from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        n = len(nums)
        result = []
        seen = set()
        nums.sort()

        for first in range(n):
            for sec in range(first + 1, n):

                third = sec + 1
                forth = n - 1

                while third < forth:
                    sums = nums[first]  + nums[sec] + nums[third] + nums[forth]

                    if sums == target:
                        res_list = [nums[first], nums[sec], nums[third], nums[forth]]
                        res_tuple = tuple(res_list)
                        if res_tuple not in seen: 
                            seen.add(res_tuple)
                            result.append(res_list)
                        
                        third += 1
                        forth -= 1
                    elif sums < target:
                        third += 1
                    elif sums > target:
                        forth -= 1

        return result