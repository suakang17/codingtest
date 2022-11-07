import sys

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return True

T = int(sys.stdin.readline().strip())
for i in range(T):
    n = int(sys.stdin.readline().strip())  # 입력 처리
    a, b = n//2, n//2  # n은 무조건 짝수이므로 a+b 는 무조건 n이다
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1