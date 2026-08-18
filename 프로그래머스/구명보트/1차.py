# 정답! 1차-1은 정석 투포인터

def solution(people, limit):
    people = sorted(people, reverse=True)
    people_cnt = len(people)
    saved = [False for _ in range(people_cnt)]
    cnt = 0

    for i, j in enumerate(people):
        if not saved[i]:
            if j + people[-1] <= limit:
                cnt += 1
                saved[i] = True
                saved.pop()
                people.pop()
            else:
                cnt += 1
                saved[i] = True

    return cnt

# people = [70, 50, 80, 50]
# limit = 100
people = [70, 80, 50]
limit = 100
print(solution(people, limit))