#인접 리스트와 재귀함수를 이용한 풀이
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
queue = []
visited = [False]*(n+1)

def dfs(v):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if visited[i]==False:
      dfs(i)

def bfs(v):
  queue.append(v)
  visited[v] = True
  while queue:
    v = queue.pop(0)
    print(v, end=' ')
    for i in graph[v]:
      if visited[i]==False:
        queue.append(i)
        visited[i]=True

for i in range(m):
  node_a, node_b = map(int, input().split())
  graph[node_a].append(node_b)
  graph[node_b].append(node_a)
  graph[node_a].sort()
  graph[node_b].sort()

dfs(v)
visited = [False]*(n+1)
print()
bfs(v)
