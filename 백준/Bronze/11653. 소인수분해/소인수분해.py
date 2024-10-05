import math

def prime_factorization(num):
    # 2부터 sqrt(num)까지의 소인수를 찾음
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            print(i)
            num //= i
    # 마지막 남은 수가 1보다 크면 그것도 소수임
    if num > 1:
        print(num)

num = int(input())
prime_factorization(num)
