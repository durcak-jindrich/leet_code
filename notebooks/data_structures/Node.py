from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    def __str__(self):
        return "{{val:{self.val}, left:{self.left}, right:{self.right}}}".format(self=self)