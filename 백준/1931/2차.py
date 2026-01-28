import sys
input = sys.stdin.readline

n = int(input())
timeline = []

for i in range(n):
    start, end = map(int, input().split())

    timeline.append((start, end))

timeline.sort(key = lambda x: (x[1], x[0])) # 가장 빨리 끝나는 회의부터 차례대로 보겠다

cnt = 0
end_time = 0

for start, end in timeline:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)