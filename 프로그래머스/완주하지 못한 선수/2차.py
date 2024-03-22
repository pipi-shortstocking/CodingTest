def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    # arr = []

    for par in participant:
        # 딕셔너리에 참가자 저장 (hash 함수로 같은 value 저장 가능)
        hashDict[hash(par)] = par
        # 딕셔너리 key값 저장
        sumHash += hash(par)
        # arr.append(hash(par))

    for com in completion:
        # 각 참가자의 key값 삭제
        sumHash -= hash(com)

    return hashDict[sumHash]
    # return arr


# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
