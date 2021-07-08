'''
This class creates an AVLTreeMap
Question 2.1
Brie Basma Chabi
20109050
'''


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTreeMap(object):

    def get(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root.value
        if (key < root.key):
            return self.get(root.left_child, key)
        else:
            return self.get(root.right_child, key)

    def getBalanceFactor(self, root):
        if not root:
            return 0
        return self.getheight(root.left_child) - self.getheight(root.right_child)

    def getheight(self, root):
        if not root:
            return 0

        return root.height

    def leftRotate(self, temp1):

        temp2 = temp1.right_child
        temp3 = temp2.left_child

        temp2.left_child = temp1
        temp1.right_child = temp3

        temp1.height = 1 + max(self.getheight(temp1.left_child),
                               self.getheight(temp1.right_child))
        temp2.height = 1 + max(self.getheight(temp2.left_child),
                               self.getheight(temp2.right_child))

        return temp2

    def rightRotate(self, temp1):

        temp2 = temp1.left_child
        temp3 = temp2.right_child

        temp2.right_child = temp1
        temp1.left_child = temp3

        temp1.height = 1 + max(self.getheight(temp1.left_child),
                               self.getheight(temp1.right_child))
        temp2.height = 1 + max(self.getheight(temp2.left_child),
                               self.getheight(temp2.right_child))

        return temp2

    def put(self, root, key, value):

        if root is None:
            return Node(key, value)
        elif key == root.key:
            root.value.append(value)
        elif key < root.key:
            root.left_child = self.put(root.left_child, key, value)
        else:
            root.right_child = self.put(root.right_child, key, value)

        root.height = 1 + max(self.getheight(root.right_child), self.getheight(root.left_child))

        BalanceFactor = self.getBalanceFactor(root)
        # Check for unbalanced
        if BalanceFactor > 1 and key < root.left_child.key:
            # right_child Rotate
            return self.rightRotate(root)

        if BalanceFactor > 1 and key > root.left_child.key:
            # left_child and right_child rotate
            root.left_child = self.leftRotate(root.left_child)
            return self.rightRotate(root)

        if BalanceFactor < -1 and key > root.right_child.key:
            # left_chlld Rotate
            return self.leftRotate(root)

        if BalanceFactor < -1 and key < root.right_child.key:
            # right_child and left_child rotate
            root.right_child = self.rightRotate(root.right_child)
            return self.leftRotate(root)

        return root


"""
Create an AVLTreeMap by inserting the following key-value pairs in order:
15-bob, 20-anna, 24-tom, 10-david, 13-david, 7-ben, 30-karen, 36-erin, 25-
david. Use the above AVLTreeMap test your get and put function.
"""
if __name__ == '__main__':
    r = AVLTreeMap()
    root = None
    root = r.put(root, 15, "bob")
    root = r.put(root, 20, "anna")
    root = r.put(root, 24, "tom")
    root = r.put(root, 7, "ben")
    root = r.put(root, 30, "karen")
    root = r.put(root, 25, "david")

    #Can be changed for testing purposes
    print(r.get(root, 20))
    print(r.getBalanceFactor(root))

