#27 二叉搜索树与双向链表
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.listhead = None
        self.listtail = None
        
    def Convert(self, pRootOfTree):
        # 递归总得有终止条件，这里是节点为空
        if pRootOfTree == None:
            return
        self.Convert(pRootOfTree.left)
        # head 为None，即当前为中序遍历第一个，即最左下
        if self.listhead == None:
            self.listhead = pRootOfTree
            self.listtail = pRootOfTree
        else: #按照中序遍历顺序,listhead就是链表的头
            self.listtail.right = pRootOfTree
            pRootOfTree.left = self.listtail
            self.listtail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listhead