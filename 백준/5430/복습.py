from collections import deque

t = int(input())  # 테스트 케이스

for _ in range(t):
    p = str(input().rstrip())  # 수행 함수
    n = int(input())  # 배열 크기
    arr = deque(input().rstrip()[1:-1].split(","))  # 배열

    cnt = 0
    flag = 0  # error 출력 종료 여부

    for order in p:
        if order == "R":
            cnt += 1
        elif order == "D":
            if n == 0 or not arr:
                flag = 1
                break
            if cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if flag:
        print("error")
    else:
        if cnt % 2 == 1:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
