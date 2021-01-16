# 첫번째 풀이 (Accept)
str_input = input()
cnt=0

for i in range(len(str_input)-1):
  if (str_input[i] != str_input[i+1]):
    cnt+=1

if cnt%2 ==0:
  print(cnt//2)
else:
  print(cnt//2 + 1)

# 두번째 풀이(RunTime Error)
str_input = input()
cnt_a, cnt_b = 0,0

split_a = str_input.split(a)

for i in split_a:
  if i!='':
    cnt_a +=1

split_b = str_input.split(b)

for i in split_b:
  if i!='':
    cnt_b +=1

print(min(cnt_a, cnt_b))
