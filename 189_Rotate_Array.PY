from types import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1st Approach
        
        # # steps
        # # 1st I will move the last element to 1st before replacing the 1st element store it in a different variable.
        # # then from 2nd element to till last shift one mosition of all and then repeate the same for k times
        # if len(nums) == 0 or len(nums) == 1:
        #     return

        # for i in range(k):
        #     m = nums[0]
        #     nums[0] = nums[-1]
        #     right = 2
        #     left_num = nums[1]
        #     for _ in range(len(nums) - 2):
        #         temp = nums[right]
        #         nums[right] = left_num
        #         right += 1
        #         left_num = temp
        #     nums[1] = m
        # return


        
        # 2nd Approach
        # Here in the next step we will reverse the full array 1st [1,2,3,4] to [4,3,2,1]
        # Then reverse the 1st k elements , lets say k is 2 hence we will reverse 1st two elements [3,4,2,1]
        # Then we will reverse the next element of kth element till the last element [3,4,1,2]
        # This would be the answar
        # one cath wuld be from start we will make k replaced with k % len(nums) as if k the num of elements we need to
        # be replaced if its less than the length list then the modulo would give us the ans as same whatever value is
        # there of k and if both  k  and length of nums are same then we no need to reverse it as its just asking the
        # whole list to be replaced and at the end if the k is bigger than len of list the rotation would be judge based
        # upon the remainder
        # Basically it is a way of putting a cap on any number so that it’s confined within that value and anything that
        # “overflows” over that value resets against from 0.
        # So say say for “n % 3”, any number under 3 will just be 3, but once we surpass 3, the remainder becomes our new
        # value.. 1%3=1, 2%3=2, 3%3=0, 4%3=1, 5%3=2, 6%3=0, 7%3=1.. and so on. It’s actually pretty easy to understand,
        # just look it up if you haven’t yet.
        
        k = k % len(nums)
        i, j = 0, len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = k, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

        