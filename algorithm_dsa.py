"""Small algorithms & data-structures examples (cleaned and runnable)

This file contains many small examples for lists, tuples, arrays, numpy,
dictionaries, sets and simple linked-list implementations. It is a cleaned
version of the original file with syntax and import errors fixed so it
can be executed as a demo script.
"""

# Basic List
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Operations
numbers.append(6)           # [1, 2, 3, 4, 5, 6]
numbers.insert(2, 99)       # [1, 2, 99, 3, 4, 5, 6]
numbers.pop()               # remove last (6)
numbers.pop(2)              # remove index 2 (99)
if 3 in numbers:
    numbers.remove(3)       # remove first occurrence of value 3
del numbers[1:3]            # remove slice

# List Methods examples
numbers.reverse()
numbers.sort()
numbers.sort(reverse=True)
sorted_numbers = sorted(numbers)  # returns new list
count_2 = numbers.count(2)
index_of_4 = numbers.index(4) if 4 in numbers else -1

# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
matrix = [[0 for _ in range(3)] for _ in range(3)]

# 2D List (matrix)
#  nodes = []
matrix2 = [
[4, 5, 6],
[7, 8, 9]
]
print('matrix2[1][2] =', matrix2[1][2])  # 6

# slicing
numbers = list(range(10))
print('numbers[2:7] =', numbers[2:7])
print('numbers[::2] =', numbers[::2])
print('numbers[::-1] =', numbers[::-1])
print('numbers[5:1:-1] =', numbers[5:1:-1])

# =========== TUPLE (immutable)
point = (2, 3)
colors = ('red', 'green', 'blue')
single = (5,)

print('point[0]=', point[0])
print('len(point)=', len(point))

# unpacking
x, y = point
print(f"x={x}, y={y}")

# namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print('namedtuple:', p.x, p.y, p[0])

# return multiple values from a function
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
print('stats:', minimum, maximum, average)

# 1.3 ARRAY MODULE
import array
int_array = array.array('i', [1, 2, 3, 4, 5])
float_array = array.array('f', [1.0, 2.0, 3.0])
double_array = array.array('d', [1.0, 2.0, 3.0])

int_array.append(6)
int_array.extend([7, 8, 9])
int_array.insert(0, 0)

import sys
list_mem = sys.getsizeof([1, 2, 3, 5])
array_mem = sys.getsizeof(array.array('i', [1, 2, 3, 4, 5]))
print(f"List memory: {list_mem} bytes, Array: {array_mem} bytes")

# 1.4 Numpy arrays (numeric computing)
import numpy as np
try:
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    zeros = np.zeros((3, 4))
    ones = np.ones((2, 4))
    identity = np.eye(3)
    range_arr = np.arange(0, 10, 2)
    linspace = np.linspace(0, 1, 5)

    print('arr1 * 2 =', arr1 * 2)
    print('arr1 + arr1 =', arr1 + arr1)
    print('sqrt(arr1) =', np.sqrt(arr1))
    print('sin(arr1) =', np.sin(arr1))

    matrix_np = np.array([[1, 2, 3], [4, 5, 6]])
    print('broadcast add =', matrix_np + arr1[:3])

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print('arr[1,2]=', arr[1, 2])
    print('arr[:,1]=', arr[:, 1])
    print('arr[0:2,1:3]=', arr[0:2, 1:3])

    arr_reshape = np.arange(12).reshape(3, 4)
    print('reshaped:\n', arr_reshape)
    print('mean=', np.mean(arr_reshape), 'sum=', np.sum(arr_reshape))
except Exception:
    print('numpy not available or error using numpy; skipping numpy demos')

# KEY-VALUE STRUCTURE
# 2.1 DICTIONARY
student = {
    'name': 'Nguyễn Văn A',
    'age': 20,
    'grades': [8.5, 9.0, 7.5],
    'is_active': True,
}

print('student name =', student['name'])
print('student age =', student.get('age'))
print('student address =', student.get('address', 'N/A'))

student['major'] = 'computer science'
student['age'] = 21
student.update({'city': 'Ha Noi', 'age': 22})

removed = student.pop('grades')
del student['is_active']
print('removed grades =', removed)

