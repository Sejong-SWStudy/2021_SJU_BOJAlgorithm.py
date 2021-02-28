from collections import deque
from sys import stdin


def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    arr[a][b] = '0'

    while queue:

        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if arr[dx][dy] == '1':
                arr[dx][dy] = '0'
                visited[dx][dy] = visited[x][y] + 1
                queue.append((dx, dy))


N, M = map(int, stdin.readline().split())
arr = []
visited = [[0 for i in range(M)] for j in range(N)]
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]

for i in range(N):
    arr.append(list(input()))

BFS(0, 0)
print(visited[N - 1][M - 1])