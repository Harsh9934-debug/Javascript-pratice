class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def preorder(root):
    if(root):
        print(root.value,end="")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if(root):
        inorder(root.left)
        print(root.value,end="")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end="")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if __name__ == "__main__":
    print("Preorder:")
    preorder(root)
    print("\n")
    print("Inorder:")
    inorder(root)
    print("\n")
    print("Postorder:")
    postorder(root)