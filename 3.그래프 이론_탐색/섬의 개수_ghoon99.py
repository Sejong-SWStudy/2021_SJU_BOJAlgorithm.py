import sys
sys.setrecursionlimit(10**6)

def DFS(graph,w,h,i,j):
  # bound 
  if i>h or i<0 or j<0 or j>w:
    return
  #
  if graph[i][j]==1:
    graph[i][j] = 0

    DFS(graph,w,h,i+1,j) #위
    DFS(graph,w,h,i,j+1) #아래
    DFS(graph,w,h,i-1,j) #오
    DFS(graph,w,h,i,j-1) #왼

    DFS(graph,w,h,i+1,j+1) # 대각위
    DFS(graph,w,h,i+1,j-1) # 대각 아래
    DFS(graph,w,h,i-1,j+1) # 대각위
    DFS(graph,w,h,i-1,j-1) # 대각 아래
  


while True:
  graph = []
  cnt = 0 
  w , h = map(int,input().split())
  if w == 0 and h==0:
    break

  for i in range(h):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
  
  for i in range(h):
    for j in range(w):
      if graph[i][j]==1:
        DFS(graph,w-1,h-1,i,j)
        cnt+=1 
  print(cnt)
