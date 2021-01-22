class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # to pointer approach
        i = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                tmp = nums[cur]
                nums[cur] = nums[i]
                nums[i] = tmp 
                i += 1
        return nums
        
