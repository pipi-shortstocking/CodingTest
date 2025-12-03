def solution(strings, n):
    answer = sorted(strings, key = lambda x: (x[n], x))

    return answer

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))

strings = ["abce", "abcd", "cdx"]
n = 2

print(solution(strings, n))