# 내소스
result = 0
n, k = map(int, input().split())

while n != 1:
    if n % k == 0:
        while True:
            n //= k
            result += 1
            if n % k != 0 or n == 1:
                break
    else:
        while True:
            n -= 1
            result += 1
            if n % k == 0 or n == 1:
                break
print(result)

# ============================================= 답안
result = 0
n, k = map(int, input().split())

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# ============================================= 모범 답안
result = 0
n, k = map(int, input().split())

while True:
    target = (n//k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    n //= k
    result += 1

result += (n-1)
print(result)