n,k=map(int,input().split())
belt=list(map(int,input().split()))
robot=[0]*(2*n)
count=0
up=0
down=n-1
while(True):
    count+=1
    #벨트 한칸 회전
    up=(up-1+(2*n))%(2*n)
    down=(up+(n-1))%(2*n)
    #내릴 칸에 로봇 있으면
    if(robot[down]==1): 
        robot[down]=0
    #로봇 이동
    for i in range(down-1,down-n,-1):
        if(robot[i%(2*n)]==1 and robot[(i+1)%(2*n)]==0 and belt[(i+1)%(2*n)]!=0):
            robot[(i+1)%(2*n)],robot[i%(2*n)]=1,0
            belt[(i+1)%(2*n)]-=1
    #올라갈 칸에 로봇 없고 내구도 남아있음
    if(robot[up]==0 and belt[up]!=0):
        robot[up]=1
        belt[up]-=1
    #내릴 칸에 로봇 있으면
    if(robot[down]==1): 
        robot[down]=0
    '''#출력
    for i in range(up,up+2*n):
        print(belt[i%(2*n)],end=" ")
    print("")
    for i in range(up,up+2*n):
        print(robot[i%(2*n)],end=" ")
    print("")'''
    #종료조건
    du=0
    for i in belt:
        if(i==0):
            du+=1
    if(du>=k):
        break

print(count)
