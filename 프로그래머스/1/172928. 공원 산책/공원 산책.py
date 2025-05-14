def solution(park, routes):
    
    # 한대의 로봇 움직이기
    # 움직이기전 가능한지 여부 확인 후 불가능하면 명령 건너뜀
    # 루트안에 담긴 모든 명령 수행후 로봇의 위치
    # 명령의 길이는 50까지\
    
    def isValid(row,col):
        return len(park)>row>=0 and len(park[0])>col>=0
    def convert_order(i):
        direction, move = i.split(" ")
        
        if direction == 'E':
            return [0,int(move)]
        elif direction == 'W':
            return [0,int(move)*-1]
        elif direction == 'N':
            return [int(move)*-1,0]
        else:
            return [int(move),0]
        
    def obsticle_route(robot_row, order_row, robot_col, order_col):
        moved_row, moved_col = robot_row+order_row, robot_col+order_col
        
        if moved_row - robot_row < 0:
            for i in range(robot_row-1,moved_row-1,-1):
                if tuple([i,robot_col]) in obsticle:
                    return False
        elif moved_row - robot_row > 0:
            for i in range(robot_row+1,moved_row+1):
                if tuple([i,robot_col]) in obsticle:
                    return False
        
        if moved_col - robot_col < 0:
            for i in range(robot_col-1,moved_col-1,-1):
                if tuple([robot_row,i]) in obsticle:
                    return False
        elif moved_col - robot_col > 0:
            for i in range(robot_col+1,moved_col+1):
                if tuple([robot_row,i]) in obsticle:
                    return False 
        return True

    start = [0,0]
    obsticle = set()
    row = len(park)
    cor = len(park[0])
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'X':
                obsticle.add(tuple([i,j]))
            elif park[i][j] == 'S':
                start = [i,j]
    
    robot_row, robot_col = start
    
    for i in routes:
        order_row,order_col = convert_order(i)
        
        # 이쪽방향으로 이동해도 벽을 넘어가지 않는지
        if not isValid(robot_row+order_row, robot_col+order_col):
            continue
        
        # 이동중에 장애물이 없는지
        if not obsticle_route(robot_row, order_row, robot_col, order_col):
            continue
        
        # 전부 통과하면 로봇 옮기기
        robot_row+=order_row
        robot_col+=order_col
    
    answer = [robot_row, robot_col]
    return answer