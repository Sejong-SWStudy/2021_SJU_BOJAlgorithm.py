import sys
 
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
INF=sys.maxsize
G=[[INF for _ in range(n+1)] for _ in range(n+1)]
 
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    G[a][b]=min(c,G[a][b])
 
 
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                G[i][j]=0
            else:
                G[i][j]=min(G[i][j],G[i][k]+G[k][j])
 
for i in range(1,n+1):
    for j in range(1,n+1):
        if G[i][j]==INF:
           print(0,end=" ")
        else:
           print(G[i][j],end=" ")
    print()
