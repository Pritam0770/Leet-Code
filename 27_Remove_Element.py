class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    # Comment either method 1 or 2 to execute 
      
        # Method 1
        length = len(nums)
        k = 0
        if val in nums:
            for _ in range(length):
                if val in nums:
                    nums.pop(nums.index(val))
                    k += 1
                else:
                    return length - k
        return length - k

        # Method 2
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
