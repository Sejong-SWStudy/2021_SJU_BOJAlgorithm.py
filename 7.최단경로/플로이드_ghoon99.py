def find():
  for i in range(1,n+1):
    for a in range(1,n+1):
      for b in range(1,n+1):
        graph[a][b] = min(graph[a][b],graph[a][i]+graph[i][b])

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0
      
for i in range(m):
  start,end,weight = map(int,input().split())
  graph[start][end]=min(weight,graph[start][end])
    
find()
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j or graph[i][j]==INF:
      print(0,end=' ')
    else:
      print(graph[i][j],end=' ')
  print()
