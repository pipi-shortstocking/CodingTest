# 백트래킹 방식

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0 for _ in range(m)] # m개의 자리수 숫자만 확인
isUsed = [False for _ in range(n + 1)] # 사용된 숫자를 기록할 배열

def solution(cnt):
    if cnt == m:
        print(*arr)
        
        return # cnt 값이 m과 같다면 끝

    for num in range(1, n + 1):
        if not isUsed[num]: # 아직 num을 사용하지 않았다면
            arr[cnt] = num # cnt번 째 자리에 num 사용
            isUsed[num] = True # num 사용함
            solution(cnt + 1) # 다음 자리 수로 넘어가기
            isUsed[num] = False # 이번 분기에서의 num 사용 취소


solution(0)