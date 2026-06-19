class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base case: if the node is empty, return an empty list
        if not root:
            return []
            
        # Combine: Current Value + Left Subtree List + Right Subtree List
        return  self.postorderTraversal(root.left) + self.postorderTraversal(root.right)+[root.val]
