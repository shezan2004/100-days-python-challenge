class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def balanceBST(self, root):
        # Step 1: In-order traversal to get sorted values
        sorted_vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Recursive function to build a balanced BST
        def build_balanced_tree(left, right):
            if left > right:
                return None
            
            # Pick the middle element to be the root of this subtree
            mid = (left + right) // 2
            node = TreeNode(sorted_vals[mid])
            
            # Recursively build the left and right subtrees
            node.left = build_balanced_tree(left, mid - 1)
            node.right = build_balanced_tree(mid + 1, right)
            
            return node
        
        return build_balanced_tree(0, len(sorted_vals) - 1)