
#  الگوریتمی بنویسید که یک عبارت ریاضی در نمادگذاری پسوندی (مثل 3 4 + 5 *) را دریافت کرده و مقدار آن را محاسبه کند. از یک پشته برای حل مسئله استفاده کنید.

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for i in tokens:
        if i.isdigit():  
            stack.append(int(i))
        else:  
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)  
            else:
                raise ValueError(f"Invalid operator: {i}")

    return stack.pop()

expr = "3 4 + 5 *"
result = evaluate_postfix(expr)
print(result)  


#     تابعی بنویسید که یک رشته شامل پرانتزهای (), [], {} را بررسی کند و تشخیص دهد آیا پرانتزها به درستی بسته شدهاند یا خیر.


def is_balanced(s):
    stack = []
    opening = "([{"
    closing = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced("{[()]}"))  
print(is_balanced("[(])"))
print(is_balanced("(()[]{})")) 
print(is_balanced("((())"))



#     چگونه میتوان یک صف (FIFO) را با استفاده از دو پشته (LIFO) پیاده سازی کرد؟ عملیات enqueue و dequeue را تحلیل زمانی کنید.

class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def insert(self, x):
        self.stack_in.append(x)

    def delete(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            print("Queue is empty")
            return
        return self.stack_out.pop()


q = QueueWithTwoStacks()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())  
q.insert(40)
print(q.delete())
print(q.delete())  



#     یک صف اولویت دار (Priority Queue) با استفاده از لیست پیوندی پیاده سازی کنید. در این صف، عناصر با اولویت بالاتر زودتر حذف میشوند.

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, data, priority):
        a = Node(data, priority)
        if self.head is None or priority < self.head.priority:
            a.next = self.head
            self.head = a
        else:
            c = self.head
            while c.next and c.next.priority <= priority:
                c = c.next
            a.next = c.next
            c.next = a

    def delete(self):
        if self.head is None:
            print("Queue is empty")
            return
        data = self.head.data
        self.head = self.head.next
        return data

    def show(self):
        c = self.head
        while c:
            print(f"({c.data}, priority={c.priority})", end=" -> ")
            c = c.next
        print("None")


pq = PriorityQueue()
pq.insert("Task A", 3)
pq.insert("Task B", 1)
pq.insert("Task C", 2)
pq.insert("Task D", 4)
pq.show()
print("Dequeue:", pq.delete())


#     الگوریتمی بنویسید که تشخیص دهد آیا یک لیست پیوندی تکراروندی (Singly Linked List) دارای حلقه است یا خیر. آیا میتوان این کار را با فضای اضافه ی O(1) انجام داد؟

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def insert_last(self, t):
        if self.head is None:
            a = Node(t)
            self.head = a
            return
        a = Node(t)
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = a

    # ایجاد حلقه در لیست: اتصال انتهای لیست به گره با مقدار مشخص
    def create_loop(self, target_data):
        if not self.head:
            return
        loop_target = None
        c = self.head
        while c.next:
            if c.data == target_data:
                loop_target = c
            c = c.next
        if loop_target:
            c.next = loop_target

print("\n---- با حلقه ----")
ll2 = LinkedList()
ll2.insert_last(10)
ll2.insert_last(20)
ll2.insert_last(30)
ll2.insert_last(40)
ll2.insert_last(50)
ll2.create_loop(30)  
print("حلقه دارد؟", ll2.has_cycle(ll2.head))




#    تابعی بنویسید که یک لیست پیوندی را به صورت گروهی (هر k گره) معکوس کند.
#    مثال:
#    ورودی: 1→2→3→4→5, k = 2
#    خروجی: 2→1→4→3→5

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self,t):
        if self.head is None:
            a = Node(t)
            self.head = a
            return
        a = Node(t)
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = a

    def reverse_k_group(self, head, k):
        current = head
        prev = None
        count = 0
        temp = head
        for i in range(k):
            if not temp:
                return head
            temp = temp.next
        while current and count < k:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1
        if current:
            head.next = self.reverse_k_group(current, k)
        return prev
    def show(self):
        c = self.head
        while c:
            print(c.data, end=' -> ')
            c = c.next
        print('None')

ll = LinkedList()
for i in range(1, 6):
    ll.insert_last(i)
print("Before reversing:")
ll.show()
k = 2
ll.head = ll.reverse_k_group(ll.head, k)
print("After reversing:")
ll.show()


#  الگوریتمی بنویسید که یک درخت دودویی را بهصورت مورب پیمایش کند و مقادیر هر مورب را چاپ کند.
#    مثال:
#        1
#        \/
#      2   3
#      \/  \/
#    4  5 6  7
#    خروجی: [1, 3, 7], [2, 5, 6], [4]

from collections import defaultdict

