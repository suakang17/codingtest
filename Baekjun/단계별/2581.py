M = int(input())  # M <= 소수의 개수 <= N
N = int(input())
l = []; err = 0
for num in range(M, N+1):
    if num == 1:
        continue
    if num == 2:
        l.append(num)
    else:
        err = 0
        for i in range(2, num):
            if num % i == 0:
                err += 1
                break
        if err == 0:
            l.append(num)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))