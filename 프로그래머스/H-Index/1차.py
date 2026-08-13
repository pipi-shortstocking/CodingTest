def solution(citations):
    citations.sort()
    n = len(citations)

    mid = n // 2
    h = citations[mid]
    c = citations[mid:]
    nc = citations[:mid]

    while True:
        if len(c) >= h:
            for p in nc:
                if p <= h:
                    return h
                else:
                    h -= 1

citations = [3,0,6,1,5]
print(solution(citations))