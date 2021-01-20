def DFS(v):
  print(v,end=' ')
  visited[v] = True
  for i in adjList[v]:
    if not visited[i]:
      DFS(i)


from collections import deque
def BFS(v):
  visited[v]=True
  queue = deque([v])

  while len(queue)!=0:
    node = queue.popleft()
    print(node,end=' ')
    for i in adjList[node]:
      if not visited[i]:
        visited[i]=True
        queue.append(i)
        
n,m,v = map(int,input().split())
adjList = [[]*i for i in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  v1 , v2  = map(int,input().split())
  adjList[v1].append(v2)
  adjList[v2].append(v1)

adjList = list(map(sorted,adjList))
#print(adjList)
DFS(v)
print()
visited = [False]*(n+1)
BFS(v)
