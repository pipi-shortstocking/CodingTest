from collections import deque

def can_change(word1, word2):
    length = len(word1)
    is_difference = 0

    for i in range(length):
        if word1[i] != word2[i]:
            is_difference += 1

    return is_difference

def solution(begin, target, words):
    q = deque()
    visited = set()

    if target not in words:
        return 0
    
    q.append((begin, 0))

    while q:
        word, depth = q.popleft()

        if word == target:
            return depth
        
        for w in words:
            if w not in visited and can_change(word, w) == 1:
                q.append((w, depth + 1))
                visited.add(w)

    return depth


begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))