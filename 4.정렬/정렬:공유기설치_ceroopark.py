N, M=map(int, input().split())

house=[]
for i in range(N):
    house.append(int(input()))
    
house=sorted(house)

start=1
end=house[N-1]-house[0]

while start<=end:
    mid=(start+end)//2

    cnt=1
    base=house[0]
    for i in range(1, N):
        if house[i]-base>=mid:
            cnt+=1
            base=house[i]
    if cnt>=M:
        start=mid+1
        ans=mid
    else:
        end=mid-1

print(ans)
