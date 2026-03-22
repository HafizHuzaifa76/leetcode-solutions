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
