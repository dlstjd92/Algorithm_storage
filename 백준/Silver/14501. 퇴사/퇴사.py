def best_schedule(schedule, day):
    dp = [0] * (day + 1)
    # n일 까지의 최댓값을 구하는 법
    # 1일부터 하루씩 더하면서
    # 해당일을 넣었을때와 뺏을때를 비교하면서 차례대로 상승
    # 만약 마지막상담과 겹치지 않으면? 무조건 넣는게 이득

    # if day == 0:
    #     if schedule[0][0] == 1:
    #         dp[0] = schedule[0][1]
    #     return dp

    # dp = best_schedule(schedule, day-1,dp)

    # if dp[day-1] != None:
    #     max_profit = dp[day-1]
    # else:
    #     max_profit = 0

    for i in range(day): # day - 1 까지 도는 포문..
        # 오늘의 최선 = 어제까지 최댓값 vs 오늘치를 포함했을 때의 값
        today = schedule[i][0]
        money = schedule[i][1]

        # 내일 값보다 오늘값이 더 높으면? 고
        dp[i+1] = max(dp[i+1],dp[i])

        # 오늘 상담을 했을때 해당 날짜랑 값 비교함
        if i + today <= day:
            dp[i + today] = max(dp[i + today], dp[i] + money)

    return dp

# def best_schedule(schedule, day):
#     dp = [0] * (day + 1)  # n일 이후는 상담을 못하므로 n + 1 크기 배열

#     for i in range(day):
#         t, p = schedule[i]  # t: 상담 기간, p: 상담 이익

#         # 현재 dp[i]까지의 최대 이익을 다음날로 이어줌 (상담을 안하는 경우)
#         dp[i + 1] = max(dp[i + 1], dp[i])

#         # 현재 상담을 선택할 경우 (상담이 끝난 날의 이익을 갱신)
#         if i + t <= day:  # 상담이 퇴사일을 넘지 않을 때만
#             dp[i + t] = max(dp[i + t], dp[i] + p)

#     return dp[day]

day = int(input())

schedule = []

for i in range(day):
    schedule.append(list(map(int,input().split())))

dp = [None]*day # 즉, dp도 schedule이랑 길이가 같을것

answer = best_schedule(schedule, day)

print(max(answer))

