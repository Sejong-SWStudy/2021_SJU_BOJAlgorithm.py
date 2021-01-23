#BFS를 이용한 풀이

from collections import deque

# 좌, 좌상, 상, 우상, 우, 우하, 하, 좌하 탐색을 위한 리스트
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

while True:
  w, h = map(int, input().split())
  #종료 조건
  if w==0 and h==0:
    break

  island = [list(map(int, input().split())) for _ in range(h)]
  queue = deque()
  count=0

  for i in range(h):
    for j in range(w):
      #땅일 경우
      if island[i][j]==1:
        queue.append((i,j))
        island[i][j]='visited'

        while queue:
          pop_x, pop_y = queue.popleft()
          # 주변 모두 탐색
          for t in range(len(dx)):
            x = pop_x + dx[t]
            y = pop_y + dy[t]
            # 주변 값이 'island' 배열 범위 안에 있을 경우만 탐색
            if 0<=x<h and 0<=y<w:
               if island[x][y] == 1:
                  queue.append((x,y))
                  island[x][y] = 'visited'
        #바다일 경우
        else:
           count+=1
  print(count)
