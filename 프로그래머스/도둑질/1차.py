def solution(money):
    house_cnt = len(money)
    dp = [0 for _ in range(house_cnt)]
    dp[0] = money[0]
    dp[1] = money[1]

    for i in range(2, house_cnt):
        dp[i] = dp[i-2] + money[i]

    if dp[-1] > dp[-2]:
        return dp[-1]
    else:
        return dp[-2]

money = [1,2,3,1]
print(solution(money))