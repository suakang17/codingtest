# 시간 초과
# M, N = map(int, input().split())
# for i in range(M, N+1):  # 판별할 수
#     if i == 1:
#         continue
#     elif i == 2:
#         print(2)
#     else:
#         for j in range(2, i):  # 나눌 수
#             if i % j == 0:  # 나눠떨어지면 소수 아님
#                 break
#             elif j == (i-1):
#                 print(i)

# 정답 소스 - 에라토스테네스의 체
m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:  # 1은 소수가 아니므로 제외
        continue
    for j in range(2, int(i**0.5)+1):  # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 해당 약수를 포함하는 수를 모두 제거할 수 있다(소수가 아니기에)
        if i % j == 0:  # 약수가 존재하므로 소수가 아님
            break    # 더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)

# 정답 소스 2 - 에라토스테네스의 체 - 사용자 정의 함수 구현
import sys
M, N = map(int, sys.stdin.readline().split())

def check_prime(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

for i in range(M, N + 1):
    if check_prime(i):
        print(i)


