from collections import deque

def score(arr):
  result = 0
  for i in range(4):
    if arr[i][0]==1:
      result += 2**i

  return result


def rotate_arr(arr,num,dir):
  # 인덱스 2번 ,6번 주목
  # 0번 , 3번 톱니에는 왼쪽,오른쪽이 없음
  

  # 먼저 회전전 체크 
   # 왼쪽 체크
  left = num -1
  r_dir = dir * -1  # 반대로 돌아가야지
  rotate_list = []

  while left>=0: # 왼쪽 끝까지
    if arr[left][2]!=arr[left+1][6]: # 다르면 회전
      rotate_list.append((left,r_dir)) # 회전 대기 목록에 추가
      r_dir *= -1 # 방향전환 
      left -=1
    else:
      break

      
  # 오른쪽 체크
  right = num + 1
  r_dir = dir * -1

  while right<=3: # 오른쪽 끝까지
    if arr[right][6]!=arr[right-1][2]: # 다르면 회전
      rotate_list.append((right,r_dir))

      r_dir *= -1 # 방향전환
      right +=1
    else:
      break

  #회전  
  arr[num].rotate(dir)

  for idx,c_dir in rotate_list:
    arr[idx].rotate(c_dir)

  return arr


arr = []

for _ in range(4):
  tmp = list(map(int,input()))
  arr.append(deque(tmp))

k = int(input())

for _ in range(k):
  num,dir = map(int,input().split())
  arr = rotate_arr(arr,num-1,dir)
  print(arr)
  
print(score(arr))

