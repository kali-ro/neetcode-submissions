# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(n):
            # dfs to get the height
            if not n:
                return [True, 0]
            
            l = dfs(n.left)
            r = dfs(n.right)
            
            # determine if balanced 
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

            return [balanced, 1 + max(l[1], r[1])]
        
        res = dfs(root)
        return res[0]

            