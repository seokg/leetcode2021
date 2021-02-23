# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode()
        
        output = dummy
        # l1_eol = False
        # l2_eol = False
        while 1:
            # if l1.next == None:
            #     # output.next = l2
            #     # break
            #     l1_eol = True
            # if l2.next == None:
            #     # output.next = l1
            #     # break
            #     l2_eol = True
            if l1 is None:
                output.next = l2
                break
            if l2 is None:
                output.next = l1
                break
                
            if l1.val < l2.val:
                output.next = l1
                l1= l1.next
                # print("l1 val ",l1.val)
                # break
            else:
                output.next = l2
                l2= l2.next 
                # print("l2 val ",l2.val)
                # break
            output = output.next
            

        return dummy.next
    
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2