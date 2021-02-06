# input
string = input()
result = []
word =[]
open = False

# solution
for idx,chr in enumerate(string):
  if open and chr != '>': # 열린 상태
    word.append(chr)
    continue

  if chr == ' ':  # 공백
    word.reverse()  # 뒤집고
    result.append("".join(word)) # 단어로 저장
    word = [] # 초기화

  elif chr == '<': # 여는 태그
    if word: # 이미 단어가 있으면 
      word.reverse() # 뒤집고
      result.append("".join(word)) # 단어로 저장 
      word = [] # 초기화
    word.append(chr)
    open = True # 열림

  elif chr == '>': # 닫는 태그
    word.append(chr) 
    result.append("".join(word)) # 안 뒤집고 저장
    word = []
    open = False # 닫힘

  else: # 그 외
    word.append(chr) # 문자 추가
    
if word: # 추가 안한 남은 문자가 있으면 
  word.reverse() # 뒤집고 추가
  result.append("".join(word))


# output 
# 현재 result 는 ['<tag>','54321','<close tag>'] 인 단어로 구별된 리스트로 되어있음
for idx in range(len(result)-1):
  if result[idx][0]=='<' or result[idx+1][0]=='<':
    print(result[idx],end='')
  else:
    print(result[idx],end=' ')
    
print(result[-1])
