
class Node:

    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data

    def insert(self, data): # 插入节点
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):  # 查找节点
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    def PrintTree(self):    # 打印树
        res = []
        if self.left:
            res += self.left.PrintTree()
        if self.right:
            res += self.right.PrintTree()
        res.append(self.data)
        return res


root = Node(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)



print(root.PrintTree())
