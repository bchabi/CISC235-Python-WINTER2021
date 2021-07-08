'''
Implement the Breadth First Search algorithm, modifying it so that it randomly
chooses a start vertex, and returns the total of the weights of the edges that it
selects
'''
import sys
from random import sample,randrange

class Graph():
    def __init__(self,vertices):
        self.vertices = vertices#Initialize the number of vertices
        self.adjMatrix = [ [ 0 for i in range(vertices+1)] for j in range(vertices+1)]
        #Graph stored as an adjacency Matrix where adjMatrix[i][j]=0 if there is no connection between i and j
        #Generating the test Graph
        self.adjMatrix=[[ 0, 15, 0, 7, 10, 0],
						[ 15, 0, 9, 11, 0, 9],
						[ 0, 9, 0, 0, 12, 7 ],
						[ 7, 11, 0, 0, 8,14 ],
						[ 10, 0, 12, 8, 0, 8], 
                        [ 0, 9, 7, 14, 8, 0]  ];
    
    #Returns the total weights of the edges visited by BFS    
    def bfs(self):
        Queue=[]#Stores the vertices whose neighbours are yet to be explored
        tot_Weigh=0#Stores the total weight
        start_vertex=randrange(1,self.vertices+1)#Randomly generating the start vertex
        visited = [False]*(self.vertices+1)#Making all vertices unvisited initially
        Queue.append(start_vertex)
        visited[start_vertex]=True
        while len(Queue)!=0:
            front=Queue.pop(0)#Remove the first element of queue
            print(front,end=" ")
            for i in range(self.vertices+1):#Explore the unvisited neighbours
                if self.adjMatrix[front][i]!=0 and visited[i]==False:
                    visited[i]=True
                    tot_Weigh=tot_Weigh+self.adjMatrix[front][i]#Add to the total weight
                    Queue.append(i)
        return tot_Weigh


g=Graph(5)
print("The total of weight of the edges is ",g.bfs())