import heapq
import sys

# 기본 다익스트라 코드
def getMinNode():
  min_idx = 0
  for i in range(1,V+1):
    if not visited[i]:
      if distance[min_idx]>distance[i]:
          min_idx = i
  return min_idx


def Dijkstra(start):
  distance[start] = 0 # 시작 노드 초기화
  visited[start] = True

  for node in graph[start]: # 시작인접노드 체킹
    distance[node[0]]=node[1]
  
  for i in range(V): # 시작 노드 제외 n-1 개 
    node = getMinNode() # 이부분을 개선
    visited[node]=True
    for adjNode in graph[node]:
      if not visited[adjNode[0]]:
        distance[adjNode[0]] = min(distance[adjNode[0]],
                                 distance[node]+adjNode[1])
        
# 제출한 코드       
def fastDijkstra(start):
  q = []
  heapq.heappush(q,(0,start)) # (거리,노드번호) 우선순위큐 (최소힙 기준 tuple[0])
  distance[start] = 0 
  while q: # (isEmpty)
    crnt_dist,node = heapq.heappop(q)
    if crnt_dist > distance[node]: # 이미 처리되었으면 넘김
      continue
    
    for adjNode,weight in graph[node]: # 인접 노드 탐색
      cost = crnt_dist + weight
      if cost<distance[adjNode]: # 값이 갱신될 때만
        distance[adjNode]=cost
        heapq.heappush(q,(cost,adjNode)) # 우선순위큐에 삽입



input=sys.stdin.readline
INF = int(1e9)

V , E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
visited = [False]*(V+1)
distance =[INF]*(V+1)

for _ in range(E):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))
          
fastDijkstra(start)

for i in range(1,V+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])
