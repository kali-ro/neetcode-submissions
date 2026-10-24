# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(tree, subtree) -> bool:
            if not tree and not subtree:
                return True
            elif not tree or not subtree:
                return False
            
            if tree.val != subtree.val:
                return False
            else:
                left = sameTree(tree.left, subtree.left)
                right = sameTree(tree.right, subtree.right)
            
            return left and right
        
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False 

        res = False
        if root.val == subRoot.val:
            res = sameTree(root, subRoot)
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return res or left or right