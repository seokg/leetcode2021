class Solution:
    # Runtime: 36 ms
    # Memory Usage: 16.3 MB
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.search(root, 0)
    
    def search(self, node, depth):
        depth += 1
        depth_left = depth
        depth_right = depth
        
        if node.left is not None:
            depth_left = self.search(node.left, depth)
        if node.right is not None:
            depth_right = self.search(node.right, depth)
        
        if depth_right < depth_left:
            return depth_left
        else:
            return depth_right