from types import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums) - 1:
            return True

        goal = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if goal - i <= nums[i]:
                goal = i
                if goal == 0:
                    return True
            i -= 1
        return False


# 1st I need to understand the question, as I have understood now the ask is to find out whether we can go to last index
# or not.
# Comming to the point how we can go to last index is 
# 1st we will go to 1st index and the value what is in the 1st index thats the maximum length we can jump.
# Mark that its the max and not a fixed length that we have to jump that much, so we have the flexibility to jump what
# ever length but it should be equal or less than the value of current index's value.
# So based on the parmutation combination you need to find out is it possible or not to reach the last index.
# The step is to track from last we will consider the goal and we will iterate from back side
# 1st we will check if the last element which is goal is reachable by its previous element if yes then we can understand
# that if we will reach to the previous element of the last index then we can also reach to last index hence now our
# updated goal would be to reach the previous element of last index and then we will do the same for this we will check if
# we can reach to the current new goal from its previous element or not and lets say for an instance we find out that we
# will not be able to reach at the current new goal from its previous index's value as its value might be 0 then we will
# move one step back means we will check the previous of the previous element of the current element whether we can reach
# at the current goal from there or not if yes then we will change our goal to that point and so on
