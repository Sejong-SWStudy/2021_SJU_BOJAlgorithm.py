import sys

T=int(input())

for _ in range(T):
    L,n=map(int,sys.stdin.readline().rstrip().split())
    ants=[]
    for _ in range(n):
        ants.append(int(sys.stdin.readline()))
    antMin=0
    antMax=0
    for ant in ants:
        if ant > L-ant:
            if antMin < L-ant:
                antMin = L-ant
            if antMax < ant:
                antMax = ant
        else:
            if antMin < ant:
                antMin =ant
            if antMax < L-ant:
                antMax = L-ant
    print(antMin,antMax)
