n=int(input())
a=list(map(int,input().split()))

a.sort()
sum0=0
sum=0
for i in range(len(a)):
    sum0+=a[i]
    sum += sum0

print(sum)