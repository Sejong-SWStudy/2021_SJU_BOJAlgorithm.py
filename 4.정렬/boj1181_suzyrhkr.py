words=[]
n = int(input())

for i in range(n):
  ch=input()
  words.append(ch)

words= list(set(words))
words.sort()
words.sort(key=len)

for i in words:
  print(i)
