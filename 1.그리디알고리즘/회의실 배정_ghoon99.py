import sys
input = sys.stdin.readline

n =int(input())
arr =[]
for _ in range(n):
  start,end = map(int,input().split())
  arr.append([start,end,end-start])



arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

cnt = 1
start = arr[0][0]
end = arr[0][1]

#print(arr)
for i in range(1,n):
  if arr[i][0]>=end:
    end = arr[i][1]
    cnt+=1

print(cnt)
