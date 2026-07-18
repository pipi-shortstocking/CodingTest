def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # set은 해시 가능한 값만 담을 수 있음
    # 리스트 -> 변경 가능해서 해시 X
    # 튜플 -> 변경 불가능해서 해시 O
    # 본 문제에서 굳이 set으로 바꾸지 않아도 통과됨
    puddles_set = set(tuple(p) for p in puddles)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) in puddles_set:
                dp[i][j] = 0
            elif i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n][m]

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))