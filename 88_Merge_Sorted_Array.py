from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


# [1,2,3,0,0,0]
# [2,5,6]

        index_1 = m-1
        index_2 = n-1
        last = n+m-1

        while index_2 >= 0 :
            if index_1 >= 0 and nums1[index_1] > nums2[index_2]:
                nums1[last] = nums1[index_1]
                index_1 -= 1
            else:
                nums1[last] = nums2[index_2]
                index_2 -= 1
            last -= 1