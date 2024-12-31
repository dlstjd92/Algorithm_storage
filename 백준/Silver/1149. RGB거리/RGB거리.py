# house_num = int(input())
# ans = 0
# first = list(map(int,input().split()))
# min_num = min(first)
# before = first.index(min_num)
# print(min_num)
# ans += min_num
#
# for _ in range(house_num-1):
#     temp = list(map(int,input().split()))
#     temp[before] = 1001
#     min_num = min(temp)
#     before = temp.index(min_num)
#     print(min_num)
#     ans += min_num
#
# print(ans)
import copy
#
# house_num = int(input())
# ans = 0
# cost = []
# for _ in range(house_num):
#     cost.append(list(map(int,input().split())))
# min_num = min(cost[0])
# before = cost[0].index(min_num)
# temp_compare = before
# # print(min_num)
# # ans += min_num
# # print(cost)
#
# def recc(dp, last_use_paint):
#     # last_use_paint = None
#     len_dp = len(dp)
#     if len_dp == house_num:
#         return dp
#     before = None
#     temp = 0
#     temp_compare = copy.deepcopy(cost[len_dp])
#     if last_use_paint != None:
#         temp_compare[last_use_paint] = 1001
#     for i in range(len_dp,-1,-1):
#         temp_row = copy.deepcopy(cost[i])
#
#         if before != None:
#             temp_row[before] = 1001
#         else:
#             last_use_paint = temp_row.index(min(temp_row))
#             print("내가 집 수만큼 나와야 해", last_use_paint)
#         min_temp = min(temp_row)
#         print("사용한 최소숫자가 맞는지",min_temp)
#         temp += min_temp
#         before = temp_row.index(min_temp)
#         #제대로 계산 vs 역으로 계싼
#     print("여긴 템프 컴페어",temp_compare)
#     print("역계산과 전",temp, dp[-1]+min(temp_compare))
#     dp.append(min(dp[-1]+min(temp_compare),temp))
#     return recc(dp, last_use_paint)
#
# dp = recc([min_num], None)
#
# print(dp)

import sys
import copy
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

house_num = int(input().strip())   # 행(집)의 개수
cost = [list(map(int, input().split())) for _ in range(house_num)]
# cost[i] = [ cost_of_painting_i_th_house_in_color0,
#             cost_of_painting_i_th_house_in_color1,
#             cost_of_painting_i_th_house_in_color2 ]

def recc(dp):
    """
    dp: 2차원 리스트
      - dp[i] = [dp_i_0, dp_i_1, dp_i_2]
        (i번째 행에서 열 0,1,2를 골랐을 때 가능한 누적 최소합)

    재귀가 진행되면서 dp에 한 행씩 누적 정보를 추가한다.
    최종적으로 dp[-1] 에는 house_num-1번째 행까지 고려한 누적합이 담기며,
    그 중 최소값이 곧 정답.
    """
    # 현재 dp에 기록된 '행'의 개수
    row_idx = len(dp)

    # base case: 모든 행을 처리하면(= row_idx == house_num) 반환
    if row_idx == house_num:
        return dp

    # 만약 아직 dp가 비어있다면(= 첫 번째 행 처리),
    # cost[0][0], cost[0][1], cost[0][2] 그대로 넣어준다.
    if row_idx == 0:
        dp.append(copy.deepcopy(cost[0]))
        return recc(dp)

    # 그 외(row_idx >= 1)라면, 이전 행의 dp값을 활용해
    # 현재 행(row_idx)의 누적합을 구한다.
    prev = dp[-1]                 # 이전 행의 [열0최소, 열1최소, 열2최소]
    new_dp = [0, 0, 0]            # 현재 행에 대해 구해줄 값

    # 열 0을 골랐을 때
    new_dp[0] = cost[row_idx][0] + min(prev[1], prev[2])
    # 열 1을 골랐을 때
    new_dp[1] = cost[row_idx][1] + min(prev[0], prev[2])
    # 열 2를 골랐을 때
    new_dp[2] = cost[row_idx][2] + min(prev[0], prev[1])

    # dp에 new_dp를 붙여넣고, 재귀 진행
    dp.append(new_dp)
    return recc(dp)

# 실제 호출
dp_result = recc([])

# 모든 행을 처리한 뒤 dp_result[-1]에는 마지막 행까지의 누적 최소합 [열0, 열1, 열2]가 들어 있음
answer = min(dp_result[-1])
print(answer)

