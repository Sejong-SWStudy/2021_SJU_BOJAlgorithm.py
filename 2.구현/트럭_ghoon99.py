from collections import deque
# input

n,w,l =map(int,input().split())
arr = deque(list(map(int,input().split())))

# solution
moved = []
bridge = deque([0]*w)
result = 0
#print(bridge)

while len(moved)!=n:
  if arr and sum(bridge)+arr[0]-bridge[-1] <= l:
    bridge.appendleft(arr.popleft())
  else:
    bridge.appendleft(0)

  truck = bridge.pop()

  if truck != 0:
    moved.append(truck)
  #print(bridge,moved)

  result += 1


# output
print(result)
