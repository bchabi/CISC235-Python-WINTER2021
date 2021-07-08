'''
This class creates a head based implementation of a priority Queue
Question 2.3
Brie Basma Chabi
20109050
'''

import WebPageIndex as web
from os import listdir
from os.path import isfile, join


class WebpagePriorityQueue:
    def __init__(self, webpage):
        self.list = []  # Stores all the webPageIndex Instances in a random order not heap.
        self.heapList = []
        self.query = ""
        self.size = 0
        files = [f for f in listdir(webpage) if isfile(join(webpage, f))]
        for file in files:
            if file.endswith(".txt"):
                self.list.append(web.WebPageIndex(file))

    def calculatePriority(self, data, webpageIndex):
        # Passed a query string  and a webPageIndex instance will return a priority for that webpage for the particular string
        string = []
        for word in data.split():
            string.append(word)
        priority = 0
        for item in string:
            priority = priority + webpageIndex.getcount(item)
        return priority

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):

        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def swap(self, pos1, pos2, heapList):
        heapList[pos1], heapList[pos2] = (heapList[pos2],
                                          heapList[pos1])

    def createMaxHeap(self, query, webpage):
        self.query = query
        self.heapList.append(webpage)
        self.size = len(self.heapList)
        current = self.size - 1
        while (self.calculatePriority(query, self.heapList[current]) > self.calculatePriority(query, self.heapList[
            self.parent(current)])):
            self.swap(current, self.parent(current), self.heapList)
            current = self.parent(current)

    def peek(self):
        return self.heapList[0]

    def poll(self):
        ans = self.heapList[0]
        self.heapList[0] = self.heapList[len(self.heapList) - 1]
        self.heapList.pop()
        self.reheap(self.query)
        return ans

    def reheap(self, query):
        self.query = query
        heapList2 = []
        for i in self.heapList:
            self.query = query
            heapList2.append(i)
            current = len(heapList2) - 1
            while (self.calculatePriority(query, heapList2[current]) > self.calculatePriority(query, heapList2[
                self.parent(current)])):
                pos1 = current
                pos2 = self.parent(current)
                heapList2[pos1], heapList2[pos2] = (heapList2[pos2], heapList2[pos1])
                current = self.parent(current)
        self.heapList = heapList2


if __name__ == "__main__":
    w = WebpagePriorityQueue("data")
    for i in w.list:
        w.createMaxHeap("array you", i)
        print(w.peek())
    print(w.poll())
