
import sys
from random import sample,randrange


class Graph():
    #Generates a random graph
    def __init__(self,vertices): 
        self.vertices = vertices#Initialize the number of vertices
        self.adjMatrix = [ [ 0 for i in range(vertices+1)] for j in range(vertices+1)]
        #Graph stored as an adjacency Matrix where adjMatrix[i][j]=0 if there is no connection between i and j
        for i in range(2,vertices+1):
            if i==2:
                x=randrange(1,2)
                S=sample(range(1, i), x)
            else:
                x=randrange(1,i-1)#Generating random integers in the range
                S=sample(range(1, i-1), x)#Getting the random sample of x values
            for s in S:
                w=randrange(10,100)#Randomly generating a weight in a range
                self.adjMatrix[i][s]=w#Adding edge between i and s
                self.adjMatrix[s][i]=w#Adding edge between s and i


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
            for i in range(self.vertices+1):#Explore the unvisited neighbours
                if self.adjMatrix[front][i]!=0 and visited[i]==False:
                    visited[i]=True
                    tot_Weigh=tot_Weigh+self.adjMatrix[front][i]#Add to the total weight
                    Queue.append(i)
        return tot_Weigh


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
        weights[1]=0#Starting with the vertex 0
        visited=[False for i in range(self.vertices+1)]
        for i in range(self.vertices):
            minVertex=self.find_minVertex(visited,weights)#Get the minimum vertex which is unvisited
            visited[minVertex]=True
            for j in range(self.vertices+1):#Exploring the neighbors and update the weights list
                if visited[j]==False and self.adjMatrix[minVertex][j]!=0 and self.adjMatrix[minVertex][j]<weights[j]:
                    weights[j]=self.adjMatrix[minVertex][j]
        for ele in range(1,len(weights)):#Summing all the edges in MST 
           tot_Weigh=tot_Weigh+weights[ele]
        return tot_Weigh

    @staticmethod
    def compareBfsPrim():#Function compares the BFS and prims spanning tree by finding the average
        #of the total weight of vertex of different number of nodes
        n=[20,40,60]#n stores the number of vertices in different random graphs
        k=int(input("Enter a number \n"))
        for j in n:
            sum=0#Stores the sum for finding the average
            for i in range(k):
                g=Graph(j)#generate graph with n nodes
                B=g.bfs()
                P=g.prim()
                Diff=((B-P)/P)*100#Finding the percent of difference
                sum=sum+Diff
            avg=sum/k#Getting the average
            print("The average for",j,"is",avg)






Graph.compareBfsPrim()