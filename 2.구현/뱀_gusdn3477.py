from sys import stdin
from collections import deque

N = int(input())

nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
jido = [[0 for i in range(N + 2)] for j in range(N + 2)]
snake = deque([(1, 1)])
rotate = []
start = 0
time = 0

K = int(input())
for i in range(K):
    a, b = map(int, stdin.readline().split())
    jido[a][b] = 1

L = int(input())
for i in range(L):
    a, b = stdin.readline().rstrip().split()
    rotate.append((int(a), b))

while True:

    x = snake[-1][0]
    y = snake[-1][1]

    x += nx[start % 4]
    y += ny[start % 4]

    time += 1

    if (x, y) in snake or x < 1 or x > N or y < 1 or y > N:
        break

    if jido[y][x] == 1:
        jido[y][x] = 0
        snake.append((x, y))

    else:
        snake.popleft()
        snake.append((x, y))

    for i in range(len(rotate)):
        if time == rotate[i][0]:
            if rotate[i][1] == 'L':
                start -= 1

            elif rotate[i][1] == 'D':
                start += 1

print(time)