def solution(targets):
    targets.sort(key=lambda x: x[1])  # 끝나는 시점 기준 오름차순
    answer = 0
    last_shot = -1  # 마지막 미사일 쏜 지점

    for s, e in targets:
        if s >= last_shot:
            # 겹치지 않음 → 새 미사일 필요
            answer += 1
            last_shot = e  # 미사일은 끝 직전에 쏘는 게 최적

    return answer