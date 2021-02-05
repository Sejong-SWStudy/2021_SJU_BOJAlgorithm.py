N, K = map(int, input().split())
worth = []
cnt = 0  # 동전의 갯수를 저장할 변수

for i in range(N):
    worth.append(int(input()))

worth.sort(reverse=True)  # 큰 가치의 단위부터 나오도록 내림차순으로 정렬합니다.

for i in worth:
    cnt += K // i  # 바꿀 수 있으면 동전으로 해당 동전으로 최대한 바꾸는 코드입니다. 해당 동전의 가치가 가지고 있는 돈보다 크면 0으로 계산됩니다.
    K %= i  # 동전으로 바꾸고, 남은 돈을 다시 K에 저장하는 코드입니다. 해당 동전의 가치가 K보다 크면 현재 K값이 유지됩니다.

    if K == 0:
        break

print(cnt)