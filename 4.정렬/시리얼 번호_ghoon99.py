import re
def toSum(string):
  nums = re.findall("\d",string) # 정규표현식 , nums 에는 숫자만(자료형은 문자) 리스트로 저장 
  return sum(list(map(int,nums))) if len(nums)>0 else 0 # 리스트에있는 숫자들을 int 형으로 바꿔서 모두 합하여 반환 / 빈 리스트면 0 을 반환

# input
n =int(input())
arr = [input() for _ in range(n)]

# solution
arr.sort()  # 먼저 사전순 정렬
arr.sort(key=toSum) # 숫자합 순 정렬 
arr.sort(key=lambda x:len(x)) # 길이순 정렬

# output
for data in arr:
  print(data)
