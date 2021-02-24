import sys
input=sys.stdin.readline
def solution(arr,l,n):
  arr.sort()
  min_t = []
  for i in range(n):
    min_t.append(min(arr[i],l-arr[i]))
  
  return max(min_t),max(arr[-1],l-arr[0])

t = int(input())
for i in range(t):
  l,n = map(int,input().split())
  arr=[int(input()) for _ in range(n)]
  min_t,max_t = solution(arr,l,n)
  print(min_t,max_t)
