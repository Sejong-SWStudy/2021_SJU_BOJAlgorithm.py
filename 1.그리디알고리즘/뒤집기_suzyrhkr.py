# 첫 번째 풀이
str_input = input()
cnt_0, cnt_1 = 0,0

split_0 = str_input.split('0')
split_1 = str_input.split('1')

cnt_1 = split_0.count('')
cnt_0 = split_1.count('')

print(min(len(split_0)-cnt_1, len(split_1)-cnt_0))

# 두 번째 풀이
str_input = input()
cnt=0

for i in range(len(str_input)-1):
  if (str_input[i] != str_input[i+1]):
    cnt+=1

if cnt%2 ==0:
  print(cnt//2)
else:
  print(cnt//2 + 1)
