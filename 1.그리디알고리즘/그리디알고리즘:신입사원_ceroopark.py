import sys

T=int(input())

for _ in range(T):
    cnt=1
    people=[]
    N=int(input())
    for _ in range(N):
        paper, interview=map(int, sys.stdin.readline().split())
        people.append([paper, interview])
    people.sort()
    compare=people[0][1]
    for i in range(1, N):
        if compare>people[i][1]:
            cnt+=1
            compare=people[i][1]
    print(cnt)
