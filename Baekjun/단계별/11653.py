# 오답 소스 - 시간초과
# N = int(input())
# l = []; err = 0
# for num in range(2, N+1):
#     if num == 2:
#         l.append(num)
#     else:
#         err = 0
#         for i in range(2, num):
#             if num % i == 0:
#                 err += 1
#                 break
#         if err == 0:
#             l.append(num)
#
# for sosu in l:
#     if N != 1:
#         while N%sosu == 0:
#             N = N//sosu
#             print(sosu)

n = int(input())
i = 2
while n != 1:
    if n%i == 0:
        print(i)
        n = n/i
    else:
        i += 1  # 보다 작은 수로 나눌 수 있을 때까지 나눈 후 i가 증가하므로 소수 아닌 수(4 등)으로 나누어지지 않음