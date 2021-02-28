N=int(input())

A=list(map(int, input().split()))
B=list(map(int, input().split()))


A.sort()
B.sort(reverse=True)
Sum=0
for i in range(N):
    Sum+=A[i]*B[i]
print(Sum)
