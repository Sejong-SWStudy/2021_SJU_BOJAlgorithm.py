N = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]  # 일단 첫 번째 요소가 가장 작다고 생각합니다.
total_cost = 0  # 정답이 담길 변수를 0으로 초기화 합니다.
total_cost += cost[0] * length[0]  # 첫 단계에선, 일단 다음 단계까지 가는 양 만큼만 충전합니다.

for i in range(1, len(cost) - 1):

    if min_cost < cost[i]:  # min_cost보다 현재 주유소가 비싸면, min_cost에서 가야 할 거리를 곱하여 더합니다.(즉, 싼 주유소에서 더 충전했다고 생각하시면 됩니다.)
        total_cost += min_cost * length[i]

    else:  # 그게 아니라면, 최소 충전 가격을 현재 주유소의 가격으로 업데이트 시킨 다음, 가야 할 거리만큼 곱하여 더해 줍니다.
        min_cost = cost[i]
        total_cost += min_cost * length[i]

print(total_cost)