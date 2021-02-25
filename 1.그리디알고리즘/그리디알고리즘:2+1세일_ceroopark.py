N=int(input())


arr=[]
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
Sum=0
for i in range(0, N):
    if i%3!=2:
        Sum+=arr[i]
print(Sum)
