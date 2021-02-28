N = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr.sort()
arr2.sort(reverse=True)

total = 0

for i in range(len(arr)):
    total += arr[i] * arr2[i]

print(total)