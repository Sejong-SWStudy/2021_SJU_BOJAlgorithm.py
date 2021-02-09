N=int(input())

graph=[]
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x<0 or x>N-1 or y<0 or y>N-1: #0~N-1
        return False
    global num
    if graph[x][y]==1:
        graph[x][y]=0
        num+=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

house_number=[]
num=0

for i in range(N):
    for j in range(N):
        if dfs(i, j)==True:
            house_number.append(num)
            num=0

print(len(house_number))

for i in sorted(house_number):
    print(i)
