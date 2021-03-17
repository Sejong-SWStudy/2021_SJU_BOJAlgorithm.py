N = int(input())
arr = list(map(int, input().split()))
ans = 2000000001
i, j = 0, len(arr) - 1
a, b = i, j

while i < j:

    if arr[i] + arr[j] < 0:
        # 코드
        if abs(arr[i] + arr[j]) < ans:
            ans = abs(arr[i] + arr[j])
            a, b = arr[i], arr[j]

        i += 1

    elif arr[i] + arr[j] > 0:
        # 코드        
        if abs(arr[i] + arr[j]) < ans:
            ans = abs(arr[i] + arr[j])
            a, b = arr[i], arr[j]

        j -= 1

    else:
        a, b = arr[i], arr[j]
        break

print(a, b)