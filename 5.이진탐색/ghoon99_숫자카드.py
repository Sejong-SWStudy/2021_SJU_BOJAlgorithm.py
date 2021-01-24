def bSearch(key,arr,start,end):
  if start>end:
    return False
  mid = (start+end)//2
  if key>arr[mid]:
    return bSearch(key,arr,mid+1,end)
  elif key<arr[mid]:
    return bSearch(key,arr,start,mid-1)
  else:
    return True
  

n = int(input())
ans = list(map(int,input().split()))
m = int(input())
arr = list(map(int,input().split()))

ans.sort()

for data in arr:
  if bSearch(data,ans,0,n-1):
    print(1,end=' ')
  else:
    print(0,end=' ')
