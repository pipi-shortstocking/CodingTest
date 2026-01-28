import sys
input = sys.stdin.readline

n = int(input())
timeline = []
cnt = 0

for i in range(n):
    start, end = map(int, input().split())

    timeline.append((start, end))

timeline.sort(key=lambda x : x[1])

for i in range(n):
    temp = []
    now_end = timeline[i][1]

    temp.append(i) # 인덱스만 저장

    j = 1
    last = 0
    while True:
        if j >= n:
            if cnt < len(temp):
                cnt = len(temp)
            
            if len(temp) > 1:
                last = temp.pop()

                if last == n - 1:
                    j = temp.pop() + 1
                else:
                    break
            else:
                break

        next_start = timeline[j][0]

        if next_start >= now_end:
            temp.append(j)
            now_end = timeline[j][1]

        j += 1

print(cnt)