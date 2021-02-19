import sys
input=sys.stdin.readline

n=int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int,input().split())))

dp = [[arr[0][0],arr[0][1],arr[0][2]] for _ in range(1002)]
for i in range(1,n):
  dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])
  dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])
  dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])

print(min(dp[n-1]))

