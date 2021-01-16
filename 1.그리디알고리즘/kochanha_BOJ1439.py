str=input()

cnt0=0
cnt1=0

for i in range(len(str)-1):
    if str[i]!=str[i+1]:
        if str[i]=='0':
            cnt0+=1
        else:
            cnt1+=1
if str[-1]=='0':
    cnt0+=1
else:
    cnt1+=1

print(min(cnt0,cnt1))




