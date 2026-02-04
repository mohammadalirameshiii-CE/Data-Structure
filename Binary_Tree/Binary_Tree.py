class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class BTree:
    def __init__(self):
        self.root = None


    def insert_left(self,d):
        if self.root is None:  
            self.root = BNode(d)
            return
        c = self.root
        while c.Lchild is not None:
            c = c.Lchild
        c.Lchild = BNode(d)

    def insert_right(self,d):
        if self.root is None:
            self.root = BNode(d)
            return
        c = self.root
        while c.Rchild is not None:
            c = c.Rchild
        c.Rchild = BNode(d)


    def delete_left(self):
        if self.root is None:
            return
        if self.root.Lchild is None:
            c = self.root.Rchild
            del self.root
            self.root = c
            return
        c = self.root
        while c.Lchild.Lchild:  
            c = c.Lchild
        c1 = c.Lchild
        c.Lchild = None
        del c1

    def delete_right(self):
        if self.root is None:
            return
        if self.root.Rchild is None:
            c = self.root.Lchild
            del self.root
            self.root = c
            return
        c = self.root
        while c.Rchild.Rchild:  
            c = c.Rchild
        c1 = c.Rchild
        c.Rchild = None
        del c1

    def delete_x(self,x):
        if self.root is None:
            return
        if self.root.data == x:
            self.root = None
            return
        self.pdelete(self.root, x)
    def pdelete(self,node,x):
        if node is not None:
            if node.Lchild:
                if node.Lchild.data == x:
                    del node.Lchild
                    node.Lchild = None
                    return
            if node.Rchild:
                if node.Rchild.data == x:
                    del node.Rchild
                    node.Rchild = None
                    return
            self.pdelete(node.Lchild, x)
            self.pdelete(node.Rchild, x)


    def insert_after_L(self,x,d):
        self.pins_after_L(self.root,x,d)
    def pins_after_L(self,node,x,d):
        if node is not None:
            if node.data == x:
                c = node.Lchild
                node.Lchild = BNode(d)
                node.Lchild.Lchild = c
            self.pins_after_L(node.Lchild,x,d)  
            self.pins_after_L(node.Rchild, x, d)


    def insert_after_R(self,x,d):
        self.pins_after_R(self.root,x,d)
    def pins_after_R(self,node,x,d):
        if node is not None:
            if node.data == x:
                c = node.Rchild
                node.Rchild = BNode(d)
                node.Rchild.Rchild = c
            self.pins_after_R(node.Rchild,x,d)  
            self.pins_after_R(node.Lchild,x,d)


    def replace(self,x,y):
        self.replace_recursive(self.root,x,y)
    def replace_recursive(self,node,x,y):
        if node is None:
            return
        if node.data == x:
            node.data = y
            return  
        self.replace_recursive(node.Lchild,x,y)
        self.replace_recursive(node.Rchild,x,y)


    def search(self, x):
        found = self.search_recursive(self.root, x)
        if found:
            print(f"{x} Found.")
        else:
            print(f"{x} Not Found.")
        return
    def search_recursive(self, node, x):
        if node is None:
            return False
        if node.data == x:
            return True
        return self.search_recursive(node.Lchild, x) or self.search_recursive(node.Rchild, x)


    def show(self):
        print("Show:")
        def inorder(node):
            if node:
                inorder(node.Lchild)
                print(node.data, end=' ')
                inorder(node.Rchild)
        inorder(self.root)


    def display_NLR(self):  
        print("\nPreorder Traversal:")
        self.show_NLR(self.root)
    def show_NLR(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.show_NLR(root.Lchild)
            self.show_NLR(root.Rchild)


    
    def display_LNR(self):  
        print("\nInorder Traversal:")
        self.show_LNR(self.root)
    def show_LNR(self,root):
        if root is not None:
            self.show_LNR(root.Lchild)
            print(root.data, end=" ")
            self.show_LNR(root.Rchild)


    
    def display_LRN(self):  
        print("\nPostorder Traversal:")
        self.show_LRN(self.root)
    def show_LRN(self,root):
        if root is not None:
            self.show_LRN(root.Lchild)
            self.show_LRN(root.Rchild)
            print(root.data, end=" ")


    def show_BFS(self):
        if not self.root:
            return
        q = [self.root]
        print("\nLevel order:")
        while q:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.Lchild:
                q.append(node.Lchild)
            if node.Rchild:
                q.append(node.Rchild)

# ---------------------------------------------- Practice --------------------------------------------------

    #  سوال1: متدی به کلاس درخت باینری اضافه کنید که تعداد برگ های درخت را بازگرداند
    # روش اول: تابع بازگشتی
    def count_levels_1(self, node):
        if node is None:
            return 0
        if node.Lchild is None and node.Rchild is None:
            return 1
        return self.count_levels_1(node.Lchild) + self.count_levels_1(node.Rchild)

    #  روش دوم: BFS
    def count_levels_2(self):
        if self.root is None:
            return
        q = [self.root]
        count = 0
        while q:
            node = q.pop(0)
            if node.Lchild is None and node.Rchild is None:
                count += 1
            if node.Lchild:
                q.append(node.Lchild)
            if node.Rchild:
                q.append(node.Rchild)
        print(f"Number of leaves by BFS: {count}")


    #  سوال2: متدی به کلاس درخت باینری اضافه کنید که گره های درجه یک را بشمارد (به روش غیر بازگشتی)
    def count_first_degree(self):
        if self.root is None:
            return
        q = [self.root]
        count = 0
        while q:
            node = q.pop(0)
            if (node.Lchild is None and node.Rchild is not None) or (node.Lchild is not None and node.Rchild is None):
                count += 1
            if node.Lchild:
                q.append(node.Lchild)

            if node.Rchild:
                q.append(node.Rchild)
        print(f"Number of leaves by BFS: {count}")


bt = BTree()
bt.root = BNode(70)
bt.insert_left(4)
bt.insert_left(9)
bt.insert_left(50)
bt.insert_left(10)
bt.insert_right(1)
bt.insert_right(43)
bt.insert_after_L(9,18)
bt.replace(1,100)
bt.search(4)



print(f"Number of leaves by Recursive Function: {bt.count_levels_1(bt.root)}")
bt.count_levels_2()

bt.show()
