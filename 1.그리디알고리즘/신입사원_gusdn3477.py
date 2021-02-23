from sys import stdin

T = int(input())

for i in range(T):
    N = int(input())
    arr = []

    for j in range(N):
        arr.append(list(map(int, stdin.readline().split())))

    arr.sort()
    start = arr[0][1]
    ct = 1

    for x in range(1, len(arr)):

        if arr[x][1] > start:  # 기준자의 면접 등수보다 큰 경우(즉, 둘다 높은 경우)
            continue

        else:  # 기준자의 면접 등수보다 작은 경우(어차피 같은 등수는 없으므로 else)
            start = arr[x][1]
            ct += 1

    print(ct)