from collections import deque

N, K = map(int, input().split())

robot = []
belt = list(map(int, input().split()))
belt = deque(belt)
robot = deque([0] * (2 * N))
second = 1
flag = 0

while True:

    # 1단계
    flag = 0
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[len(robot) // 2 - 1] = 0

    # 2단계

    for i in range(len(robot) // 2 - 1, -1, -1):
        if robot[i] != 0 and robot[i + 1] == 0 and belt[i + 1] >= 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1

    robot[len(robot) // 2 - 1] = 0

    # 3단계
    if belt[0] >= 1 and robot[0] == 0:
        belt[0] -= 1
        robot[0] = 1

    # 4단계
    ct = 0
    for i in belt:
        if i == 0:
            ct += 1

        if ct >= K:
            flag = 1

    if flag == 1:
        break

    second += 1

print(second)