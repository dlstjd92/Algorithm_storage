from datetime import timedelta
import math

def solution(h1, m1, s1, h2, m2, s2):
    # 1) 시작·끝을 초 단위로 환산
    t0 = h1*3600 + m1*60 + s1
    t1 = h2*3600 + m2*60 + s2

    # 2) 주기 정의
    T_sm = 3600.0 / 59.0      # 초침 ↔ 분침
    T_sh = 43200.0 / 719.0    # 초침 ↔ 시침

    events = []

    # 3) 초↔분 만남: k_start=ceil(t0/T), k_end=floor(t1/T)
    k_start_sm = math.ceil(t0 / T_sm)
    k_end_sm   = math.floor(t1 / T_sm)
    # (t0=0 일 때 k_start_sm=0, k=0 이벤트 포함)
    for k in range(k_start_sm, k_end_sm + 1):
        events.append(k * T_sm)

    # 4) 초↔시 만남
    k_start_sh = math.ceil(t0 / T_sh)
    k_end_sh   = math.floor(t1 / T_sh)
    for k in range(k_start_sh, k_end_sh + 1):
        events.append(k * T_sh)

    # 5) 중복 제거 (eps 내에서 같은 시각 하나로)
    eps = 1e-6
    events.sort()
    merged = []
    for t in events:
        if not merged or abs(t - merged[-1]) > eps:
            merged.append(t)

    return len(merged)