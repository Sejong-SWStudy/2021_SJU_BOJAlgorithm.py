N, K=map(int, input().split())

coin=[]
for i in range(N):
    coin.append(int(input()))
cnt=0

for i in range(N-1, -1, -1):
    cnt+=K//coin[i]
    K%=coin[i]
    if K==0:
        break
print(cnt)
