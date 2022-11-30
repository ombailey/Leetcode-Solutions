# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def postorder(o,c):
            if o:
                postorder(o.left,c.left)
                postorder(o.right,c.right)
            if o == target:
                self.found = c
                
        postorder(original,cloned)
        return self.found
