class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_min(root):
    if root is None:
        return float('inf')
    return min(
         find_min(root.left),
         find_min(root.right)
     )

def find_max(root):
    if root is None:
        return float('-inf')
    return max(
         find_max(root.left),
         find_max(root.right)
     )

root=Node(10)
root.left=Node(5)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(25)
root.right.right=Node(6)

print("Minumum: ",find_min(root))
print("Maximum: ",find_max(root))