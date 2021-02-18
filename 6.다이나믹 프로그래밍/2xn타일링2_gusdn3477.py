N = int(input())
dp = [0] * (N + 5)  # 조금 넉넉하게 리스트의 사이즈를 잡아봤습니다.

dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = dp[i - 1] % 10007 + dp[i - 2] * 2 % 10007

print(dp[N] % 10007)