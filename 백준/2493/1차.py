import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))

ans = [0 for _ in range(n)]

for i in range(1, n): # 첫번째 탑은 무조건 만나지 못함
    for j in range(i,0,-1): # i번째 탑부터 첫번째 탑까지 탐색
        if tops[i] < tops[j]:
            ans[i] = j + 1
            break
    
print(*ans)
# 시간 초과