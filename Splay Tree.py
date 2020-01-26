
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent=None


class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None)


    def Insert(self, value):
        self.root = self._Insert(value, self.root)
        self.splay(value)

    def _Insert(self, value, root):
        if root == None:
            root = Node(value)

        else:
            if value > root.value:
                root.right = self._Insert(value, root.right)
            else:
                root.left = self._Insert(value, root.left)

        return root

    def PreOrder(self):
        return self._PreOrder(self.root)

    def _PreOrder(self, root):
        List = []
        if root is None:
            return List
        if root:
            List.append(root.value)
        if root.left is not None:
            List += self._PreOrder(root.left)
        if root.right is not None:
            List += self._PreOrder(root.right)
        elif root.value == None:
            return List
        return List


    def InOrder(self):
        return self._InOrder(self.root)

    def _InOrder(self, root):
        List = []
        if root is None:
            return List
        if root.left is not None:
            List += self._InOrder(root.left)
        if root:
            List.append(root.value)
        if root.right is not None:
            List += self._InOrder(root.right)
        return List


    def PostOrder(self):
        return self._PostOrder(self.root)

    def _PostOrder(self, root):
        List = []
        if root is None:
            return List
        if root.right is not None:
            List += self._PostOrder(root.right)
        if root.left is not None:
            List += self._PostOrder(root.left)
        if root:
            List.append(root.value)

        return List


    def Height(self):
        return self._Height(self.root)

    def _Height(self, root):
        if root == None:
            return -1
        l = self._Height(root.left)
        r = self._Height(root.right)
        return 1 + max(l, r)


    def FindMin(self):
        return self._FindMin(self.root)

    def _FindMin(self, root):
        if root == None:
            return None

        if root.left == None:
            return root.value

        return self._FindMin(root.left)


    def FindMax(self):
        return self._FindMax(self.root)

    def _FindMax(self, root):
        if root == None:
            return None
        if root.right == None:
            return root.value
        return self._FindMax(root.right)


    def Successor(self):
        return self._Successor(self.root)

    def _Successor(self, root):
        if root == None:
            return -1
        elif root.right == None:
            return root.value
        else:
            return self._FindMin(root.right)


    def Predecessor(self):
        return self._Predecessor(self.root)

    def _Predecessor(self, root):
        if root == None:
            return -1
        elif root.left == None:
            return root.value
        else:
            return self._FindMax(root.left)


    def _Search(self, value, root):

        if root.value == value:
            self.splay(root.value)

        elif value > root.value:
            if root.right != None:
                self._Search(value,root.right)
            else:
                self.splay(root.value)
        else:
            if root.left != None:
                self._Search(value,root.left)
            else:
                self.splay(root.value)

    def Search(self,value):
        self._Search(value,self.root)


    def Delete(self,n):
        self.splay(n)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root != None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root != None:
            right_subtree.root.parent = None

        if left_subtree.root != None:
            m = left_subtree._FindMax(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root

    def splay(self, value):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if value < t.value:
                if t.left == None:
                    break
                if value < t.left.value:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif value > t.value:
                if t.right == None:
                    break
                if value > t.right.value:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t



a = SplayTree()
a.Insert(7)
a.Insert(5)
a.Insert(3)
a.Insert(2)
a.Insert(6)
print("_________Insert__________")
print("Preorder =", a.PreOrder())
print("Inorder =", a.InOrder())
print("Postorder =", a.PostOrder())
print("Height =", a.Height())
print("Min =", a.FindMin())
print("Max =", a.FindMax())
print("Successor =", a.Successor())
print("Predecessor =", a.Predecessor())
print("root =",a.root.value)
a.Search(5)
a.Search(8)
print("_________Search___________")
print("Preorder =", a.PreOrder())
print("Inorder =", a.InOrder())
print("Postorder =", a.PostOrder())
print("Height =", a.Height())
print("Min =", a.FindMin())
print("Max =", a.FindMax())
print("Successor =", a.Successor())
print("Predecessor =", a.Predecessor())
print("root =",a.root.value)
a.Delete(3)
a.Delete(7)
print("_________Delete___________")
print("Preorder =", a.PreOrder())
print("Inorder =", a.InOrder())
print("Postorder =", a.PostOrder())
print("Height =", a.Height())
print("Min =", a.FindMin())
print("Max =", a.FindMax())
print("Successor =", a.Successor())
print("Predecessor =", a.Predecessor())
print("root =",a.root.value)
