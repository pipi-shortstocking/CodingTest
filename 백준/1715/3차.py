import sys, heapq
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    heapq.heappush(arr,int(input()))

result = 0

while len(arr) >= 2:
    temp1 = heapq.heappop(arr)
    temp2 = heapq.heappop(arr)
    result += temp1+temp2

    heapq.heappush(arr, temp1+temp2)

print(result)