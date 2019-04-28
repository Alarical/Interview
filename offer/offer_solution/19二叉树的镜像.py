class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        def dfs(root):
            if root == None:
                return
            if root.left == None and root.right == None:
                return
            temp = root.left
            root.left = root.right
            root.right = temp

            if root.left != None:
                dfs(root.left)
            if root.right != None:
                dfs(root.right)
        dfs(root)
        return root