s = input()

def to_one(string):
  cnt = 0
  for i in range(len(string)-1):
    if string[i]=='0':
      if string[i+1]=='0':
        continue
      else:
        cnt+=1
  if string[-1]=='0':
    cnt+=1
  return cnt

def to_zero(string):
  cnt = 0 
  for i in range(len(string)-1):
    if string[i]=='1':
      if string[i+1]=='1':
        continue
      else:
        cnt+=1
  if string[-1]=='1':
    cnt+=1 
  return cnt


result = min(to_one(s),to_zero(s))
print(result)
