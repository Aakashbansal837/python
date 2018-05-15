graph={}
def deletegraph():
    graph = {}

def creategraph(n,m):
    for j in range(1,n+1):
        graph[j] = 0
    for j in range(m):
        a,b = map(int,input().strip().split(" "))
        if graph[a] == 0:
            graph[a] = [b]
        else:
            arr = graph[a]
            if b in arr:
                continue
            graph[a] = arr[:]+[b]
        if graph[b] == 0:
            graph[b] = [a]
        else:
            arr = graph[b]
            if a in arr:
                continue
            graph[b] = arr[:]+[a]
    #print("graph is:",graph)


def bfs_connected_component(graph, start):
    queue = [start]

    levels = {}         
    levels[start]= 0    

    visited= [start]    
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                levels[neighbour]= levels[node]+6

    #print(levels)
    return levels

r = int(input())
for i in range(r):
    n,m = map(int,input().split())
    creategraph(n,m)
    start = int(input())
    ans = bfs_connected_component(graph,start)
    for j in range(1,n+1):
        if j != start:
            if j in ans:
                print(ans[j],end=" ")
            else:
                print(-1,end=" ")
    #print(ans)
    deletegraph()
    print()