class BNode:
    def __init__(self, x):
        self.data = x
        self.Lchild = None
        self.Rchild = None

def diagonal_traversal(root):
    result = defaultdict(list)

    def helper(node, diagonal):
        if not node:
            return
       
        result[diagonal].append(node.data)
        
        helper(node.Lchild, diagonal + 1)
       
        helper(node.Rchild, diagonal)

    helper(root, 0)
    # مرتب‌سازی نتایج بر اساس شماره مورب و تبدیل به لیست خروجی
    return [result[d] for d in sorted(result)]


root = BNode(1)
root.Lchild = BNode(2)
root.Rchild = BNode(3)
root.Lchild.Lchild = BNode(4)
root.Lchild.Rchild = BNode(5)
root.Rchild.Lchild = BNode(6)
root.Rchild.Rchild = BNode(7)

output = diagonal_traversal(root)
print(output)  # 


#     تابعی بنویسید که دو گره در یک درخت جستجوی دودویی (BST) دریافت کند و کوچکترین جد مشترک آنها را برگرداند. آیا این کار برای درخت دودویی معمولی (نه BST) هم قابل انجام است؟

class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        self.l = []

    def find_LCA_BST(self,root, n1, n2):
        if not root:
            return None
        if n1 < root.data and n2 < root.data:
            return self.find_LCA_BST(root.Lchild, n1, n2)
        if n1 > root.data and n2 > root.data:
            return self.find_LCA_BST(root.Rchild, n1, n2)
        return root

    def add(self,x):
        if self.root is None:
            self.root = BNode(x)
            self.l.append(x)
            return
        self.padd(self.root,x)
    def padd(self,root,x):
        if x > root.data:
            if root.Rchild == None:
                root.Rchild = BNode(x)
                self.l.append(x)
            self.padd(root.Rchild,x)  
        if x < root.data:
            if root.Lchild is None:
                root.Lchild = BNode(x)
                self.l.append(x)
            self.padd(root.Lchild,x)
        return


bst = Binary_Search_Tree()
for val in [20, 10, 30, 5, 15, 25, 40]:
    bst.add(val)

lca = bst.find_LCA_BST(bst.root, 5, 15)
print("LCA:", lca.data)  

lca = bst.find_LCA_BST(bst.root, 5, 30)
print("LCA:", lca.data)  


class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class BTree:
    def __init__(self):
        self.root = None

    def find_LCA_general(self,root, n1, n2):
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self.find_LCA_general(root.Lchild, n1, n2)
        right = self.find_LCA_general(root.Rchild, n1, n2)

        if left and right:
            return root
        return left if left else right

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



tree = BTree()
tree.insert_left(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.insert_right(5)
n1, n2 = 4, 5
lca = tree.find_LCA_general(tree.root, n1, n2)
print(f"LCA of {n1} and {n2} is: {lca.data if lca else None}")



#    الگوریتمی بنویسید که پیمایش Inorder یک درخت دودویی را بدون بازگشت و با استفاده از یک پشته انجام دهد. تحلیل زمانی آن چیست؟

class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class BTree:
    def __init__(self):
        self.root = None

    def inorder_iterative(self,root): 
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.Lchild
            current = stack.pop()
            print(current.data, end=' ')
            current = current.Rchild

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


bt = BTree()
bt.root = BNode(70)
bt.insert_left(2)
bt.insert_left(6)
bt.insert_left(12)
bt.insert_right(30)
bt.insert_right(8)
bt.inorder_iterative(bt.root)

# تحلیل زمانی:
# تمام گره‌ها دقیقاً یک‌بار وارد پشته و یک‌بار از آن خارج می‌شوند →
# ⏱ O(n) برای n گره.




#     چگونه میتوان یک سیستم کش LRU (Least Recently Used) را با ترکیب یک صف (بر اساس لیست پیوندی) و یک هش مپ پیادهسازی کرد؟ عملیات get و put را شرح دهید.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # O(1)      مقدار رو برمی‌گردونه و گره رو میاره جلو (یعنی اخیراً استفاده‌شده).
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1

    # مقدار جدید می‌ذاره، و اگر کش پر بود، قدیمی‌ترین مقدار رو حذف می‌کنه.     O(1)
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._insert_at_front(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def show(self):
        current = self.head.next
        print("Cache state (newest → oldest):")
        while current != self.tail:
            print(f"Key: {current.key}, Value: {current.value}")
            current = current.next
        print("-" * 30)



cache = LRUCache(2)
cache.put(1, 100)   
cache.put(2, 200)   

print(cache.get(1))  

cache.put(3, 300)   

print(cache.get(2))  
print(cache.get(3))  
print(cache.get(1))  


cache.put(4, 400)  

print(cache.get(3))  
print(cache.get(4)) 
print(cache.get(1))
cache.show()

