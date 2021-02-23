import sys
input=sys.stdin.readline

def solution(score,n):
  cnt = 1
  score.sort(key=lambda x:x[0])
  max_score = score[0][1]
  #print(score)

  for i in range(1,n):
      if max_score > score[i][1]:
        max_score = score[i][1]
        #print(score[i])
        cnt+=1
  return cnt

t = int(input())
for _ in range(t):
  score = []
  n = int(input())
  for _ in range(n):
    a,b = map(int,input().split())
    score.append([a,b])
  print(solution(score,n))    
