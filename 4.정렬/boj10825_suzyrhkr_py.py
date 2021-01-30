n = int(input())
student = []
for i in range(n):
  name, kor, eng, math = list(input().split())
  student.append([name, int(kor), int(eng), int(math)])

student.sort(key=lambda x: x[0])
student.sort(key=lambda x: -x[3])
student.sort(key=lambda x: x[2])
student.sort(key=lambda x: -x[1])

for name in student:
  print(name[0])
