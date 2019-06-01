# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderHelper(self, root, levels, level):
        if root is None: return

        if len(levels) <= level:
            levels.append([root.val])
        else:
            levels[level].append(root.val)

        self.levelOrderHelper(root.left, levels, level+1)
        self.levelOrderHelper(root.right, levels, level+1)
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        self.levelOrderHelper(root, levels, 0)
        return levels
