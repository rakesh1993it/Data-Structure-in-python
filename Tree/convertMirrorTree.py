class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def mirror(root):
    if (root == None):
        return
    else:
        temp = root
        mirror(root.left)
        mirror(root.right)
        temp.left, temp.right = temp.right, temp.left


def inOrder(node):
    if (node == None):
        return
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal of the constructed tree is")
    inOrder(root)
    """ Convert tree to its mirror """
    mirror(root)
    print("\nInorder traversal of the mirror tree is ")
    inOrder(root)
    print()