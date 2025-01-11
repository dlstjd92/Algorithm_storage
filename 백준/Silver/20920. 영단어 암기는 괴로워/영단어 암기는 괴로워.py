import sys
from collections import defaultdict

# 입력값 처리
input_num = list(map(int, input().split()))  # [N, M]

memo = defaultdict(int)

# 입력받기
for _ in range(input_num[0]):
    curr = sys.stdin.readline().rstrip()
    if len(curr) >= input_num[1]:  # 길이가 M 이상인 단어만 고려
        memo[curr] += 1  # 출현 빈도 기록

# 정렬 기준:
# 1. 출현 빈도 역순 (많을수록 우선)
# 2. 길이 역순 (길수록 우선)
# 3. 사전순 (알파벳순)
sorted_words = sorted(memo.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 결과 출력
for word, count in sorted_words:
    print(word)
