#  My solution
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        for i, height_i in enumerate(height):
            for j, height_j in enumerate(height):
                if i < j:
                    width = j - i
                    h = min(height_i, height_j)
                    area = width * h
                    max_area = max(max_area, area)
        
        return max_area
    #  but it does not work when arraay size is too much long

# Another solution
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area with current walls
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            
            # Update maximum area
            max_area = max(max_area, area)
            
            # Move the pointer with the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area