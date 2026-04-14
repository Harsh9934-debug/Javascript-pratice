class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal: ", end="")
    inorder(root)
    print("\nPreorder traversal: ", end="")
    preorder(root)
    print("\nPostorder traversal: ", end="")
    postorder(root)
    print()
"""
DETAILED WORKING OF THE ALGORITHM (Tree Traversals):

Recursive Traversals operate strictly recursively focusing on Root, Left, and Right handling order:

1. Inorder (Left, Root, Right):
   - Goes deeply down the left branch entirely.
   - Processes/prints the Current Root item.
   - Goes deeply down the right branch.
   - Generates naturally sorted outputs for Binary Search Trees!

2. Preorder (Root, Left, Right):
   - Immediately prints the Current Root item.
   - Recursively dives left, then inherently dives right.
   - Heavily utilized for cloning configurations physically.

3. Postorder (Left, Right, Root):
   - Penetrates all the way to the deepest left and deepest right children sequentially BEFORE processing the Root element itself.
   - Highly useful for node deletion and physical memory free-up since it removes children before parents.
"""
