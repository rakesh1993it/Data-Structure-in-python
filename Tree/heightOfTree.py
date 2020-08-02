# Fiend the Height of Binary Tree

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# return the Height of the given Binary Tree
'''
1.if root is not then chek depth f left subtree and also chek depth right subtree
2.then take maximum depth value of left and right subtree 
3. return maximum value + 1
'''

def height(root):
    if root:
        return 1 + max(height(root.left),height(root.right))
    else:
        return 0

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Height of tree is %d" %(height(root)))

