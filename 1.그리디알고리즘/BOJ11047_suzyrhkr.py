#BOJ 11047번

n, k = list(map(int, input().split()))
arr = [int(input()) for i in range(n)]
arr.sort(reverse=True)
i, cnt = 0, 0

while k!=0:
  if (arr[i] <= k):
    num = k//arr[i]
    k = k - num * arr[i]
    cnt += num
  i+=1

print(cnt)
