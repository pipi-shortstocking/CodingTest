def solution(routes):
    routes.sort(key = lambda x : x[1])
    cnt = 1
    loc = routes[0][1]

    for car in routes[1:]:
        # 카메라 설치 시점보다 자동차 진입 시점이 뒤에 있으면 카메라에 잡히지 않음
        if loc < car[0]:
            # 최대한 뒤쪽에 카메라를 설치하면 뒤에 나가는 다른 차도 같이 잡힐 확률이 높아짐
            loc = car[1] 
            cnt += 1

    return cnt

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))