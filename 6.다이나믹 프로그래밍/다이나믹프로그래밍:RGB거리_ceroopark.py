N=int(input())

a=[]

for _ in range(N):
    a.append(list(map(int, input().split())))

              
for i in range(1, N):
    a[i][0]+=min(a[i-1][1], a[i-1][2])
    a[i][1]+=min(a[i-1][0], a[i-1][2])
    a[i][2]+=min(a[i-1][0], a[i-1][1])


print(min(a[N-1][0],a[N-1][1],a[N-1][2]))
