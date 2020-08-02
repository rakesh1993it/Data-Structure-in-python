# Python program to print level order traversal using Queue
'''
Algorithm:

printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children (first left then right children) to q
    c) Dequeue a node from q and assign it’s value to temp_node
'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative Method to print the height of a binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return
    # Create an empty queue for level order traversal
    queue = []
    # Enqueue Root and initialize height
    queue.append(root)
    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

        # Driver Program to test above function


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left = Node(4)


print("Level Order Traversal of binary tree is -")
printLevelOrder(root)

