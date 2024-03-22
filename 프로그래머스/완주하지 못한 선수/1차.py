def solution(participant, completion):
    # 동명이인 해결 X
    # ans = [name for name in participant if name not in completion]

    # idxs = []
    # # for idx in range(len(completion)):
    # for name in completion:
    #     #  완주 선수 이름과 동일한 참가 선수의 인덱스 값 저장
    #     if name in participant:
    #         idxs.append(participant.index(name))

    for name in completion:
        if name in participant:
            idx = participant.index(name)
            del participant[idx]

    answer = ""
    answer += participant[0]

    return answer


# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
