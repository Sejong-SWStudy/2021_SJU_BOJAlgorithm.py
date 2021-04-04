#각 집중국의 수신 가능 영역의 길이의 합을 최소화

n=int(input()) #센서 개수
k=int(input()) #집중국 개수
sensor=list(map(int,input().split())) #센서 좌표
sensor=sorted(sensor) #좌표 정렬

if(k>n):
    print(0)
else:
    #인접 거리 구하기
    adjoin=list(map(lambda x : sensor[x]-sensor[x-1], range(1,n))) 
    #인접 거리 정렬 후 가장 먼 곳부터 K-1개 제거
    sorted_adjoin=sorted(adjoin,reverse=True)[k-1:] 
    print(sum(sorted_adjoin))

'''
K 개수의 섹션으로 나눈 뒤
그 섹션별 평균 위치에 집중국 설치
섹션을 나누는 기준: 인접한 거리가 가장 먼 곳
'''
