class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        
        robMax = [0 for _ in range(N+1)]
        
        robMax[0] = 0
        robMax[1] = nums[0]
        
        for i in range(2,N+1):
            robMax[i] = max(robMax[i-1], robMax[i-2]+nums[i-1])
            # print(robMax[i])
        return robMax[-1]