n =int(input())
house = list(map(int,input().split()))

house.sort() # 집 순서대로 정렬
# 제일 몰려있는곳 -> 중앙
print(house[len(house)//2-1])
