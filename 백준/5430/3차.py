import sys
from collections import deque

input = sys.stdin.readline

t = int(input()) # testcase

for _ in range(t):
    p = list(input().rstrip()) # 수행 함수
    n = int(input()) # 배열크기
    arr = deque(input().rstrip()[1:-1].split(','))

    cnt = 0
    flag = 1 # error 경우 확인
    
    for order in p:
        if order == "R":
            cnt += 1
        elif order == "D":
            if n == 0 or len(arr) == 0:
                print("error")
                flag = 0
                break
            if cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if flag == 0:
        continue
    else:
        if cnt % 2 == 1:
            arr.reverse()
            
        print("["+",".join(arr)+"]")