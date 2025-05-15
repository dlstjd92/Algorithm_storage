import math
def solution(players, m, k):
    answer = 0
    # m은 서버당 수용할수있는 인원수
    # k는 서버당 구동할 수 있는 시간
    
    # 각 서버가 언제 구동되고 언제 꺼지는지 알아야함
    # 시간이 지날때마다 갱신해야하고
    
    # 반복은 24번 뿐인데 최악의 경우가 1000*24잖아
    # 꺼지는 시간을 키값으로, 서버 정보를 벨류값으로<- 이렇게 하면 현재 몇개 켜져있는지 알 수 없음
    server_shut = dict()
    servers = 1
    # 기본 서버수 1대
    for i in range(24):
        cur_player = players[i]
        # print("시작",i,"시","이시간 유저 수",cur_player, "서버수", servers)
        # 이때 꺼지는 서버가 있다면
        if i in server_shut:
            # print("꺼지는 서버 수",server_shut[i])
            servers -= server_shut[i]
        capacity = servers*m
        # print("수용가능한 인원", capacity)
        
        if cur_player >= capacity:
            # print("서버 증설", (cur_player-capacity)/m)
            needed_server = math.ceil((cur_player-capacity)/m+0.000001)
            
            server_shut[i+k] = needed_server
            answer += needed_server
            servers+=needed_server
            # print("증설 서버 수", needed_server)
        # print(answer)
    
    
    return answer