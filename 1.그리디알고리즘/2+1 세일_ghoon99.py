n = int(input())
ci = [int(input()) for _ in range(n)]
ci.sort(reverse=True)

result = 0
for i in range(0,n,3):
  tmp = ci[i:i+3]
  if len(tmp)==3:
    result += sum(tmp)-min(tmp)
  else:
    result += sum(tmp)
 
print(result)
