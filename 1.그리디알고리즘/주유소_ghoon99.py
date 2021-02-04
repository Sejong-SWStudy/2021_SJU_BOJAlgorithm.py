# input 
n =int(input())
dist =list(map(int,input().split()))
price = list(map(int,input().split()))
# solution 
result = 0

# 딱 맞춰서 이동하다가 젤 싼곳에서 끝까지 가기 x
# -> 젤싼 곳 까지 가는 곳을 최적화 해야됨

tmp_min = price[0] # 임시 최소값 초기화

for pos in range(n-1):
  if price[pos]<tmp_min: # 최소값 갱신
    tmp_min = price[pos]
    result += tmp_min*dist[pos] # dist 다 더해서 한번에 곱하려 했으나 그냥 그때 그때 곱해도 됨 (2*(1+2+3)= 2*1+2*2...)
  else:
    result += tmp_min*dist[pos] #최소 값으로 주유

# output
print(result)
