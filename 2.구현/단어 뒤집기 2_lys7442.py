from collections import deque
S=input()
tag=0
dq=deque()
for i in S:
    if(i=='<'):
        while(len(dq)>0):
            print(dq.pop(),end="")
        print(i,end="")
        tag=1
    elif(i=='>'):
        while(len(dq)>0):
            print(dq.popleft(),end="")
        print(i,end="")
        tag=0
    elif(i==' 'and tag==0):
        while(len(dq)>0):
            print(dq.pop(),end="")
        print(i,end="")
    else:
        dq.append(i)
while(len(dq)>0):
    print(dq.pop(),end="")
        
