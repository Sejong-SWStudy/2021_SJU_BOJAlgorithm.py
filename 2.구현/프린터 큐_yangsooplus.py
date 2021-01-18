times = int(input())


for j in range(times):
    n,m = map(int, input().split())
    queue = list(map(int, input().split()))
    order = list()


    for i in range(n):
        order.append(i)

    cnt = 0

    while(True):
        max_value = max(queue)

        popped_value = queue.pop(0)
        popped_order = order.pop(0)

        if popped_value < max_value:
            queue.append(popped_value)
            order.append(popped_order)
        else:
            cnt+=1
            if popped_order == m:
                break;
    print(cnt)
