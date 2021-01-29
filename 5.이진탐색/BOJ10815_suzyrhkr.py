# 첫 번째 풀이 (반복문 이용)
def bst(target):
  start, end = 0, n-1
  while (start<=end):
      mid = (start+end)//2

      if card[mid] == target:
        return 1
      elif card[mid] < target:
        start = mid+1
      else:
        end = mid-1
  return 0

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
check = list(map(int, input().split()))

for i in check:
  ret = bst(i)
  print(ret, end=' ')

#--------------------------------------------------------
#두 번째 풀이 (재귀 함수 이용)
def recurr_bst(target, start, end):
  if start>end:
    print(0, end=' ')
    return
  mid = (start+end)//2

  if card[mid] == target:
    print(1, end=' ')
    return
  elif card[mid] > target:
    recurr_bst(target, start, mid-1)
  else:
    recurr_bst(target, mid+1, end)

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
check = list(map(int, input().split()))

for i in check:
  recurr_bst(i, 0, n-1)

#--------------------------------------------------------
# 세 번째 풀이 (set을 이용한 간단한 풀이)
n = int(input())
card = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for i in check:
  if i in card:
    print(1, end=' ')
  else:
    print(0, end=' ')
