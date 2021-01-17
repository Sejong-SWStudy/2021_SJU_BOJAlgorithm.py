n=int(input())
sum=0

p=list(map(int, input().split()))
p.sort()

for i in range(n):
  for j in range(i+1):
    sum += p[j]

print(sum)

--------------------------------------

n = int(input())
p = list(map(int, input().split()))

p.sort() 

sum = 0 
total = 0

for i in range(N): 
    total += (sum + p[i])
    sum += p[i] 
        
print(total)
