from collections import deque

def solution(begin, target, words):
    # target이 words 안에 없으면 0 return
    if target not in words:
        return 0

    length = len(words)
    visited = [False] * length
    queue = deque([(begin, 0)])

    while queue:
        w, cnt = queue.popleft()
        
        if w == target:
            return cnt

        for i in range(length):
            if not visited[i] and is_diff(w, words[i]):
                queue.append([words[i], cnt + 1])
                visited[i] = True

def is_diff(target, word):
    diff = 0

    for i in range(len(target)):
        if target[i] != word[i]:
            diff += 1

    if diff != 1:
        return False
    
    return True

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))