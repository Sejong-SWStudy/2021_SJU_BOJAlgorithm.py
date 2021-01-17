n = int(input())
line = list(map(int, input().split()))
cost_time = [0]*n

line.sort()

cost_time[0] = line[0]

for i in range(1,n):
    cost_time[i] = cost_time[i-1] + line[i]

print(sum(cost_time))
