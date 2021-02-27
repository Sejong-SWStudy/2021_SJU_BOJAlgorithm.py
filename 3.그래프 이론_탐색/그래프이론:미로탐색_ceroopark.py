N, M=map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

graph=[]
for _ in range(N):
    graph.append(list(map(int, input())))

queue=[[0, 0]]#inital coordinate

graph[0][0]=1

while queue:
    a, b=queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x=a+dx[i]
        y=b+dy[i]
        if 0<=x<N and 0<=y<M and graph[x][y]==1:
            queue.append([x, y])
            graph[x][y]=graph[a][b]+1
print(graph[N-1][M-1])
        
