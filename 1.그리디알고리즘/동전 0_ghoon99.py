# input
n , k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

#solution
result = 0
for i in range(n-1,-1,-1): # 거꾸로
  cnt = k//coins[i] # 몫 구하기 

  if cnt != 0:
    result += cnt # 동전 개수 추가
    k -= cnt * coins[i] # 금액 덜어내기
    
  if k == 0: # 조기 중단 
    break

#output
print(result)
