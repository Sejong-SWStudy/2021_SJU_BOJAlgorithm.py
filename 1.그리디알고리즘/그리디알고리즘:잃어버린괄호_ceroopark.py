S=input().strip().split("-")

sum_n=0
for i in S[0].split("+"):
    sum_n+=int(i)

if len(S)>1:
    for s in S[1:]:
        sum_n-=sum(map(int, s.split("+")))
                   
print(sum_n)  