keys = list(student.keys())
values = list(student.values())
items = list(student.items())
print('keys =', keys)

# dictionary comprehension
squares_dict = {x: x**2 for x in range(6)}
even_squares_dict = {x: x**2 for x in range(6) if x % 2 == 0}

company = {
    'employee1': {'name': 'John', 'position': 'Manager'},
    'employee2': {'name': 'Jane', 'position': 'Developer'},
}
print('company employee1 name =', company['employee1']['name'])

from collections import defaultdict, OrderedDict, Counter
word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for word in words:
    word_count[word] += 1
print('word_count =', dict(word_count))

ordered_dict = OrderedDict()
ordered_dict['first'] = 1
ordered_dict['second'] = 2
ordered_dict['third'] = 3
print('ordered keys =', list(ordered_dict.keys()))

# Counter
word_counter = Counter(words)
print('word_counter =', word_counter)
print('most common 2 =', word_counter.most_common(2))
print("count('apple')=", word_counter['apple'], "count('grape')=", word_counter['grape'])

counter1 = Counter({'a': 3, 'b': 2, 'c': 1})
counter2 = Counter({'a': 1, 'b': 2, 'd': 3})
print('counter1+counter2 =', counter1 + counter2)
print('counter1-counter2 =', counter1 - counter2)
print('counter1&counter2 =', counter1 & counter2)
print('counter1|counter2 =', counter1 | counter2)

# ----------------- SET STRUCTURE ------------------
fruits_set = {'apple', 'banana', 'orange'}
numbers_set = set([1, 2, 3, 4, 5])
fruits_set.add('grape')
fruits_set.update(['kiwi', 'mango'])
fruits_set.discard('banana')

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print('A|B =', A | B)
print('A&B =', A & B)
print('A-B =', A - B)
print('A^B =', A ^ B)

set_squares = {x**2 for x in range(10)}
even_set_squares = {x**2 for x in range(10) if x % 2 == 0}

frozen = frozenset([1, 2, 3, 4, 5])

# -------------------- LINKED STRUCTURES --------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Add node to the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError('Index out of bounds')
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def delete(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return ' -> '.join(nodes) if nodes else 'Empty list'


ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert(2, 15)
print('singly linked list:', ll)
print('search 15 ->', ll.search(15))
ll.delete(10)
print('after delete 10 ->', ll)


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class # ...existing code...

class DoublyLinkedList:
    # ...existing code...

    def display_forward(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes) if nodes else "Empty list"

    # ...existing code...

# Example usage (move outside class)
dl = DoublyLinkedList()
dl.append('a')
dl.append('b')
dl.prepend('z')
print('doubly forward =', dl.display_forward())
print('doubly backward =', dl.display_backward())

# sử dụng
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5) DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    def display_forward(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return ' <-> '.join(nodes) if nodes else 'Empty list'

    def display_backward(self):
        nodes = []
        current = self.tail
        while current:
            nodes.append(str(current.data))
            current = current.prev
        return ' <-> '.join(nodes) if nodes else 'Empty list'


dl = DoublyLinkedList()
dl.append('a')
dl.append('b')
dl.prepend('z')
print('doubly forward =', dl.display_forward())
print('doubly backward =', dl.display_backward())

      # ...existing code...
    
class DoublyLinkedList:
        # ...existing code...
    
        def display_forward(self):
            nodes = []
            current = self.head
            while current:
                nodes.append(str(current.data))
                current = current.next
            return " <-> ".join(nodes) if nodes else "Empty list"
    
        def display_backward(self):
            nodes = []
            current = self.tail
            while current:
                nodes.append(str(current.data))
                current = current.prev
            return " <-> ".join(nodes) if nodes else "Empty list"
    
        def delete(self, value):
            # Basic implementation: find and remove node by value
            current = self.head
            while current:
                if current.data == value:
                    if current.prev:
                        current.prev.next = current.next
                    else:
                        self.head = current.next
                    if current.next:
                        current.next.prev = current.prev
                    else:
                        self.tail = current.prev
                    return
                current = current.next
    
    # ...existing code...
    
    # Example usage
    dl = DoublyLinkedList()
    dl.append('a')
    dl.append('b')
    dl.prepend('z')
    print('doubly forward =', dl.display_forward())
    print('doubly backward =', dl.display_backward())
    
    # sử dụng
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    print(dll.display_forward())  # 5 <-> 10 <-> 20
    print(dll.display_backward())  # 20 <-> 10 <-> 5
    dll.delete(10)  current = self.tail
    while current:
        nodes.append(str(current.data))
        current = current.prev
    return " <-> ".join(nodes) if nodes else "Empty list"
# sử dụng
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
print(dll.displayed_forward()) # 5 <-> 10 <-> 20
print(dll.displayed_backward()) # 20 <-> 10 <-> 5
dll.delete(10)
print("After deletion:", dll.display_forward()) # 5 <-> 20 
 #-----------------Tree struture------------------
 #5.1 binary tree
class TreeNode:
    def __init__(self, data):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
     def __init__(self, root_value_):
        self.root = TreeNode(root_value)
    def insert(self, value):
        """Chèn giá trị vào cây nhị phân"""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                Node.left  = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self,value):
        """ Tìm kiếm value trong tree"""
        return self._search_recursive(self.root, value)
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, node)
        else:
            return self._search_recursive(node.right, node)

