import sys
n=int(sys.stdin.readline()) #도시 개수
distance=list(map(int,sys.stdin.readline().split())) #거리
price=list(map(int,sys.stdin.readline().split())) #비용

lowprice=price[0] #첫 도시의 비용
priceSum=0
for i in range(n-1):
    #더 저렴한  비용이 발생할 때만 갱신
    lowprice=min(lowprice,price[i])
    priceSum+=lowprice*distance[i]

print(priceSum)

