import sys

class BinTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree(object):
    def __init__(self):
        self.root = None

    def maketree(self, arr):
        mid = len(arr) // 2
        self.root = BinTreeNode(arr[mid])

        self.root.left = self.addsubs(arr[:mid])
        self.root.right = self.addsubs(arr[mid + 1:])

    def addsubs(self, arr):
        self.printtree()

        if len(arr) == 0:
            return None

        mid = len(arr) // 2

        node = BinTreeNode(arr[mid])

        node.left = self.addsubs(arr[:mid])
        node.right = self.addsubs(arr[mid + 1:])
        return node		

    def printtree(self):
        self._printtree(self.root)
        print()

    def _printtree(self, node):
        if node is None:
            return
        
        print(node.value, end=", ")
        self._printtree(node.left)
        self._printtree(node.right)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bt = BinTree()

bt.maketree(a)
bt.printtree()
