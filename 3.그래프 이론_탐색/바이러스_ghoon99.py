def Dfs(v):
  global cnt
  cnt += 1
  visited[v] = True
  for node in graph[v]:
    if not visited[node]:
      Dfs(node)
      
from collections import deque
def Bfs(v):
  cnt = 0 
  visited[v] = True
  queue = deque([v])
  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        cnt += 1
  return cnt 

# input

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
  start,end = map(int,input().split())
  graph[start].append(end)
  graph[end].append(start)

# solution
# cnt = -1 
# Dfs(1)
cnt = Bfs(1)
print(cnt)
