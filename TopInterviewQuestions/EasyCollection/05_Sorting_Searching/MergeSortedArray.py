class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        
        nums1 += nums2
        nums1.sort()
        
        """


        if n == 0:
            return
        
        if m == 0:
            nums1[:] = nums2[:]
            return
        
        nums1[n:n+m] = nums1[:m]
        index1 = 0
        index2 = 0
        total_index = 0
        
        while total_index < (m+n):
            if nums1[n+index1] <= nums2[index2]:
                nums1[total_index] = nums1[n+index1]
                index1 += 1
            else:
                nums1[total_index] = nums2[index2]
                index2 += 1
                
            total_index +=1
            
            if index1 == m:
                nums1[total_index:] = nums2[index2:]
                break
                
            if index2 == n:
                nums1[total_index:] = nums1[n+index1:]
                break
            
        
        print(nums1)
            
            
            
            