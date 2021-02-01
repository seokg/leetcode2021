class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # total_len = len(s)
        # for i in range(total_len//2):
        #     tmp = s[i]
        #     s[i] = s[-1-i]
        #     s[-1-i] = tmp
        
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l] # why is this faster?
            l += 1
            r -= 1
