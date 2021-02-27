import sys
sys.setrecursionlimit(100000)

def DFS(x, y):
    if x<0 or x>M-1 or y<0 or y>N-1:
        return False
 
    if G[x][y]==1:
        G[x][y]=0
 
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
 
    return False
 
T=int(input())
 
for _ in range(T):
    M, N, K=map(int, input().split())
    G=[[0]*N for _ in range(M)]
    for _ in range(K):
        X, Y=map(int, input().split())
        G[X][Y]=1
 
    num=0
 
    for i in range(M):
        for j in range(N):
            if DFS(i, j)==True:
                num+=1
    print(num)
