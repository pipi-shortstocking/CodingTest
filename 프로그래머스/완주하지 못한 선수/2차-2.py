from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]


# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
