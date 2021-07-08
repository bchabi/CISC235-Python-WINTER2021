'''
Create a Graph class (and a vertex class if needed). Your graph class should have
an initialization function to create a random connected graph with a specified
number of vertices, and random weights on all the edges, such that the edgeweights all come from a specified range of integers.
'''
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


g=Graph(3)
print(g.adjMatrix)

