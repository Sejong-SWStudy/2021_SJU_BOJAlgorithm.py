import bisect
from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
arr2 = list(set(arr.copy()))

arr2.sort()

for i in arr:
    print(bisect.bisect_left(arr2,i),end=' ')