def solution(citations):
    citations.sort()
    n = len(citations)

    for i, c in enumerate(citations):
        # c번 이상 인용된 논문 수 -> n - i

        if c >= n - i:
            return c


citations = [3,0,6,1,5]
print(solution(citations))