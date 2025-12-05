class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be NULL at this point
            current = stack.pop()
            
            # Add the node to result
            result.append(current.val)
            
            # Visit the right subtree
            current = current.right
            
        return result