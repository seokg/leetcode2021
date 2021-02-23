# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        
        while head:
            if not hasattr(head, 'flag'):
                head.flag = False
                
                
            if not head.flag: # head flag is first visited
                head.flag = True
            
            else:
                return True
            
            head = head.next 
            
        return False
            
#         hash_table = dict()
        
#         while head:
#             print(hash_table)
#             if head in hash_table:
#                 return True
            
#             hash_table.add(head)
            
#             head = head.next
            
#         return False
            
        
        