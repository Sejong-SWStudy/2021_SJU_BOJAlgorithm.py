def binary_search():
    global total_cnt
    start = 1
    end = arr[-1]  # arr의 최댓값

    while start <= end:

        mid = (start + end) // 2
        total = 0

        for i in arr:

            if i <= mid:
                total += i

            else:
                total += mid

        if total <= M:  # 예산보다 작거나 같은 경우, mid를 늘려야 한다.
            start = mid + 1
            total_cnt = max(total_cnt, mid)

        else:  # 예산보다 큰 경우, mid를 줄인다.
            end = mid - 1


N = int(input())
total_cnt = 0  # 최소 금액

arr = list(map(int, input().split()))

M = int(input())
arr.sort()
binary_search()
print(total_cnt)