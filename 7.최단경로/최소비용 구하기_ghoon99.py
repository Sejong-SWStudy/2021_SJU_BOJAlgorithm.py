import heapq

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

n = int(input())
m = int(input())
import sys
input=sys.stdin.readline
INF = int(1e9)

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance =[INF]*(n+1)

for _ in range(m):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))

start , end = map(int,input().split())

fastDijkstra(start)
print(distance[end])
