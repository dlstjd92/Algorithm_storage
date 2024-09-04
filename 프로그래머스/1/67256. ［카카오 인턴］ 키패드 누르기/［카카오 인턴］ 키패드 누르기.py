def solution(numbers, hand):
    lh = 10
    rh = 12
    answer = ''

    while (numbers):
        next = numbers.pop(0)
        # print(lh, rh, next)
        if next == 0: next = 11

        if next in [1, 4, 7]:
            answer += 'L'
            lh = next

        elif next in [3, 6, 9]:
            answer += 'R'
            rh = next

        else:

            a = abs(lh - next)
            b = abs(rh - next)

            if a//3 + a%3 < b//3 + b%3:
                answer += 'L'
                lh = next
            elif a//3 + a%3 > b//3 + b%3:
                answer += 'R'
                rh = next
            else:
                if hand == 'left':
                    answer += 'L'
                    lh = next
                else:
                    answer += 'R'
                    rh = next

    # print(answer)
    return answer

# solution([1,2,6,0], "left")
# solution([7,0,2], "right")