'''
This class creates a web page index using an AVLTreeMap
Question 2.2
Brie Basma Chabi
20109050
'''

import AVLTreeMap as mains


class WebPageIndex:
    def __init__(self, file):
        self.file = file
        self.counter = 0
        # self.formAVL(file)

    def formAVL(self, file):
        with open(file, 'r') as f:
            flat_list = [word for line in f for word in line.split()]
        r = mains.AVLTreeMap()
        root = None
        with open(file, 'r') as file1:
            for line in file1:
                for word in line.split():
                    self.counter = self.counter + 1
                    r.put(root, word, self.counter)

    def getcount(self, words):
        word_dicti = {}
        with open(self.file, 'r') as file1:
            flat_list = [word for line in file1 for word in line.split()]
            for word in flat_list:
                if word in word_dicti:
                    word_dicti[word] = word_dicti[word] + 1
                else:
                    word_dicti[word] = 1
        if words in word_dicti:
            return word_dicti[words]
        else:
            return 0


if __name__ == '__main__':
    w = WebPageIndex("data/doc1-arraylist.txt")
    print(w.getcount('or')) #Should print 1

    w = WebPageIndex("data/doc2-graph.txt")
    print(w.getcount('graph')) #Should print 9

    w = WebPageIndex("data/doc4-stack.txt")
    print(w.getcount('or')) #Should print 1