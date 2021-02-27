import sys

sys.setrecursionlimit(4000)


def DFS(x, y):
    arr[x][y] = 0

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue

        if arr[dx][dy] == 1:
            DFS(dx, dy)


T = int(input())
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
ct = 0

for i in range(T):

    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0 for i in range(M)] for j in range(N)]
    ct = 0

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    for a in range(N):
        for b in range(M):
            if arr[a][b] == 1:
                DFS(a, b)
                ct += 1

    print(ct)