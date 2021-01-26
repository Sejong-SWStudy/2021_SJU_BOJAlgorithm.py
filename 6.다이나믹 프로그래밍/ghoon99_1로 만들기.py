n = int(input())
dp = [0]*10**7

# bottom up 방식 
for i in range(2,n+1):
  dp[i] = dp[i-1] + 1 # 2일때 횟수 1번 1을 빼는연산
  
  if i%2 == 0: 
    dp[i] = min(dp[i],dp[i//2]+1) # 2로 나눠떨어질때 비교
  if i%3 ==0: 
    dp[i] = min(dp[i],dp[i//3]+1)

print(dp[n])
