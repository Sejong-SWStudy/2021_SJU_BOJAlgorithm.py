N = int(input())
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
arr = []

for i in range(N):
    a = input()
    total = 0

    for j in a:
        if j in num:
            total += int(j)

    arr.append((len(a), total, a))

arr2 = sorted(arr, key=lambda x: (x[0], x[1], x[2]))

for i in arr2:
    print(i[2])