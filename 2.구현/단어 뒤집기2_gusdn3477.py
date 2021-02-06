from collections import deque

flag = 0
S = input()
stack = deque()

for i in S:

    # < 가 나오는 경우, 이전에 스택을 다 비워주고 > 만날 때 까지 스택에 쌓음

    if i == ' ': #공백을 만나는 경우

        if flag == 0:  # flag가 0이면 -> 모두 출력
            while stack:
                a = stack.pop()
                print(a, end='')
            print(i, end='')

        else:  # flag == 1인 경우, 괄호 모드이므로 일단 스택에 넣기.
            stack.append(i)

    elif i == '<':  # 앞에 있는 것들 모두 출력
        flag = 1
        while stack:
            a = stack.pop()
            print(a, end='')

        print(i, end='')

    elif i == '>':  # 닫는 괄호가 나오면 앞의 것부터 차례대로 출력한다.
        flag = 0
        while stack:
            a = stack.popleft()
            print(a, end='')
        print(i, end='')

    else: #단순한 문자열일 경우
        stack.append(i)

while stack:  # 남은 것들 모두 출력
    a = stack.pop()
    print(a, end='')
