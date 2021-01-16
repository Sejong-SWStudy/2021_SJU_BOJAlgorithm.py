n=int(input())
sum=0

p=list(map(int, input().split()))
p.sort()

for i in range(n):
  for j in range(i+1):
    sum += p[j]

print(sum)
