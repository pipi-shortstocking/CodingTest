def solution(id_list, report, k):
    answer = []

    # 유저 ID, 유저가 신고한 ID 정리
    init_list = [[] for _ in range(len(id_list))]
    report_list = dict(zip(id_list, init_list))

    for r in report:
        a = r.split(" ")[0]
        b = r.split(" ")[1]
        
        if b not in report_list[a]:
            report_list[a].append(b)

    # 유저별 신고당한 횟수 정리 (동일 유저가 신고했을 경우 count X)
    init_count = [0 for _ in range(len(id_list))]
    report_count = dict(zip(id_list, init_count))

    for r in list(report_list.values()):
        for member in r:
            report_count[member] += 1

    # k번 이상 신고당한(정지) 유저 정리
    ban_list = []
    for r in report_count:
        if report_count[r] >= k:
            ban_list.append(r)

    # 유저별 정지 유저를 신고한 횟수 정리
    for r in report_list:
        count = 0

        for b in ban_list:
            if b in report_list[r]:
                count += 1

        answer.append(count)

    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))