N=int(input())
budget=list(map(int, input().split()))
M=int(input())

budget=sorted(budget)

start=1
end=budget[-1]

total=sum(budget)

if total<=M:
    ans=end #max
else:
    while start<=end:
        mid=(start+end)//2
        cnt=0
        B=M
        for i in range(0, N):
            if budget[i]>mid and B>=mid:
                B-=mid
                cnt+=1
            elif budget[i]<=mid and B>=mid:
                B-=budget[i]
                cnt+=1
        if cnt==len(budget):
            start=mid+1
            ans=mid
        else:
            end=mid-1

print(ans)
