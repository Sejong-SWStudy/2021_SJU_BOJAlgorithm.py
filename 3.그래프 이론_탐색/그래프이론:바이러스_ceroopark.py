N=int(input()) #node
M=int(input()) #edge

graph=[[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a, b=map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1	

def DFS(graph, start, node):
    for i in range(1, node+1):
        if graph[start][i] == 1 and i not in visited:
            visited.append(i)
            DFS(graph, i, node)
            
visited=[]
DFS(graph, 1, N)
print(len(visited)-1)
