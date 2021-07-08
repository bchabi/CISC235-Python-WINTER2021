'''
This class implements a simple web search engine using previous classes
Question 2.4
Brie Basma Chabi
20109050
'''

import WebPageIndex as webIdx
import WebpagePriorityQueue as webPq

def readFiles(myDirectory):
    WebList = []
    for i in myDirectory:
        if i.endswith('.txt'):
            WebList.append(webIdx.WebPageIndex(i))
    return WebList

'''I wasn't able to get my main function to work however I tried my best'''
def main():
    dir_path = "data"
    w=webPq.WebpagePriorityQueue(dir_path)
    a_file = open("queries.txt")
    lines = a_file.readlines()
    #Creating the max heap for the first line query
    #Weblist is same as w.list both store the same values
    counter= 1
    for line in lines:
        print("For query No. "+str(counter))
        for itr in w.list:
            w.createMaxHeap(line,itr)
            while len(w.heapList)!=0:
                print(w.poll().file)
        counter = counter+1


main()