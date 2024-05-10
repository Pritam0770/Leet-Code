class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2,3,1,1,4]
        l = r = 0
        jump = 0

        while r < len(nums) - 1:
            maxSeen = 0
            for i in range(l, r + 1):
                maxSeen = max(maxSeen, i + nums[i])
            l = r + 1
            r = maxSeen
            jump += 1
        return jump
                
             

# 1st I will start from the 1st element , and from there I will declare 3 variables one would be my current 2nd would be 
# max (the max valued element I can see from my current reach) example:- [2,3,1,1,4] so my current would be 0 as I am
# standing at the 1st element and then my max would be the value of the max elements that I have seen in this current sub
# array would be 2 now I will look into what would I get if I will take the max variable number of jump.
# I would reach to index 2 and that would be 1 now from this index I would look back wards untill the previous curr
# element in this sub array I will check the max element and what would that be I will just look ahead that many numbers
# and the same time I would make my jump +1 , Now while looking I will go to max potential place that I could go from the
# current location and look back till the current element and see which one is the max element after looking I will jump
# to that position and make my curr as that element and from there I will look the max element from the sub array of curr
# to max jump
# We will iterate for len of nums - 1 coz when we will reach to the last index there also we will check back and create a
# jump which is completely not required our goal is to get such a umber so that we can jump till last or greaterthan last
# index.