def sum(string):
    result=0
    for s in string:
        if s.isdigit():#For true
            result+=int(s)
    return result

def compare(str1, str2):
    #1
    if len(str1)<len(str2):
        return True
    elif len(str1)>len(str2):#not else cause if using else this def can't be over
        return False
    #2
    if sum(str1)<sum(str2):
        return True

    elif sum(str1)>sum(str2):
        return False
    #3
    for i in range(len(str1)):
        if ord(str1[i]) < ord(str2[i]):
            return True
        elif ord(str1[i]) > ord(str2[i]):
            return False

def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(len(a)-1, i, -1):
            if compare(a[j-1], a[j])==False:
                a[j-1], a[j] = a[j], a[j-1]
                
N=int(input())
products=[]

for _ in range(N):
    products.append(input())

bubble_sort(products)

for s in products:
    print(s)
