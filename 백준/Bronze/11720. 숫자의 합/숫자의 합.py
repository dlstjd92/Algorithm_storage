how_num = int(input())

num_string = input()

ans = 0

for i in range(how_num):
    ans += int(num_string[i])

print(ans)