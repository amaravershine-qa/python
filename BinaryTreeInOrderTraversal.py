class Node:
    """Represents a single node in the binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root):
    """Performs an in-order traversal (Left, Root, Right) and prints the data."""
    if root:
        # 1. Traverse the left subtree
        inorder_traversal(root.left)
        
        # 2. Visit the root node
        print(root.data, end=" ")
        
        # 3. Traverse the right subtree
        inorder_traversal(root.right)


# --- Driver Code to Test the Implementation ---
if __name__ == "__main__":
    # Constructing the following binary tree:
    #        1
    #       / \
    #      2   3
    #     / \  / \
    #    4   5 6  7
    #   / \  / \
    #  8  9 10 11

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.right.right.left = Node(10)
    root.right.right.right = Node(11)

    print("In-order Traversal of the binary tree is:")
    inorder_traversal(root)
