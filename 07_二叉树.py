# coding:utf-8

class Node(object):
    """ 二叉树节点 """
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):        # 层序添加接树的节点
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def level(self, root):      # 层序遍历  根->左->右
        if root:
            queue = [root]      # 存放节点
            res = []            # 存放节点的值
            while queue:        # 如果节点列表不为空
                cur_node = queue.pop(0) # 删除节点列表的第一个节点并返回
                res.append(cur_node.val)# 添加该节点的值到res
                if cur_node.left:       # 如果该节点的左子节点存在，则添加节点列表
                    queue.append(cur_node.left)
                if cur_node.right:      # 如果该节点的右子节点存在，则添加节点列表
                    queue.append(cur_node.right)
            return res
        return

    def preorder(self,root):    # 前序遍历  根->左->右
        res = []
        if root:                                # 如果根节点存在
            res.append(root.val)               # 添加根节点
            res += self.preorder(root.left)     # 合并左子树列表
            res += self.preorder(root.right)    # 添合并右子树列表
        return res

    def inorder(self,root):     # 中序遍历 ,左->根->右
        res = []
        if root:
            res += self.inorder(root.left)
            res.append(root.val)
            res += self.inorder(root.right)
        return res

    def postorder(self,root):   # 后序遍历，左->右->根
        res = []
        if root:
            res += self.postorder(root.left)
            res += self.postorder(root.right)
            res.append(root.val)
        return res


if __name__ == "__main__":
    tree = Tree()
    for i in range(10):
        tree.add(i)

    print(tree.level(tree.root))
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
