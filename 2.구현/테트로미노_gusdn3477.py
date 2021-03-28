def isTrue(a, x, y):
    global N, M

    for k in range(len(a)):
        dx = x + a[k][0]
        dy = y + a[k][1]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            return False

    return True


def Total(a, x, y):
    global N, M
    total = 0

    for k in range(len(a)):
        dx = x + a[k][0]
        dy = y + a[k][1]
        total += arr[dx][dy]

    return total


N, M = map(int, input().split())
arr = []
poly1 = [[0, 0], [0, 1], [0, 2], [0, 3]]
poly1_2 = [[0, 0], [1, 0], [2, 0], [3, 0]]
poly2 = [[0, 0], [0, 1], [1, 0], [1, 1]]
poly3 = [[0, 0], [1, 0], [2, 0], [2, 1]]
poly3_2 = [[0, 0], [1, 0], [0, 1], [0, 2]]
poly3_3 = [[0, 0], [0, 1], [1, 1], [2, 1]]
poly3_4 = [[0, 0], [0, 1], [0, 2], [-1, 2]]
poly3_5 = [[0, 0], [0, 1], [-1, 1], [-2, 1]]
poly3_6 = [[0, 0], [1, 0], [1, 1], [1, 2]]
poly3_7 = [[0, 0], [1, 0], [2, 0], [0, 1]]
poly3_8 = [[0, 0], [0, 1], [0, 2], [1, 2]]
poly4 = [[0, 0], [1, 0], [1, 1], [2, 1]]
poly4_2 = [[0, 0], [0, 1], [-1, 1], [-1, 2]]
poly4_3 = [[0, 0], [1, 0], [0, 1], [-1, 1]]
poly4_4 = [[0, 0], [0, 1], [1, 1], [1, 2]]
poly5 = [[0, 0], [0, 1], [0, 2], [1, 1]]
poly5_2 = [[0, 0], [0, 1], [-1, 1], [1, 1]]
poly5_3 = [[0, 0], [0, 1], [-1, 1], [0, 2]]
poly5_4 = [[0, 0], [1, 0], [2, 0], [1, 1]]

max_sum = 0
total = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):

        if isTrue(poly1, i, j):
            total = Total(poly1, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly1_2, i, j):
            total = Total(poly1_2, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly2, i, j):
            total = Total(poly2, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3, i, j):
            total = Total(poly3, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_2, i, j):
            total = Total(poly3_2, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_3, i, j):
            total = Total(poly3_3, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_4, i, j):
            total = Total(poly3_4, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_5, i, j):
            total = Total(poly3_5, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_6, i, j):
            total = Total(poly3_6, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_7, i, j):
            total = Total(poly3_7, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly3_8, i, j):
            total = Total(poly3_8, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly4, i, j):
            total = Total(poly4, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly4_2, i, j):
            total = Total(poly4_2, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly4_3, i, j):
            total = Total(poly4_3, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly4_4, i, j):
            total = Total(poly4_4, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly5, i, j):
            total = Total(poly5, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly5_2, i, j):
            total = Total(poly5_2, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly5_3, i, j):
            total = Total(poly5_3, i, j)
            max_sum = max(max_sum, total)

        if isTrue(poly5_4, i, j):
            total = Total(poly5_4, i, j)
            max_sum = max(max_sum, total)

print(max_sum)