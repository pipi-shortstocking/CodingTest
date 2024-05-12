n = int(input()) # n번 재귀함수를 물으면 그 다음 재귀함수 물음에 답변

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

ans1 = '"재귀함수가 뭔가요?"'
ans2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
ans3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
ans4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
ans5 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
ans6 = '라고 답변하였지.'

frist = [ans1, ans2, ans3, ans4]
last = [ans1, ans5, ans6]
h = "____"

def re(n, cnt):
    if n == 0:
        for j in range(3):
            print(h*cnt + last[j])
        return
    
    for i in range(4):
        print(h*cnt + frist[i])
    
    re(n-1, cnt+1)
    print(h*cnt + ans6)

re(n, 0)