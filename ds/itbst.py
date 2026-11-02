class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None

def inorder(root):
    stack=[]
    result=[]

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root=stack.pop()
        result.append(root.data)
        root=root.right
    return result

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)

print("Inorder Traversal: ")
print(inorder(root))
