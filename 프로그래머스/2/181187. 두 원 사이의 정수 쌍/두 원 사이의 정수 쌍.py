import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        maxY = math.floor((r2**2 - x**2) ** 0.5)
        minY = 0 if x >= r1 else math.ceil((r1**2 - x**2) ** 0.5)
        answer += (maxY - minY + 1)
    return answer * 4  # 네 사분면 전체