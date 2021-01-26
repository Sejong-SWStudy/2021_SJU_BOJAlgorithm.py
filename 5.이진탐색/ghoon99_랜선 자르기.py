def solution(arr,n):
  start = 1
  end = max(arr)
  result = 0
  # 탐색

  while start<=end:
    cnt = 0
    mid = (start+end)//2
    for i in arr:
        cnt += i // mid
      
    if cnt >= n : # n 개 이상만들엇으면  
          start = mid + 1 # 더 길게
    else:
      end = mid - 1 # 짧게 가자

  return end

k,n = map(int,input().split())

arr=[]
for i in range(k):
  tmp = int(input())
  arr.append(tmp)
print(solution(arr,n))
