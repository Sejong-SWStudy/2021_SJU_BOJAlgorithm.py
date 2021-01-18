test_case=int(input())

for i in range(test_case):
  count=0
  num, position = map(int, input().split())
  priority = list(map(int,input().split()))
  idx = list(priority)
  idx[position] = 'interest'

  while (True):
    if (priority[0]==max(priority)):
      count+=1

      if (idx[0]=='interest'):
        print(count)
        break

      else:
        del priority[0]
        del idx[0]

    else:
      priority.append(priority.pop(0))
      idx.append(idx.pop(0))
