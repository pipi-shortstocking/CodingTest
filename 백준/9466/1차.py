t = int(input())

state = [0 for _ in range(100005)]  # 크기 확인


def run(x):
    cur = x
    while True:
        state[cur] = x  # 방문 시작 노드 표시
        # print("state[cur] : ", state[cur])
        cur = arr[cur]  # 이번에 방문할 노드 idx
        # print("cur : ", cur)
        if state[cur] == x:  # 이번에 방문한 노드인지
            while state[cur] != -1:  # 사이클 표시를 아직 안했을 경우
                state[cur] = -1  # 사이클 표시
                cur = arr[cur]  # 이번에 방문할 노드 idx
            return
        elif state[cur] != 0:  # 이전에 방문했던 노드
            return


for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    for i in range(1, n + 2):
        state[i] = 0

    for i in range(1, n + 1):
        if state[i] == 0:  # 아직 방문 안함
            run(i)

    cnt = 0
    for i in range(1, n + 1):
        if state[i] != -1:
            cnt += 1

    print(cnt)
