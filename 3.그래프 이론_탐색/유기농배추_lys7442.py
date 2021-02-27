from sys import stdin
from collections import deque
t=int(stdin.readline()) # Test Case

for test in range(t):
    m,n,k=map(int,stdin.readline().split()) #가로길이,세로길이,배추개수
    arr=[[0 for row in range(m+2)] for col in range(n+2)] #밭
    for _ in range(k):
        x,y=map(int,stdin.readline().split()) #각 배추 위치  
        arr[y+1][x+1]=1

    cnt=0 #필요한 지렁이 수
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(arr[i][j]==1):
                que=deque([(j,i)])
                arr[i][j]=2 #is visited
                while(que):
                    x,y=que.popleft()
                    if(arr[y-1][x]==1):
                        que.append((x,y-1))
                        arr[y-1][x]=2
                    if(arr[y+1][x]==1):
                        que.append((x,y+1))
                        arr[y+1][x]=2
                    if(arr[y][x-1]==1):
                        que.append((x-1,y))
                        arr[y][x-1]=2
                    if(arr[y][x+1]==1):
                        que.append((x+1,y))
                        arr[y][x+1]=2
                cnt+=1
    #for k in range(n+2):
        #print(arr[k])
    print(cnt)
