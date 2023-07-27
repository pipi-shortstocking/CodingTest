import sys, heapq
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    heapq.heappush(arr,int(input()))

result = 0

while len(arr) >= 2:
    for i in range(2):
        result += heapq.heappop(arr)
    heapq.heappush(arr,result)

print(result)