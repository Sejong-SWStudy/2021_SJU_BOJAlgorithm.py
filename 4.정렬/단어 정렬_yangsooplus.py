def selection_sort_st(list):
    for i in range(len(list)-1):
        keep_i = i
        for j in range(i+1, len(list)):
            if len(list[j]) < len(list[keep_i]):
                keep_i = j
            elif len(list[j]) == len(list[keep_i]):
                if list[j] < list[keep_i]:
                    keep_i = j

        tmp = list[i]
        list[i] = list[keep_i]
        list[keep_i] = tmp
    return list

n = int(input())
words = list()
for i in range(n):
    input_word = input()
    if input_word not in words:
       words.append(input_word)

words = selection_sort_st(words)

for w in words:
    print(w)