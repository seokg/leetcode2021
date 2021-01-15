class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1 
                nums[j] = nums[i]
        nums = nums[0:j+1]
        return j+1
        
