def solution(people, limit):
    people.sort()
    i, j = 0, len(people)-1
    cnt = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        cnt += 1

    return cnt

people = [70, 50, 80, 50]
limit = 100
# people = [70, 80, 50]
# limit = 100
print(solution(people, limit))