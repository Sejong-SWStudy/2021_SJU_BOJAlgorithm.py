def bi_search(target, card_list):
    size = len(card_list)
    if size > 1:
        if card_list[size//2] == target:
            return 1
        elif card_list[size//2] > target:
            return bi_search(target, card_list[0:size//2])
        elif card_list[size // 2] < target:
            return bi_search(target, card_list[size//2:size])
        else:
            return 0
    else:
        if card_list[0] == target:
            return 1
        else:
            return 0


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

cards.sort()

for num in find:
    x = bi_search(num, cards)
    print(x,end=" ")