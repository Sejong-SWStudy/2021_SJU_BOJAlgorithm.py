from sys import stdin

T = int(input())

for i in range(T):
    N = int(input())
    poc = []
    arr = list(map(int, stdin.readline().split()))
    arr.sort()
    ans = 0

    if N % 2 == 1:
        for j in range(0, len(arr), 2):
            poc.append(arr[j])

        for j in range(len(arr) - 2, 0, -2):
            poc.append(arr[j])

    else:
        for j in range(0, len(arr), 2):
            poc.append(arr[j])

        for j in range(len(arr) - 1, 0, -2):
            poc.append(arr[j])

    for j in range(len(poc) - 1):
        ans = max(ans, abs(poc[j + 1] - poc[j]))

    ans = max(ans, abs(poc[0] - poc[1]))
    print(ans)