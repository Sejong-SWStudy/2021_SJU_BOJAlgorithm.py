from sys import stdin

N, M = map(int, stdin.readline().split())
arr = []
dp = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))

dp[0][0] = arr[0][0]

for i in range(N):
    for j in range(M):

        if i == 0 and j == 0:
            continue

        elif i == 0:
            dp[i][j] = dp[i][j - 1] + arr[i][j]

        elif j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]

        else:
            dp[i][j] = max(dp[i - 1][j] + arr[i][j], dp[i][j - 1] + arr[i][j])

print(dp[N - 1][M - 1])