from sys import stdin
from collections import deque

n=int(stdin.readline()) #보드의 크기
k=int(stdin.readline()) #사과의 개수
apple=[list(stdin.readline().rstrip().split()) for _ in range(k)]
l=int(stdin.readline()) #방향 변환 횟수
change=[list(stdin.readline().rstrip().split()) for _ in range(l)]
boundary=[0,n+1]
directions=['r','d','l','u'] 
now_dir=0
time=0
que=deque([(1,1)]) #1,1에서 시작

while(1):
    time+=1
    pos=list(que[-1])
    #현재 방향에 따라 이동
    if(directions[now_dir]=='r'):
        pos[1]+=1
    elif(directions[now_dir]=='l'):
        pos[1]-=1
    elif(directions[now_dir]=='d'):
        pos[0]+=1
    else:
        pos[0]-=1
    #벽에 부딪힐 때
    if(pos[0] in boundary or pos[1] in boundary):
        break
    #자기 몸통에 부딪힐 때
    if pos in que:
        break
    #사과가 있음->사과 먹어서 없애기 / 없음->꼬리 제거
    for j in apple:
        if(pos[0]==int(j[0]) and pos[1]==int(j[1])):
            apple.remove(j)
            break
    else:
        que.popleft()
    que.append(pos)
    #방향 변경
    for i in change:
        if(int(i[0])==time):
            if(i[1]=='D'):
                now_dir=(now_dir+1)%4
            else:
                now_dir=(now_dir+3)%4

print(time)
