n = int(input())
ans = set(map(int,input().split()))
N = int(input())
qu = list(map(int,input().split()))

for i in range(N):
    if qu[i] in ans:
        print(1, end=' ')
    else:
        print(0,end=' ')

