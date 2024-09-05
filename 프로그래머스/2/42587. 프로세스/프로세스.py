def solution(priorities, location):
    
    order = sorted(priorities, reverse=True)
    pt = 0
    opt = 0
    
    answer = 0
    
    while(1):
        # print(priorities, pt, opt)
        if priorities[pt] == order[opt]:
            opt+=1
            answer+=1
            if pt == location:
                break
                
            priorities[pt] = None

        else:
            if pt >= len(priorities)-1:
                pt = 0
            else:
                pt+=1

    
    # print(answer)
    return answer

solution([1, 1, 9, 1, 1, 1],0)