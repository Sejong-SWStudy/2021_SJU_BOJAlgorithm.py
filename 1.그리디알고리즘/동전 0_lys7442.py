import sys
n,k = map(int,sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for i in range(n)]
a.sort(reverse=True)
cnt=0

for i in a:
    while(i<=k):
        k-=i
        cnt+=1
    if(k==0):
        break
print(cnt)