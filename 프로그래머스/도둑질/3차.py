def solution(money):
    length = len(money)

    case1 = rob(money[0:length-1])
    case2 = rob(money[1:length])

    return max(case1, case2)

def rob(houses):
    length = len(houses)
    dp = [0 for _ in range(length)]

    for i in range(length):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    return dp[-1]

money = [1,2,3,1]
print(solution(money))