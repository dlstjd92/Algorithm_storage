def solution(board, h, w):
    answer = 0
    # 그냥 순수하게 순회돌면서 같으면 점수 더하죠
    # 와 순회도 아니야?
    # 그냥 찝은 칸 주위만 확인하면됨
    # 유의할거 isValid밖에 없음
    
    def isValid(row,col):
        return 0<=row<len(board) and 0<= col < len(board[0])
    def isSame(cur_color, other_color):
        return cur_color == other_color
    
    cur = board[h][w]
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    
    for row,col in directions:
        if isValid(h+row,w+col):
            if isSame(cur,board[h+row][w+col]):
                answer+=1
    
    return answer