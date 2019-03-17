class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):         # 插入节点函数
        if self.val:               # 如果根节点数据存在，则继续
            if val < self.val:        # 如果待插入数据小于根节点数据，则继续
                if self.left is None:       # 如果左子节点为空，则将此数据插入左节点
                    self.left = Node(val)
                else:                       # 如果左子节点不为空，则将左子节点设为根节点，并递归调用插入节点函数
                    self.left.insert(val)  
            elif val > self.val:      # 如果待插入数据大于根节点数据，则继续
                if self.right is None:      # 如果右子节点为空，则将此数据插入右子节点
                    self.right = Node(val)
                else:                       # 如果右子节点不为空，则将右子节点设为根节点，并递归调用插入节点函数
                    self.right.insert(val) 
        else:                       # 如果根节点不存在，则将此节点设为根节点
            self.val = val                
    
    def PrintTree(self):    # 中序打印二叉树
        if self.left:       # 如果左子树存在，则打印左子树
            self.left.PrintTree()
        print(self.val)    # 打印根节点数据
        if self.right:      # 如果右子树存在，则打印左子树
            self.right.PrintTree()

    def preorder(self,root):    # 前序遍历  根->左->右
        res = []
        if root:                                # 如果根节点存在
            res.append(root.val)               # 添加根节点
            res += self.preorder(root.left)     # 合并左子树列表
            res += self.preorder(root.right)    # 添合并右子树列表
        return res                              # 返回列表

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

if __name__ == '__main__':
    
    root = Node(1)
    for i in range(2,16):
        root.insert(i)

    print(root.preorder(root))
    print(root.inorder(root))
    print(root.postorder(root))
