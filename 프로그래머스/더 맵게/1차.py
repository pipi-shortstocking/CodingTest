# 기준 스코빌 지수 : K
# 모든 음식을 K 이상으로 만들기 위한 섞는 최소 횟수 구하기
# 항상 음식 리스트를 정렬해서 맨 앞의 값이 K가 넘는지 확인 -> 넘으면 바로 횟수 return

# scoville.insert(0, 0)

def mix_food(food1, food2):
    return food1 + (food2 * 2)

def solution(scoville, K):
    count = 0
    scoville.sort()
    
    # 음식이 2개 이상이고 가장 안 매운 음식의 스코빌 지수가 K 미만일 때
    while len(scoville) >= 2 and scoville[0] < K:
        first = scoville.pop(0)
        second = scoville.pop(0)
        
        mixture = mix_food(first, second)
        
        scoville.append(mixture)
        count += 1
        scoville.sort()
        
    if len(scoville) < 2 and scoville[0] < K:
        return -1
    
    return count