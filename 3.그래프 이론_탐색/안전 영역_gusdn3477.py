from collections import deque
from copy import deepcopy


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:

        a = queue.popleft()
        for _ in range(4):
            dx = a[0] + nx[_]
            dy = a[1] + ny[_]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if arr[dx][dy] != 0 and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy))


N = int(input())
arr2 = []
m = 100
M = 0
ct = 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]

for i in range(N):
    arr2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr2[i][j] < m:
            m = arr2[i][j]

        if arr2[i][j] > M:
            M = arr2[i][j]

for i in range(M + 1):

    tmp = 0
    arr = deepcopy(arr2)
    visited = [[0 for a in range(N)] for b in range(N)]
    for a in range(N):
        for b in range(N):
            if arr[a][b] <= i:
                arr[a][b] = 0

    for a in range(N):
        for b in range(N):
            if arr[a][b] != 0 and visited[a][b] == 0:
                BFS(a, b)
                tmp += 1

    ct = max(ct, tmp)

print(ct)