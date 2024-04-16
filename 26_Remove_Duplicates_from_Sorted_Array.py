class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,2,3,3,4]
        # we will iterate thought this list will keep two pointers j and k 
        # j would be 1 and k would be 1 also
        # j is 1 coz we want to start updating from 2nd element as the 1st element in a list would always be a unique
        # element the 2nd element could be a duplicate of the 1st one
        # i is 1 coz we also want to start from 2nd element to compare it with its previous element
        # 1st iteration we will check 2nd element and 1st element in list are same or not if not same then we will
        # increase the j and would update the jth element of the nums with ith element of nums
        # which in our case would be nums[j] is nums[1] and nums[i] is nums[1] replace the same element with the same
        # element and then we will increase the j
        # next iteration we will compare nums[i] and nums[i-1] and if not matched then nums[j] is nums[2] would be
        # updated with nums[i] is nums[2] and j increases by 1
        # next iteration nums[i] is compared with nums[i-1] which is 3 compared with 3 both are same hence we will not do
        # anything that means as we did not move j's index here j is still pointing to 3 location which is the 2nd 3 ,
        # j = 3 now
        # next iteration we compare we found 4 is not equal to 3 we update the nums[j] with nums[i] , remember the j is 3
        # now as in previous iteration we did not update it yet the i got updated each time hence i is 4 now so we will
        # update the j with the i and that would be 2nd 3 replaced with 4 then the iteration would be ended.
        # Now the j is the number which was able to cound all the unique items as you can remember 1st element was unique
        # hence j was 1 then next onwards we updated the j only if we got to know that the curent element is not equal to
        # its previous element




        j = 1
        
        # I have made the above one as 1 rather than 0 as when we will want to update any element of array 
        # if its the 1st element then it will always be the unique one as 1st elemnt is a unique element and the what ever
        # comes next that could be a duplicate of the 1st element hence we would want to replace that 2nd appearing
        # element from start rather than remove the 1st element

        for i in range(1, len(nums)):
            # I dod not take the list as when we do something with the original list it afftcts the for loop as well 
            # hence in for loop we took the path of using the range apart from that the 1st element of range is 1 as the
            # comparision should be done from nums[1] which is 2nd element with the first element

            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
