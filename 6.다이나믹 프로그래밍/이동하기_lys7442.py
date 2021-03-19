n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)] #N*M
dp=[[0 for row in range(m)] for col in range(n)]

for y in range(n):
    for x in range(m):
        if(y==0 and x==0):
            dp[y][x]=arr[y][x]
        elif(y==0):
            dp[y][x]=arr[y][x]+dp[y][x-1]
        elif(x==0):
            dp[y][x]=arr[y][x]+dp[y-1][x]
        else:
            dp[y][x]=arr[y][x]+max(dp[y-1][x],dp[y][x-1])

print(dp[n-1][m-1])
'''
이동방향 오른쪽,아래,대각선
(1,1)~(n,m) = max[(1,1) ~(n-1,m),(n,m-1)] + (n,m)
'''


