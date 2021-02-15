from sys import stdin
n=int(stdin.readline())
house=list(map(int,stdin.readline().split()))
house=sorted(house)
median=(n+1)//2
print(house[median-1])

