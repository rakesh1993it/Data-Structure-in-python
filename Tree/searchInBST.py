# Python program to demonstrate insert operation in binary search tree

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def search(root, key):
    if root:
        if root.val== key:
            return root
        elif root.val< key:
            return search(root.right,key)
        else:
            return  search(root.left,key)
# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above functions
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

# Print inoder traversal of the BST
inorder(r)
print("searched elements is:", search(r,40).val)

