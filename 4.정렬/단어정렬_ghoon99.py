n = int(input())
words = list(set([input() for _ in range(n)]))
words.sort()
words.sort(key=lambda x:len(x))
for i in words:
  print(i)
