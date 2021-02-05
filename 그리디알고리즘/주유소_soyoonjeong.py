n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
minprice = price[0]
result = price[0]*road[0]
for i in range(1, n-1):
    if minprice > price[i]:
        minprice = price[i]
    result += minprice*road[i]
print(result)
