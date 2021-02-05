n, k = map(int, input().split())
coin = list()

for i in range(n):
    coin.append(int(input()))

cnt = 0
for i in range(n-1, -1, -1):
    unit = coin[i]
    if k//unit != 0:
        cnt += k//unit
        k = k % unit
    if k == 0:
        break;
print(cnt)

