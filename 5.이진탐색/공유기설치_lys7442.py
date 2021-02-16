def binary(arr,c):
    def possible(gap):
        count=0
        tmp=-gap
        for i in arr:
            if(tmp+gap<=i):
                tmp=i
                count+=1
            if(count>=c):
            return True
        return False
    l,r=0,max(arr)
        while(l<=r):
            mid=(l+r)//2
            if(possible(mid)): # 가능  -> 간격 더 늘려도 된다
                l=mid+1
                result=mid
            else: # 불가능 -> 간격 더 좁혀야 한다
                r=mid-1 
            return result

import sys
n,c=map(int,sys.stdin.readline().split())
arr =[int(sys.stdin.readline())for _ in range(n)]
arr=sorted(arr)
print(binary(arr,c))

'''
def binary(c):
    l,r=1,wifi[-1]
    max_distance=1
    while(l<=r):
        mid=(l+r)//2
        tmp=-mid
        cnt=0
        for i in wifi:
            if(i>=tmp+mid):
                cnt+=1
                tmp=i
        if(cnt>=c):
            max_distance=mid
            l=mid+1
        else:
            r=mid-1
    return max_distance

from sys import stdin
n,c=map(int,stdin.readline().split())
wifi=[]
for i in range(n):
    x=int(stdin.readline())
    wifi.append(x)
wifi=sorted(wifi)
print(binary(c))
'''
