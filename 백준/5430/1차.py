import sys
from collections import deque

input = sys.stdin.readline

t = int(input()) # testcase

for _ in range(t):
    p = list(input().rstrip()) # 수행 함수
    n = int(input()) # 배열크기
    arr_input = list(input().rstrip())
    arr = deque()
    
    for i in arr_input:
        if i.isdigit():
            arr.append(i)

    if p.count('D') > n:
        print("error")
        continue

    for order in p:
        if order == "R":
            arr.reverse()
        elif order == "D":
            arr.popleft()

    print("["+",".join(arr)+"]")
    