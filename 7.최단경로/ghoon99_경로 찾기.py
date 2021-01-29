def find():
  for i in range(n):
    for a in range(n):
      for b in range(n):
        graph[a][b] = max(graph[a][i] and graph[i][b],graph[a][b])

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))

find()

for i in range(n):
  for j in range(n):
    print(graph[i][j],end=' ')
  print()
