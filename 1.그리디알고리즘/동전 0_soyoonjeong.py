n, k = map(int, input().split())
arr = [0]*n
money = 0
for i in range(0, n):
    arr[i] = int(input())
for i in range(n-1, -1, -1):
    if arr[i] <= k:
        money += k//arr[i]
        k -= (k//arr[i])*arr[i]
    if k==0:
        break
print(money)
