

import heapq
from collections import deque

def solution(n,m,arr):
  heap = []
  new_arr = deque()
  for idx,i in enumerate(arr):
    heapq.heappush(heap,(-i,i)) # 최대 힙 생성
    new_arr.append((idx,i)) # 순서있는 배열 생성 (인덱스,원소)
  
  # 찾고자 하는 위치
  target = (m,arr[m])

  cnt = 1 
  while True:
    if heap[0][1]>new_arr[0][1]:  # 현재 제일 최대값(우선순위 최대)과 비교
      new_arr.append(new_arr.popleft()) # 아니면 맨뒤로 다시 줄서
    else:  # 우선 순위가 최대임
      if target == new_arr[0]: #내가 찾는 값이면 
        return cnt # 값 반환
      heapq.heappop(heap) # 최대값 삭제 -> 2번째로 큰 값이 맨위로 온다.
      new_arr.popleft() #프린트 했으므로 삭제
      cnt+=1 # 1번 프린트함 

  return cnt
    

case = int(input())

for i in range(case):
  n,m = map(int,input().split())
  arr = list(map(int,input().split()))
  print(solution(n,m,arr))
