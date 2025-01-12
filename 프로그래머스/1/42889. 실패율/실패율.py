from collections import defaultdict
def solution(N, stages):
    # memo = defaultdict(int)
    length = N+2
    memo = [0]*(length)
    total = len(stages)
    for i in stages: # 해당 스테이지에 멈춰있는 사람 말고 해당 스테이지를 통과한 사람도 통계를 매겨야함
        memo[i] += 1 # 어차피 탐색해야 한다면 딕트 필요없음
    # 그럼 뒤에서부터 하나씩 읽어서 하나씩 더하면?
    answer = [0]*(N+1)
    for i in range(length-2,0,-1):
        total_players = sum(memo[i:length])
        if total_players == 0:
            answer[i] = (0, i)
        else:
            answer[i] = (memo[i] / total_players, i)
    answer = answer[1:]
    # print(answer) # 실패율 완성
    
    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    ans = []
    for i in answer:
        ans.append(i[1])
        
    print(ans)
    # print(answer)
    
    return ans