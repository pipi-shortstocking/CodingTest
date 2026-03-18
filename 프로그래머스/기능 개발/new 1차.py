# 스택은 하루 단위(하루가 지나면 스택이 비워짐) -> 스택의 크기가 한 번에 배포되는 기능의 수
# 앞서 수행되는 작업이 이후 수행되는 작업보다 오래 걸린다면 이후 작업도 같이 배포 가능
# ex) 1번 작업은 7일 소요 -> 2번 작업은 3일 소요 => 1, 2번 작업 같이 배포 가능

def cal_task_time(progress, speed):
    task = 100 - progress
        
    if task % speed == 0:
        task_time = task // speed
    else:
        task_time = task // speed + 1
    
    return task_time

def solution(progresses, speeds):
    task_count = len(progresses)
    stack = []
    ans = []
    
    # 초기값으로 맨 처음 작업 시간
    stack.append(cal_task_time(progresses[0], speeds[0]))
    
    for i in range(1, task_count):
        time = cal_task_time(progresses[i], speeds[i])
        
        if stack[0] >= time: # 이후 작업이 이전 작업보다 적게 걸리면 같이 배포 가능
            stack.append(time) # 배포 리스트에 추가
        else:
            ans.append(len(stack))
            stack = []
            stack.append(time)
            
    ans.append(len(stack))
        
    return ans