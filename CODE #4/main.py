'''
This class creates a Binary Search Tree
Question 1
Brie Basma Chabi
20109050
'''

COUNT = [10]

class BinarySearchTree:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.data = value


#Used https://cppsecrets.com/ to help with this code
def insert(root, node):
    if root is None: root = node
    else:
        if root.data < node.data:
            if root.right_child is None: root.right_child = node
            else: insert(root.right_child, node)
        else:
            if root.left_child is None: root.left_child = node
            else: insert(root.left_child, node)


# Used https://www.techiedelight.com/calculate-height-binary-tree-iterative-recursive/ to help with this function
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left_child), height(root.right_child))


def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left_child) + countNodes(root.right_child)


def getWeightBalanceFactor(root):
    if root is None:
        return float('-inf')

    rootWbf = countNodes(root.left_child) - countNodes(root.left_child)
    rootWbf = abs(rootWbf)
    lWbf = getWeightBalanceFactor(root.left_child)
    rWbf = getWeightBalanceFactor(root.right_child)
    return max(rootWbf, lWbf, rWbf)


"""Code used from geeksforgeeks as per instruction to print out tree"""


# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right_child, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)

    # Process left child
    print2DUtil(root.left_child, space)


"""Code used from geeksforgeeks as per instruction to print out tree"""


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


if __name__ == '__main__':
    root = BinarySearchTree(1)
    insert(root, BinarySearchTree(7))
    root.left_child = BinarySearchTree(3)
    root.left_child.right_child = BinarySearchTree(11)
    insert(root.left_child, BinarySearchTree(21))
    print("Height:", height(root))
    print("Node Counter:", countNodes(root))
    print("Weight:", getWeightBalanceFactor(root))
    print2D(root)
