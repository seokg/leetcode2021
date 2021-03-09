class Solution:
    # Runtime: 32 ms
    # Memory Usage: 14.5 MB
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root, root)
    
    def mirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return (node1.val == node2.val) \
                    and self.mirror(node1.right, node2.left) \
                    and self.mirror(node1.left, node2.right) 