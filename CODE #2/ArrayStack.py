"""
Assignment 1
Question 5
This program implements a Stack class using an array based list
by: Brie Basma Chabi
CISC 235
"""


class ArrayStack:
    def __init__(self):
        self.arraylist = []

    def isEmpty(self):
        return self.arraylist == []

    def push(self, e):
        self.arraylist.append(e)

    def pop(self):
        return self.arraylist.pop()

    def top(self):
        return self.arraylist[len(self.arraylist) - 1]

    def Size(self):
        return len(self.arraylist)


if __name__ == '__main__':
    s = ArrayStack()
    s.push("1")
    s.push("2")
    s.push("3")
    print(s.arraylist)  # Should print list ['1','2','3']
    print(s.Size())  # Should print 3
    print(s.pop())  # Should print 3
    print(s.arraylist)  # Should print array ['1','2']
    print(s.top())  # Should print 2
    print(s.isEmpty())  # Should print False
