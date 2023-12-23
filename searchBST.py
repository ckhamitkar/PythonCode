def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      if not root:
        return None

      if root.val < val:
        return self.searchBST(root.right, val)

      elif root.val > val:
        return self.searchBST(root.left, val)

      else:
        return root        