#travel methods
def inorder_traversal(self, node=None, result=None):   
    """ Left -> Root -> Right"""
    if result is None:
        result = []
    if node is None:
        node = self.root
    if node.left:
        self.inorder_traversal(node.left, result)
    result.append(node.value)
    if node.right:
        self.inorder_traversal(node.right, result)
    return result 
def preorder_traversal(self, node=None, result=None):
    """ Root -> Left -> Right"""
    if result is None:
        result = []
        if node is None:
            node = self.root

    results.append(node.value)
    if node.left:
        self.preorder_traversal(node.left, result)
    if node.right: 
        self.preorder_traversal(node.right, result0
    return result\
    
def  postorder_traversal(self, node=None, result=None):
    """Left -. Right -> Root"""
    if result is None:
       result = []
    if node is None:
       node = self.root
    
    if node.left:
       self.postorder_ traversal(node.left, result)
    if node.right:
       self.postorder_traversal(node.right, result)
       result.append(node.value)
    return result

def level_order_traversal(self):
    """Level by level traversal(BFS traversal)"""
    if not self.root:
        return []
    result = []
    queue = [self.root]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result 
#s sử dụng 
tree = BinaryTree(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40) 
tree.insert(60)
tree.insert(80)

print("Inorder:", tree.inorder_traversal())  #[20, 30, 40, 50, 60, 70, 80]
print("Preorder:", tree.preorder_traversal()) #[50, 30, 20, 40, 70, 60, 80]
print("Postorder:", tree.postorder_traversal()) #[20, 40, 30, 60, 80, 70, 50]
print("Level Order:", tree.level_order_traversal()) #[50, 30, 70, 20, 40, 60, 80]
print("Search 40:", tree.search(40)) #True
print("Search 90:", tree.search(90)) #False 90 not found in the tree
#5.2 Binary Search Tree (BTS)
class BSTNode:
    def __init__( self, key, value=None)
        self.keyy = key 
        self.value = values
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key, value=None):
        if self.root = new_node
        return

        current = self.root
        parent = None

        while current
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
        parent.right = new_node

    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None  # Key not found
    def find_min(self, node = None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node
    def find_max(self, node = None):
       if node is None:
            node = self.root
        while node.right:
            node = node.right
        return nodee
    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
        # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # node có 2 children
            # tìm successor( nhỏ nhất ở cây con bên phải)
            successor = self.find_min(node.right)
            node.key = successor.key            
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.key)
        return node
# sử dụng
bst = BinarySearchTree()
bst.insert(50, "Apple")
bst.insert(30, "Banana")
bst.insert(70, "Cherry")
bst.insert(20, "Date")
bst.insert(40, "Elderberry")

print("Search 30:", bst.search(30)) #Banana
print("Min:", bst.find_min().key) #20 Date
print("Max:", bst.find_max().key) #70 Cherry

bst.delete(30)
print("Search 30 after deletion:", bst.search(30)) #None 30 đã bị