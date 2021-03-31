T=int(input())


for _ in range(T):
    N=int(input())
    arr=list(map(int, input().split()))
    arr.sort()
    max_arr=0
    for j in range(2, N):
        max_arr=max(max_arr, arr[j]-arr[j-2])
    print(max_arr)
            
        
