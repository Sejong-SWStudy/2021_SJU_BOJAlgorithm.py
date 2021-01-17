n=int(input())
time=list(map(int, input().split()))
time.sort()
sum=0
for i in range(n):
  tmp=0
  for j in range(i+1):
    tmp+=time[j]
  sum+=tmp
print(sum)
