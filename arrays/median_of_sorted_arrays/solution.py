class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)

        if length % 2 == 0:
            index = length//2
            value = nums3[index-1] + nums3[index]
            value = value/2
        else:
            index = length//2
            value = nums3[index]

        return value
