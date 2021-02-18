import sys

N=int(input())
d=[0]*(N+1)

def dp(x):
    if x==1:
        return 1
    if x==2:
        return 3
    if d[x]!=0:
        return d[x]
    d[x]=(dp(x-1) + 2*dp(x-2))%10007
    return d[x]

sys.setrecursionlimit(10000)
print(dp(N))

