st = input()

set_one = 0
set_zero = 0

cur = "9"

for i in st:
    if cur != i:
        if i == "0":
            set_zero += 1
            cur = "0"
        else:
            set_one += 1
            cur = "1"

if set_one <= set_zero:
    print(set_one)
else:
    print(set_zero)