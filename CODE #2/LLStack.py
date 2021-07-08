"""
Assignment 1
Question 5
This program implements a Stack class using an inner Linked link class
by: Brie Basma Chabi
CISC 235
"""


class LLStack:
    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)  # When pushing a new node, replace the current LinkedLink head.
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Empty stack, cannot pop"
        else:
            pop_result = self.head.value
            self.head = self.head.next
            self.size -= 1
            return pop_result

    def top(self):
        if self.isEmpty():
            return "Empty stack, cannot pop"
        else:
            return self.head.value

    def Size(self):
        return self.size


if __name__ == '__main__':
    s = LLStack()
    s.push("One")  # One added into stack
    print(s.isEmpty())  # Should print false
    print(s.top())  # Should print One
    s.push("Two")
    s.push("Three")
    print(s.Size())  # Should print 3
    s.pop()
    print(s.top())  # Should print two
