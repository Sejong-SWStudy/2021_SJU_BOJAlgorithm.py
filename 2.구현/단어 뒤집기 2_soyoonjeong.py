# 17413
s = input()
start = 0
i = 0 #문자열 인덱스
while True:
    if s[i] == ' ':  # 태그모드가 아닐 때 공백문자 만나면
        for j in range(i-1, start-1, -1):
            print(s[j], end='')
        print(" ", end='')
        start = i+1
    elif s[i] == '<':  # 태그모드 시작
        for j in range(i-1, start-1, -1):  # 태그시작 전에 있던 문자들 출력
            print(s[j], end='')
        while s[i] != ">":
            print(s[i], end='')
            i += 1
        print(">", end='')
        start = i+1
        if i == len(s)-1:  # 혹시 태그로 끝날경우
            break
    elif i == len(s)-1: 
        for j in range(i, start-1, -1):
            print(s[j], end='')
        break
    i += 1
