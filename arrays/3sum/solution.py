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


    # alternate sollution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result