# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.segment = []
        self.indx = 0
        def rec(root):
            if root:
                rec(root.left)
                self.segment.append(root.val)
                rec(root.right)
        rec(root)
    def next(self) -> int:
        self.indx+=1
        return self.segment[self.indx-1]
    def hasNext(self) -> bool:
        return self.indx < len(self.segment)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()