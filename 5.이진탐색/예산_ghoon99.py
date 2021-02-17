def solution(): # m => key
  start = 0
  end = arr[-1]
  while start<=end:
    tmp = 0 
    mid = (start+end)//2

    for data in arr:
      tmp += min(data,mid)
    
    if tmp<=m: # 예산 남아버림
      start = mid+1
    elif tmp>m: # 예산 넘겨버림
      end = mid-1
    #print(start,end)
  return end

# input
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr.sort()  

# output
answer = solution()
print(answer)
