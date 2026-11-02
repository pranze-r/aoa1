class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return Node(data)
    if root < root.data :
        root.left = insert(root.left,data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

root = None
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    root = insert(root, value)
key = 40
if search(root, key):
    print(key, "found in BST")
else:
    print(key, "not found in BST")