from sys import stdin

n = int(stdin.readline())
arr = []

for i in range(n):
  name,kor,eng,math = stdin.readline().split()
  kor,eng,math = int(kor),int(eng),int(math)
  tmp = [name,(kor,eng,math)]
  arr.append(tmp)

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1][2],reverse=True)
arr.sort(key=lambda x:x[1][1])
arr.sort(key=lambda x:x[1][0],reverse=True)
for name in arr:
  print(name[0])
