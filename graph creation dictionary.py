graph={}
def deletegraph():
    graph = {}

def creategraph():
    n,m = map(int,input().split())
    for j in range(1,n+1):
        graph[j] = 0
    for j in range(m):
        a,b = map(int,input().split())
        if graph[a] == 0:
            graph[a] = [b]
        else:
            arr=graph[a]+[b]
            graph[a] = arr
        if graph[b] == 0:
            graph[b] = [a]
        else:
            arr=graph[b]+[a]
            graph[b] = arr
    print(graph)


