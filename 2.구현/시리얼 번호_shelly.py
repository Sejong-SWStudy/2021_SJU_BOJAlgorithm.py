# 1. 길이가 짧은 것이 먼저
# 2. 길이가 같다면 모든 자리수의 합을 비교해 작은 합
# 3. 1번과 2번으로 결정을 못한다면 사전순


def getShorter(a, b):
    if len(a) < len(b) :
        return a
    elif len(a) > len(b) :
        return b
    else:
        return False

def isNum(a):
    
    return a>='0' and a <='9' 

def getSum(a):
    value = 0
    tmp = a
    
    for i in range(len(a)):
        if isNum(a[i]):
  
            value += int(a[i])
    
    return value

def getSmallerOfSum(a, b):
    aSum = getSum(a)
    bSum = getSum(b)

    if aSum > bSum :
        return b
    elif aSum < bSum :
        return a
    else:
        return False

def getFirstDict(a, b):
    if a > b : 
        return b
    else :
        return a

def needSwap(a, b):
    shorter = getShorter(a, b)
    if shorter == a :
        return False
    elif shorter == b:
        return True

    smallerOfSum = getSmallerOfSum(a, b)
    if smallerOfSum == a :
        return False
    elif smallerOfSum == b :
        return True
    
    firstDict = getFirstDict(a, b)
    if firstDict == a :
        return False
    else :
        return True
    

n = int(input())
arr = []

for i in range(n):
    arr.append(input())

for i in range(n):
    for j in range(i+1, n):

        if needSwap(arr[i], arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

for i in range(n) :
    print(arr[i])
