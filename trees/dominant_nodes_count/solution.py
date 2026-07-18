# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    large = 0
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.preorder(root, root.val)
        return self.large

    def preorder(self, node, parent):
        if not node:
            return 0

        x = self.preorder(node.left, node.val)
        y = self.preorder(node.right, node.val)
        
        if not (x > node.val or y > node.val):
            self.large += 1
            
        return max(x, y, node.val)