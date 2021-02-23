
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return None
        
        m_index = len(nums) // 2
        # print('=====')
        # print('m_index:', m_index)
        # print('list:', nums)
        
        root = TreeNode(nums[m_index])
        root.left = self.sortedArrayToBST(nums[:m_index])
        root.right = self.sortedArrayToBST(nums[m_index+1:])
        
        return root
    
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         def make_tree(lst):
#             if not lst:
#                 return None
#             l = len(lst)
#             mid = l//2
#             node = TreeNode(lst[mid])
#             node.left = make_tree(lst[:mid])
#             node.right = make_tree(lst[mid+1:])
#             return node
         
#         return make_tree(nums)
        