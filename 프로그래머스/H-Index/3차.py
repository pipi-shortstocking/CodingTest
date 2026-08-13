def solution(citations):
    citations.sort()
    n = len(citations)
    answer = 0

    for i, c in enumerate(citations):
        # c번 이상 인용된 논문 수 -> n - i

        if c >= n - i:
            answer = n - i

    return answer

# citations = [3,0,6,1,5]
citations = [0,0,0]
print(solution(citations))