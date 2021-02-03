def solution():
  stack =[]
  result = 0
  for chr in string:
    print(chr,stack)
    if chr=='(':
      stack.append(chr)
    elif chr=='[':
      stack.append(chr)
    elif chr==')':
      if stack[-1]=='(':
        stack.pop()
        stack.append(2)
      else:
        tmp =stack.pop()*2
        stack.pop()
        stack.append(tmp)

        
    elif chr ==']':
      if stack[-1]=='[':
        stack.pop()
        stack.append(3)
      else:
        tmp =stack.pop()*3
        stack.pop()
        stack.append(tmp)

  return result

def check():
  stack=[]
  for chr in string:
    if chr=='(':
      stack.append(chr)
    elif chr=='[':
      stack.append(chr)
    elif chr==')':
      if len(stack)==0 or stack[-1]!='(':
        return False
      stack.pop()
    elif chr ==']':
      if len(stack)==0 or stack[-1]!='[':
        return False
      stack.pop()
  if stack:
    return False

  return True


string = input()

if check():
  print(solution())
else:
  print(0)
