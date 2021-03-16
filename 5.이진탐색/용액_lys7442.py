import sys
n=int(input())
liquid=list(map(int,input().split()))
liquid=sorted(liquid)

if(liquid[-1]<0): #전부 음수
    print(liquid[-2],liquid[-1])
elif(liquid[0]>0): #전부 양수
    print(liquid[0],liquid[1])
else:
    for i in range(1,len(liquid)):
        if(liquid[i-1]<0 and liquid[i]>0):
            border=i #음수와 양수 사이 경계가 되는 지점, border부터 양수
            break
    l,r=border,len(liquid)-1
    closest=[liquid[border-1],liquid[border],abs(liquid[border-1]+liquid[border])] #초기값
    for nn in range(border-1,-1,-1):
        while(l<=r):
            mid=(l+r)//2
            if(abs(liquid[nn]+liquid[mid])<closest[2]):
                closest=[liquid[nn],liquid[mid],abs(liquid[nn]+liquid[mid])]
            if(liquid[nn]+liquid[mid]<0):
                l=mid+1
            elif(liquid[nn]+liquid[mid]>0):
                r=mid-1
            else: #특성값이 정확히 0
                break
        l=r
        r=len(liquid)-1
    print(closest[0],closest[1])
        
        
        
