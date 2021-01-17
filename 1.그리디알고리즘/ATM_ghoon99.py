n = int(input())
arr = list(map(int,input().split()))

arr.sort()
print(sum([sum(arr[:i]) for i in range(1,n+1)]))
