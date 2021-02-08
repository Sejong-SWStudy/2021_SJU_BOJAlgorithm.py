ST=input()+' '

temp=''
idx=0

while idx<len(ST):
    if ST[idx]==' ':
        print(temp[::-1], end=' ')
        temp=''
    elif ST[idx]=='<':
        print(temp[::-1], end="")
        temp=''
        tag=ST.find('>', idx)
        print(ST[idx:tag+1], end='')
        idx=tag
    else:
        temp+=ST[idx]
    idx+=1

