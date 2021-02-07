def DFS(x):
    visited[x] = 1

    for i in range(1, N + 1):
        if arr[x][i] == 1 and visited[i] == 0:
            DFS(i)


N = int(input())
arr = [[0 for i in range(N + 1)] for j in range(N + 1)]
M = int(input())
visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

DFS(1)
print(visited.count(1) - 1)  # 1번 컴퓨터 본인 빼고 카운트