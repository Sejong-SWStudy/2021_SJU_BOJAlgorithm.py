import sys
input = sys.stdin.readline
n, h = map(int, input().rstrip().split())
arr=[int(input()) for i in range(n)] #장애물 크기

#장애물 홀수/짝수 분리, 테이블 생성
even=[0]*(h)
odd=[0]*(h)
for i in range(n):
    if(i%2==0):
        even[arr[i]-1]+=1
    else:
        odd[arr[i]-1]+=1
        
#누적 테이블 생성-길이가 짧은 장애물로 값이 누적되도록

for i in range(h-2,-1,-1):
    odd[i]+=odd[i+1]
    even[i]+=even[i+1]

# 파괴 장애물 카운트 및 최솟값 출력
answer=[]
cnt=0
for i in range(h):
    #짝수 테이블은 뒤집어서 계산
    answer.append(even[h-1-i]+odd[i])
Min=min(answer)
for i in answer:
    if(i==Min):
        cnt+=1
print(Min,cnt)
