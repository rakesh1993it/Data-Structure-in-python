class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Leaf count of the tree is %d" % (getLeafCount(root)))