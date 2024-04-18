class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,2,2,2,2,3,3]
        # left and right both are going to start from 1st position
        # the strategy here is to increment right and check how many of the current item are there lets say for 1st
        # instance it would see that there are two 1s hence we will move our left pointer to 3rd element as when counting
        # the right pointer would be able to assess how many of the perticular element is present after it has touched to
        # every element of that specific element hence it would be at the last place of that specific item.
        # Now if any where we see when the right pointer has counted the element and it has found out that the element is 
        # present more than 2 times then we would move the left pointer to just to the 3rd occurance's location of that
        # specific item 
        # and each time we are moving the left pointer we are copying the r's values to left pointer's location
        # like if left has gone two 3rd position and right is also at 3rd position then we will replace left's value with
        # right one and after that we will increase both by one and then we will do the same again and then we will move
        # r again so that r will be at a new position and the main loop would end and then again r will go counting and
        # we will follow the left accordingly
        # Link:- https://www.youtube.com/watch?v=ycAq8iqh0TI
        
        l,r = 0,0

        while r < len(nums):
            count = 1 # as each element is a new element when r is standing at it
            while r+1 < len(nums) and nums[r] == nums[r+1]: # added exta constraint of r+1 should be less than length as
            # to prevent it to move to the index out of range issu
                r += 1
                count += 1
            for i in range(min(2, count)): #run the loop of replacing the values till the minimum either the count id 1
            # which means the element is present once or the count is more than 1 or more than 2 which means the element
            # is present more times hence we just need to move out left pointer to 3rd position if the element is present
            # more than 2 times so that we can replace the 3rd position with the r's value and move the left value after
            # replacing one value move left to next one
                nums[l] = nums[r]
                l += 1
            # After all done with the current element move the pointer to next unique element
            r += 1
        return l

        # It is a o(n) time complexity as the while loop is iterating when r is less than length of nums yet inside the
        # while loop we are incrementing the r from the current position to till it gets to the same element's last
        # occurance and after that we are changing the values , while doing the value change you notice each time we are
        # not actually iterating through the intire nums list we are only iterating that much time of which the current
        # element's length if if its 1 we are iterating one time and if anything else we are iterating only 2 times and
        # eventually we will iterate in total of length of the output list 
        # Hence summing up the outer while loop and inner while loop its o(n) and the for loop itslef is o(n) so final
        # time complexity is o(2n) which is anyway o(n)
        # and space complexity is o(1) as the valiables we declare at the begining l and r and in the for loop i all will
        # not increase in time they will take the same single element at a perticular period of time hence theie space
        # complexity is o(1)


