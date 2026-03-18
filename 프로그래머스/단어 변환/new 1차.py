# 우연히 성공한 해답
# new 2차로 이어짐

from collections import deque

def can_change(word1, word2):
    length = len(word1)
    is_difference = 0

    for i in range(length):
        if word1[i] != word2[i]:
            is_difference += 1

    return is_difference

def change_word(begin, target, words):
    count = 0

    if target not in words:
        return 0
    
    for word in words:
        if can_change(begin, target) == 1:
            count += 1
            return count

        if can_change(begin, word) == 1:
            count += 1
            begin = word

    return count

begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]

print(change_word(begin, target, words))