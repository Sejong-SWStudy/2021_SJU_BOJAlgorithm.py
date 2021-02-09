def Dfs(i,j):
  if i<0 or i>=n or j<0 or j>=n: #경계 넘으면 종료
    return
  if square_map[i][j]==1: # 갈수있으면 가기
    global cnt
    cnt += 1
    square_map[i][j]=0
    Dfs(i,j+1) # 왼
    Dfs(i,j-1) # 오
    Dfs(i+1,j) # 아래
    Dfs(i-1,j) # 위

# input
n = int(input())
square_map = []
for i in range(n):
  square_map.append(list(map(int,input())))

# solution 
house = []
cnt = 0 
for i in range(n):
  for j in range(n):
    if square_map[i][j]==1:
      Dfs(i,j)
      house.append(cnt)
      cnt = 0
      
# output
print(len(house))
house.sort()
for cnt in house:
  print(cnt)   
  
