##g = Graph(6)
##g.addEdge(0, 1, -1)
##g.addEdge(1, 2, -2)
##g.addEdge(1, 3, 11)
##g.addEdge(1, 4, -1)
##g.addEdge(2, 3, 8)
##g.addEdge(3, 4, 3)
##g.addEdge(4, 5, 0)
from collections import defaultdict
import sys
 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
         
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))
        return dist[self.V-1]
     
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
 
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest 
        # path from src to any other vertex can have at-most |V| - 1 
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        # Step 3: check for negative-weight cycles.  The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.
 
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print ("Graph contains negative weight cycle")
                        return
                         
        
        return dist[self.V-1]


def raceAgainstTime(n, mh, h, p):
    g=Graph(n+1) #ans+n
    h.insert(0,mh)
    print(h)
    print(p)
    
    for i in range (len(h)):
        for j in range (i+1,len(h)):
            print("p[j-1]=",p[j-1])
            wt = abs(h[i]-h[j])+p[j-1]
            print("edge: ",i," to ",j," with wt=",wt)
            g.addEdge(i,j,wt)
            if(h[j]>h[i]):
                break
        if((j==len(h)-1) and h[i]>=h[j]):
            print("h[j]=",h[j]," j=",j) #weight=0
            print("edge: ",i," to ",j+1," with wt=0")
            g.addEdge(i,j+1,0)

    
            
    print("__________________________________________________________________________________")        
    answer = g.BellmanFord(0)
    return (answer+n)
            

            

if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    result = raceAgainstTime(n, mason_height, heights, prices)
    print("ans=",result)
