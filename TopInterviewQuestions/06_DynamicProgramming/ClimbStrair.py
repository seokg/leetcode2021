class Solution:
    def climbStairs(self, n: int) -> int:
        # save
        n_1 = -1
        n_2 = -1
        
        for i in range(n):
            if i == 0:
                n_1 = 1
                n_2 = -1
            elif i ==1:
                n_2 = 1
                n_1 = n_1 + n_2 
            else:
                tmp = n_1
                n_1 = n_1 + n_2
                n_2 = tmp
        return n_1