class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # The main catch is here the statement in the question saying that return the most occuring element which is
        # having occurance of more than the half length of the list.
        # So if thats the case when you will sort the list in a decreasing or non decreasing order the mid element will
        # alswas be the element which is having occurance of more than the half length of the list
        # so we just sort the numbers and then return the mid element

        nums.sort()
        return nums[len(nums)//2]