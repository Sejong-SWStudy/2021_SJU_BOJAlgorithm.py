n = int(input())

tile = [0]*1001

tile[1] = 1
tile[2] = 2

for i in range(3, n+1):
    tile[i] = tile[i-2] + tile[i-1]

print(tile[n]%10007)