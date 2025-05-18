import math
def solution(n, w, num):
    answer = 0
    
    # 상자의 갯수 n 열의 길이 w 
    # 필요한 상자번호 num
    # 지그재그로
    
    target = []
    a = math.ceil(n/w)
    box = [[-1 for _ in range (w)] for _ in range(a)]
    
    row = 0
    col = 0
    reverse_flag = 1
    # 쌓고나서 뒤집기? <- 이게 맞네
    
    
    for i in range(1,n+1):
        box[row][col] = i
        if i == num:
            target = [row,col]
        col+=reverse_flag
        
        if col == w:
            col = w-1
            row += 1
            reverse_flag*=-1
        if col == -1:
            col = 0
            row+=1
            reverse_flag*=-1
    
    print(box, target)
    answer = len(box)-target[0]
    if box[len(box)-1][target[1]] == -1:
        answer-=1
    return answer