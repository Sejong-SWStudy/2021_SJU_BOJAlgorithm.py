N=int(input())


a=list(map(int, input().split()))

Arr=list(sorted(set(a)))#jung bok jae geo

ans_sheet={value:index for index, value in enumerate(Arr)}


for element in a:
    print(ans_sheet[element], end=" ")
