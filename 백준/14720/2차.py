import sys
input = sys.stdin.readline

n = int(input()) # 우유 가게의 수
store = list(map(int,input().split()))
order = 0

for i in range(n):
    if store[i] == (order % 3):
        order += 1        
            
print(order)