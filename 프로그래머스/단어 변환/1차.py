from collections import deque

def can_change(w1, w2):
    diff = 0

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1

    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))
    visited = set()

    while q:
        word, depth = q.popleft()

        if word == target:
            return depth

        for w in words:
            if w not in visited and can_change(w, word):
                visited.add(w)
                q.append((w, depth + 1))

    return 0


begin = "hit"
target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))