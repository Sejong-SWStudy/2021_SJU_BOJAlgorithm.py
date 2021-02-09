def DFS(x, y):
    global ct

    arr[x][y] = 0  # 현재 해당 인덱스를 0으로 만들어 줍니다.
    ct += 1  # 인덱스가 1인 경우, ct 변수를 1 증가시켜줍니다.

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= N or dy < 0 or dy >= N:  # 현재 인덱스 기준으로 아래,왼쪽,위,오른쪽을 보며, 범위에 벗어나면 continue로 지나칩니다.
            continue

        if arr[dx][dy] == 1:  # 만약, 아래,왼쪽,위,오른쪽 인덱스 중 1이 있으면, 해당 인덱스로 가서 DFS 함수를 실행합니다.
            DFS(dx, dy)


N = int(input())
ct = 0
arr = []
answer = []
total = 0
nx = [-1, 0, 1, 0]  # nx, ny는 주변 4방향 인덱스를 반복문으로 돌기 위해 만든 리스트입니다.
ny = [0, -1, 0, 1]
for i in range(N):
    arr.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:  # 인덱스가 1인 경우만 DFS 함수로 들어갑니다.
            DFS(i, j)  # 이 부분에서, DFS함수가 주변 1을 돌며 0으로 바꿔줍니다.
            total += 1  # 총 단지의 수를 증가시켜 줍니다.
            answer.append(ct)  # 집의 수를 answer에 append 해주고, ct를 0으로 초기화해줍니다.
            ct = 0

answer.sort()  # 오름차순으로 출력하라고 했기에 sort 함수를 사용하였습니다.
print(total)
for i in answer:
    print(i)