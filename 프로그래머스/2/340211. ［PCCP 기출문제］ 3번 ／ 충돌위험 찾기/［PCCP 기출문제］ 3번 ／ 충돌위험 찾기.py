from collections import deque, defaultdict

def solution(points, routes):
    
    # 좌표계에서 탐색하는 bfs문제<- 시간마다 움직여야 하니까
    # 동일한 좌표에 로봇이 두대 이상 모인다면 충돌위험 있음 <- 카운트
    # 동일한 시간에 여러 좌표에서 발생할경우 전부 카운트
    # 각 포인트좌표가 주어짐 :출발/도착 장소
    # 루트는 i번째 로봇이 출발-경유-도착하는 포인트
    # 특정포인트에서 포인트로 이동할 때, 동시에 끝나지 않을수도 있기 때문에 고려해야함
    # 결국엔 순수하게 탐색 돌리는게 맞고, 동시에 충돌여부를 확인해야 하기 때문에 BFS
    # 루트 하나당 최대 움직일수있는 거리 200 거기에 포인트가 100개 까지 있을 수 있고, 로봇이 100개 있을 수 있음 100 200*100*100 = 2000000 정도면 돌만한듯
    
    # 로봇의 움직임을 검사하는 함수-> 특정포인트에 도착했는지 확인하고 안했다면 규칙대로 한칸씩 움직이는 함수
    # 그럼 최대 100*100의 필드를 리스트로 초기화한 보드를 만들어서 인덱스를 로봇으로 사용해 움직이면 되겠네<- 아니야 리스트를 넣었다 뺏다 해야되서 살짝 손해인데
    # 리스트를 하나 더만들기. 코드가 너무 복잡해질 수 있음 그냥 리스트 조절로 가자
    # 그러게 보드가 필요하나?
    # 보드없이, 로봇이 현재 자기 좌표기억하고
    # 좌표값을 가진 map을 운용, 현재 좌표에 로봇 몇대있는지 기억하고
    # map값이 2이상이면 카운트
    # 각 시간이 지날때마다 map을 초기화하는게 포인트
    
    queue = deque()
    locate = defaultdict(int)
    crash=0
    
    
    for i in range(len(routes)):
        # 로봇의 메타데이터
        # 나는 어떤 로봇이고,
        # 몇번째 체크포인트를 목표로 하고있는지
        # 그리고 시작포인트의 좌표값 기억
        robot = [i,0,points[routes[i][0]-1]]
        queue.append(robot)
        
        cur_row, cur_col = robot[2]
        locate[(cur_row, cur_col)] +=1

        if locate[(cur_row, cur_col)] == 2:
            crash+=1
            # print("crash~!!!!~!~!~! : ", crash)

    # print(queue)
    
    while queue:
        # print("----------time-----------")
        len_queue = len(queue)
        locate = defaultdict(int)
        
        
        for _ in range(len_queue):
            
            robot_num, robot_cur_goal_point,(cur_row, cur_col) = queue.popleft()
            # print("robot_activate", robot_num)
            
            goal_row, goal_col = points[routes[robot_num][robot_cur_goal_point]-1]
            
            # 둘다동일함-> 플랫폼도착
            if goal_row == cur_row and goal_col == cur_col:
                # print("platform", robot_num)
                robot_cur_goal_point+=1
                # 도착한 로봇 없에기
                if robot_cur_goal_point >= len(routes[0]):
                    # print("done", robot_num)
                    continue
                goal_row, goal_col = points[routes[robot_num][robot_cur_goal_point]-1]

            # 행먼저
            if goal_row != cur_row:
                if cur_row > goal_row:
                    cur_row-=1
                else:
                    cur_row+=1
            # 열확인하고
            elif goal_col != cur_col:
                if cur_col > goal_col:
                    cur_col-=1
                else:
                    cur_col+=1
            
            locate[(cur_row, cur_col)] +=1
            
            if locate[(cur_row, cur_col)] == 2:
                crash+=1
                # print("crash~!!!!~!~!~! : ", crash)
                
            
            
            # print([robot_num, robot_cur_goal_point, [cur_row,cur_col]])
            queue.append([robot_num, robot_cur_goal_point, [cur_row,cur_col]])
                
        
    answer = 0
    return crash