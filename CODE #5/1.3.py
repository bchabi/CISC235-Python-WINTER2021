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

    def find_minVertex(self,visited,weights):#Finds the minimum vertex in the weights array and which is unvisited
        minVertex=-1
        for i in range(self.vertices+1):
            if visited[i]==False and (minVertex == -1 or weights[minVertex]>weights[i]):
                minVertex=i
        return minVertex

    #Function returns the total weight of all the edges in the MST formes by the prim's algorithm
    def prim(self):
        weights=[sys.maxsize for i in range(self.vertices+1)]#Stores the weights of all edges in MST
        tot_Weigh=0
        weights[0]=0#Starting with the vertex 0
        visited=[False for i in range(self.vertices+1)]
        for i in range(self.vertices):
            minVertex=self.find_minVertex(visited,weights)#Get the minimum vertex which is unvisited
            visited[minVertex]=True
            for j in range(self.vertices+1):#Exploring the neighbors and update the weights list
                if visited[j]==False and self.adjMatrix[minVertex][j]!=0 and self.adjMatrix[minVertex][j]<weights[j]:
                    weights[j]=self.adjMatrix[minVertex][j]
        for w in weights:#Summing all the edges in MST
           tot_Weigh=tot_Weigh+w
        return tot_Weigh




g=Graph(5)
print("The total weight of the edges selected in MST are",g.prim())
