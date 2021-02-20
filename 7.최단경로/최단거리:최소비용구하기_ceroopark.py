N=int(input())
M=int(input())
a=[[100000]*N for i in range(N)]
for i in range(N):
  for j in range(N):
    if i ==j :
      a[i][j]=0


for i in range(M):
  start, end, price=map(int, input().split())
  a[start-1][end-1]=price
  a[end-1][start-1]=price

for k in range(N):
  for i in range(N):
    for j in range(N):
      if a[i][j] > a[i][k]+a[k][j]:
        a[i][j]=a[i][k]+a[k][j]
  
    
start, end=map(int, input().split())



