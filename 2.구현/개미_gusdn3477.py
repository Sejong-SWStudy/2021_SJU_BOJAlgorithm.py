from sys import stdin

T = int(input())

for i in range(T):

    l, n = map(int, stdin.readline().split())
    arr = []
    mid = (1 + l) / 2
    diff = 1000000

    for j in range(n):
        arr.append(int(stdin.readline()))

    arr.sort()

    for x in range(n):

        if diff > abs(mid - arr[x]):
            save = arr[x]
            diff = abs(mid - arr[x])

    print(min(save, l - save), end=' ')
    print(max(l - arr[0], arr[n - 1]))