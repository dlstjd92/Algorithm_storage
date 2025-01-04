home, conn_num = list(map(int, input().split()))

loc_list = []

for _ in range(home):
    temp = int(input())
    loc_list.append(temp)
loc_list.sort()

# 이분 탐색 범위 초기화
min_dist = 1
max_dist = loc_list[-1] - loc_list[0]
result = 0

while min_dist <= max_dist:
    mid = (min_dist + max_dist) // 2

    # 공유기 설치 개수 계산
    cnt = 1
    cur = loc_list[0]

    for i in range(1, home):
        if loc_list[i] - cur >= mid:
            cnt += 1
            cur = loc_list[i]

    # 설치된 공유기 개수가 충분하면 거리 증가
    if cnt >= conn_num:
        result = mid  # 최적의 결과 갱신
        min_dist = mid + 1
    else:
        max_dist = mid - 1

print(result)
