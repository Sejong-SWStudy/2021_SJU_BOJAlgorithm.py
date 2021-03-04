from collections import deque

s = input()
num = deque()
oper = deque()
st = ''
flag = 0

for i in s:

    if i == '-':
        num.append(int(st))
        oper.append(i)
        st = ''

    elif i == '+':
        num.append(int(st))
        oper.append(i)
        st = ''

    else:
        st += i

num.append(int(st))
total = 0

while '+' in oper:
    a = oper.index('+')
    del oper[a]
    x, y = num[a], num[a + 1]
    del num[a]
    del num[a]
    num.insert(a, x + y)

while oper:
    a = oper.popleft()
    x = num.popleft()
    y = num.popleft()
    num.appendleft(x - y)

print(*num)