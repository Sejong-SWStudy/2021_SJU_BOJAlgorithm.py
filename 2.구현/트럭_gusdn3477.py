from collections import deque
from sys import stdin

n, w, L = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
time = 0
bridge = deque()
total_weight = 0
queue = deque(arr)

while True:
    
    if not bridge and not queue: # 다리와 큐가 모두 비었으면 종료.
        break
        
    total_weight = 0 # 다리 위에 있는 차량의 무게를 저장하는 변수입니다.
        
    if bridge:
        for i in range(len(bridge)):
            bridge[i][1] += 1 # 다리에 있는 모든 요소의 시간을 1씩 증가시켜 준다.
            
        if bridge[0][1] > w: # 다리에 있는 시간이 다리의 길이보다 커지면, 통과된 것임.
            bridge.popleft() # 그런 차량은 bridge에서 pop 해준다.
            
        # pop 해주는 과정이, 새로 들어오는 과정보다 먼저여야 합니다. 
        # 차량이 나가면서 동시에 들어올 수 있는데, 먼저 나가지 못하면 새로운 차량이 들어올 수 없습니다.
            
    
    if not bridge: # 다리가 빈 경우, 다리 위의 차량의 무게는 0입니다.
        total_weight = 0
        
    else: # 그 외의 경우, 차량의 무게를 모두 더합니다.
        for i in range(len(bridge)):
            total_weight += bridge[i][0]
        
    if queue and total_weight + queue[0] <= L: #큐에 차량이 남아있으며, 새로운 차량이 다리 위에 올라와도 최대 중량보다 같거나 적으면, 큐에서 하나를 뽑아 다리 위에 올립니다.
        a = queue.popleft()
        bridge.append([a,1])
        
    time += 1
    
print(time)
