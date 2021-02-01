def solution():
  # 뒤에서 부터 접근
  # 오늘이후에 가장 비싼날에 팔기 (파는날이 이미 정해짐)
  high = arr[-1]
  profit = 0
  for i in range(n-2,-1,-1): # 거꾸로 접근
    if arr[i]>high:
      high = arr[i] # high 갱신
    else:
      profit += high-arr[i] #arr[i]에 산 걸 high 에 팔기
    
  return profit

t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  print(solution())
