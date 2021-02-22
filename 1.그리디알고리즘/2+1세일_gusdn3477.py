from sys import stdin

N = int(input())
arr = []

for i in range(N):
    arr.append(int(stdin.readline()))

arr.sort(reverse=True)  # 가격이 큰 것부터 처리해야 이득이다.
total = 0
ct = 0

for i in arr:
    ct += 1

    if ct % 3 == 0:  # 세 번째 요소인 경우 넘어감.
        ct = 0
        continue

    total += i

print(total)