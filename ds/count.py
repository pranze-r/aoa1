class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0 
    return 1 +  count_leaf_nodes(root.left)+count_nodes(root.right)

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left)+count_nodes(root.right)

def count_internal_nodes(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + count_internal_nodes(root.left)+count_internal_nodes(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)

print("Total Nodes:", count_nodes(root))
print("Leaf Nodes:", count_leaf_nodes(root))
print("Internal Nodes:", count_internal_nodes(root))